import os

import pandas as pd
import geopandas as gpd

from shapely.geometry import Polygon

SHP_DATABASE_DIR = os.environ.get("GSHHG_SHP_DATABASE_PATH")


class GetCoastline:
    def __init__(
        self,
        resolution: str = "f",
        lonlatbox: tuple = None,
        output_epsg: int = None,
        layer: str = "L1",
    ) -> None:
        """Load GSHHS coastline database to GeoDataFrame.
        Clip and convert coordinates to required lonlatbox and epsg code, if required.

        Args:
            resolution (str, optional): GSHHS resolution "f", "h", "i", "l" or "c" (full, high, intermediate, low or crude). Defaults to "c".
            lonlatbox (tuple, optional): box coordinates, (lonmin, lonmax, latmin, latmax). Defaults to None.
            output_epsg (int, optional): epsg-code for output transformation. Defaults to None.
            layer (str, optional): layer from GSHHS database. Defaults to "L1".
        """

        if resolution not in ["c", "f", "h", "i", "l"]:
            # TODO - set standard ERROR
            print("ERROR!")

        self.gdf = self._load_from_shp(resolution, lonlatbox, output_epsg, layer)

    def _load_from_shp(
        self, resolution: str, lonlatbox: tuple, output_epsg: int, layer: str
    ) -> gpd.GeoDataFrame:
        """Load and clip GSHHS shapefile (layer "L1") and convert to required epsg, if needed

        Args:
            resolution (str): GSHHS database resolution
            lonlatbox (tuple): box coordinates, (lonmin, lonmax, latmin, latmax)
            output_epsg (int): epsg-code for output transformation
            layer (str): GSHHS database layer

        Returns:
            gpd.GeoDataFrame: costlines polygons
        """
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
        print(SHP_DATABASE_DIR)
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

        if output_epsg:
            gdf = gdf.to_crs(output_epsg)

        return gdf.reset_index(drop=True)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert GeoDataFrame to standard DataFrame

        Returns:
            pd.DataFrame: costlines polygons
        """
        df = pd.DataFrame([])
        dataframes = []
        for index, (feature, area) in enumerate(zip(self.gdf.geometry, self.gdf.area)):
            lon, lat = feature.exterior.coords.xy
            poly_id = [index] * len(feature.exterior.coords)
            area = [area] * len(feature.exterior.coords)
            tmp = pd.DataFrame(
                {"polygon_id": poly_id, "longitude": lon, "latitude": lat, "area": area}
            )
            dataframes.append(tmp)
        df = pd.concat(dataframes, ignore_index=True)
        return df.reset_index(drop=True)
