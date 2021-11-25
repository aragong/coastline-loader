# Coastline-loader
- `GetCoastline` (class) - Load coastlines from GSHHS database to GeoDataFrame.
- `.to_dataframe()` (method) - Convert GeoDataFrame to standard DataFrame. 

---

## :house: Installation
1. Clone this repository to your local machine and install the conda environment defined in [environment.yml](environment.yml). You can use pip or directly conda usinge the next command:
    ```bash
    conda create --file environment.yml
    ```

2. Download GSHHS database (shapefile) from [GSHHC web-site](https://www.soest.hawaii.edu/pwessel/gshhg/) or directly using this [link](http://www.soest.hawaii.edu/pwessel/gshhg/gshhg-shp-2.3.7.zip).

3. Extract content of the compressed file downloaded.

4. Set path to "gshhg-gmt-2.3.7" folder in `.env` file.

---

## :heavy_check_mark: Tests: 
- [tests/test_gshhs.py](tests/test_gshhs.py)

---

## :rocket: Examples:
- [example.py](example.py)
- [example.ipynb](example.ipynb)

---
## :grey_question: More info
For more information about this database, resolutions and layers... please check
[GSHHC web-site](https://www.soest.hawaii.edu/pwessel/gshhg/).

---
## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).