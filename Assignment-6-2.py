import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

# Load data
df = pd.read_csv("MUSEUM_20250430.csv")

# Count museums by district
counts = df['CITY'].value_counts().sort_index()

# Define the same color mapping used on the map
color_map = {
    "Bronx":           "#2ca02c",  # green
    "Brooklyn":        "#9467bd",  # purple
    "Jackson Heights": "#8c564b",  # brownish
    "Long Island City":"#d62728",  # red
    "New York":        "#1f77b4",  # blue
    "Queens":          "#ff7f0e",  # orange
    "Staten Island":   "#e377c2",  # pink
}

# Generate a colors list aligned with counts.index
colors = [color_map[d] for d in counts.index]

# ---------------------------
# 1) Glowing Bar Chart
# ---------------------------
fig1, ax1 = plt.subplots(figsize=(10, 5), facecolor='black')
ax1.set_facecolor('black')
bars = ax1.bar(counts.index, counts.values, color=colors)

# Add glow effect to each bar
for bar, c in zip(bars, colors):
    bar.set_path_effects([
        path_effects.Stroke(linewidth=20, foreground=c, alpha=0.3),
        path_effects.Normal()
    ])

# Style text and axes
ax1.set_title('Number of Museums by District', color='white', fontsize=16)
ax1.set_xlabel('District', color='white', fontsize=12)
ax1.set_ylabel('Number of Museums', color='white', fontsize=12)
ax1.tick_params(colors='white', labelsize=10)
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
for spine in ax1.spines.values():
    spine.set_edgecolor('white')

plt.tight_layout()

# ---------------------------
# 2) Glowing Pie Chart
# ---------------------------
fig2, ax2 = plt.subplots(figsize=(6, 6), facecolor='black')
ax2.set_facecolor('black')

wedges, texts, autotexts = ax2.pie(
    counts.values,
    colors=colors,
    labels=counts.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(width=0.4)
)

# Add glow effect to wedges
for wedge, c in zip(wedges, colors):
    wedge.set_path_effects([
        path_effects.Stroke(linewidth=20, foreground=c, alpha=0.3),
        path_effects.Normal()
    ])

# Style text
for txt in texts + autotexts:
    txt.set_color('white')

ax2.set_title('Distribution of Museums by District', color='white', fontsize=16)
ax2.set_ylabel('')

plt.tight_layout()
plt.show()