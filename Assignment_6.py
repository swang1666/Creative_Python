import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv("MUSEUM_20250430.csv")

def extract_lon(geom):
    x,y = geom.replace("POINT (","").replace(")","").split()
    return float(x)

def extract_lat(geom):
    x,y = geom.replace("POINT (","").replace(")","").split()
    return float(y)

df["lon"] = df["the_geom"].apply(extract_lon)
df["lat"] = df["the_geom"].apply(extract_lat)


group_field = "CITY"  
categories = df[group_field].unique().tolist()

palette = px.colors.qualitative.Dark24

color_map = {cat: palette[i % len(palette)] for i, cat in enumerate(categories)}


fig = go.Figure()

for city, sub in df.groupby(group_field):
    col = color_map[city]
   
    fig.add_trace(go.Scattermapbox(
        lat=sub["lat"], lon=sub["lon"],
        marker=dict(size=50, color=col, opacity=0.15),
        hoverinfo="none", showlegend=False
    ))
   
    for _, row in sub.iterrows():
        fig.add_trace(go.Scattermapbox(
            lat=[row["lat"], row["lat"] + 0.005],
            lon=[row["lon"], row["lon"]],
            mode="lines",
            line=dict(color="white", width=1),
            hoverinfo="none", showlegend=False
        ))
    
    fig.add_trace(go.Scattermapbox(
        lat=sub["lat"], lon=sub["lon"],
        mode="markers+text",
        marker=dict(size=8, color=col, opacity=1),
        text=sub["NAME"],
        textposition="top center",
        textfont=dict(color=col, size=10),
        hoverinfo="none", showlegend=False
    ))


fig.update_layout(
    mapbox=dict(
        style="mapbox://styles/mapbox/dark-v10",
        accesstoken="pk.eyJ1Ijoid2FuZ3M2ODciLCJhIjoiY21hNHFxeGwxMDl4MDJqcHdtNmwyOWZtYyJ9.N1Umf2LjwqocE98Hh49_pA",  
        center=dict(lat=40.75, lon=-73.98),
        zoom=10
    ),
    margin=dict(t=0, b=0, l=0, r=0),
    paper_bgcolor="black",
)

fig.show()
