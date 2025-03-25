import wave
import struct
import math
import numpy as np

# Parameters
SAMPLE_RATE = 44100      # Samples per second
DURATION = 2.0           # Total length of generated sound in seconds
NUM_TIME_STEPS = 100     # How many "chunks" across time we’ll split (left -> right)
FREQS = np.linspace(200, 2000, 10)  # A set of frequencies (low to high)
MAX_AMPLITUDE = 32767.0  # Max amplitude for 16-bit audio

# We'll pretend each vertical "slice" from left to right has a random subset
# of frequencies "active," with volume scaled by the density in that slice.
# Denser black in the image => more frequencies + higher volume.

# For demonstration, let's define a manual "density curve" 
# that starts high (dense on the left) and gradually decreases (sparse on the right).
# In a real scenario, you'd map actual pixel data from the image.
density_curve = np.linspace(1.0, 0.1, NUM_TIME_STEPS)

# Generate the waveform
num_samples = int(SAMPLE_RATE * DURATION)
wave_data = np.zeros(num_samples, dtype=np.float32)

# Determine how many samples each chunk (vertical slice) spans
samples_per_step = num_samples // NUM_TIME_STEPS

# Synthesize chunk-by-chunk
start_sample = 0
for i in range(NUM_TIME_STEPS):
    end_sample = start_sample + samples_per_step
    
    # The "density" at this time step (i.e. how many freqs + amplitude)
    density = density_curve[i]
    
    # Let’s pick frequencies to "turn on" in this slice.
    # For example, we’ll randomly choose half of them on average
    # and scale their volume by the density.
    active_freqs = []
    for f in FREQS:
        if np.random.rand() < density:
            active_freqs.append(f)
    
    # Synthesize the samples for this slice
    t = np.linspace(0, (samples_per_step-1)/SAMPLE_RATE, samples_per_step)
    slice_wave = np.zeros_like(t, dtype=np.float32)

    # Add up each active frequency
    for f in active_freqs:
        # A simple sine wave for each frequency
        slice_wave += np.sin(2 * math.pi * f * t) * density

    # Insert this slice into wave_data
    wave_data[start_sample:end_sample] += slice_wave
    start_sample = end_sample

# Normalize the final wave data to avoid clipping
max_val = np.max(np.abs(wave_data))
if max_val > 0:
    wave_data = (wave_data / max_val) * 0.9  # keep some headroom

# Write to a 16-bit WAV file
with wave.open("image_based_sound.wav", 'wb') as wf:
    wf.setnchannels(1)           # mono
    wf.setsampwidth(2)          # 16 bits
    wf.setframerate(SAMPLE_RATE)
    
    # Convert float32 samples to 16-bit and write
    for sample in wave_data:
        wf.writeframesraw(struct.pack('<h', int(sample * MAX_AMPLITUDE)))

print("Finished generating 'image_based_sound.wav'.")
