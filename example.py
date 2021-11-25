import matplotlib.pyplot as plt
from gshhs import GetCoastline

# Load to GeoDataFrame from GSHHS database in Esri-shape format
coast = GetCoastline(resolution="f", lonlatbox=(-10, 15, 32.5, 52.5))
coast.gdf.head()

# Transform to standard DataFrame
df = coast.to_dataframe()
df.head()

# Plot from DataFrame
fig, ax = plt.subplots()
for i in df["polygon_id"].unique():
    df[df["polygon_id"]==i].plot(x="longitude", y="latitude", ax=ax, legend=False)
plt.show()

# Plot from GeoDataFrame
coast.gdf.plot()
plt.show()
