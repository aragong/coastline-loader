import os

import pandas as pd
import geopandas as gpd

from shapely.geometry import Polygon

SHP_DATABASE_DIR = os.environ.get("GSHHG_SHP_DATABASE_PATH")

class GetCoastline:    
    
    def __init__(self, resolution="c", lonlatbox=None, layer="L1"):

        if resolution not in ["c", "f", "h", "i", "l"]:
            # TODO - set standard ERROR
            print("ERROR!")
        
        self.gdf = self._load_from_shp(resolution, lonlatbox, layer)

    def _load_from_shp(self, resolution, lonlatbox, layer):
        if lonlatbox:
            polygon = Polygon(
                [
                    (lonlatbox[0], lonlatbox[2]),
                    (lonlatbox[0], lonlatbox[3]),
                    (lonlatbox[1], lonlatbox[3]),
                    (lonlatbox[1], lonlatbox[2]),
                    (lonlatbox[0], lonlatbox[2]),
                ]
            )

        path = os.path.join(
            SHP_DATABASE_DIR,
            "GSHHS_shp",
            resolution,
            f"GSHHS_{resolution}_{layer}.shp",
        )
        if polygon:
            gdf = gpd.GeoDataFrame.from_file(
                path, bbox=(lonlatbox[0], lonlatbox[2], lonlatbox[1], lonlatbox[3])
            ).set_crs(4326)
            gdf = gdf.clip(polygon).explode(index_parts=False)
        else:
            gdf = gpd.GeoDataFrame.from_file(path).set_crs(4326)
        return gdf.reset_index(drop=True)     


    def to_dataframe(self):
        df = pd.DataFrame([])
        for index, feature in enumerate(self.gdf.geometry):
            lon,lat = feature.exterior.coords.xy
            poly_id = [index]*len(feature.exterior.coords)
            tmp = pd.DataFrame({"polygon_id":poly_id, "longitude": lon, "latitude": lat})
            df = df.append(tmp)
        
        return df.reset_index(drop=True)         

