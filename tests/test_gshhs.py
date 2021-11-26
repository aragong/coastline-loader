import unittest
from coastline_loader.gshhs import GetCoastline


class TestGshhs(unittest.TestCase):
    def test_read_shp(self):
        coast = GetCoastline(resolution="f", lonlatbox=(-10, 15, 32.5, 52.5))
        self.assertIsNotNone(coast.gdf)
        df = coast.to_dataframe()
        self.assertIsNotNone(df)
