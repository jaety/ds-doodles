import wbdata
import fastparquet as fp
import os
import domain
import pandas as pd
import math

dest_dir = os.path.abspath(os.path.join(os.path.split(__file__)[0], "../data"))

def to_float(v):
    return float(v) if v is not None else math.nan

def world_bank(indicator):
    codes = domain.countries.set_index('iso2')['id']
    data = wbdata.get_data(indicator)
    index = pd.MultiIndex.from_tuples([(codes[x['country']['id']], int(x['date'])) for x in data], names=["country", "year"])
    return pd.Series([to_float(x['value']) for x in data], index=index, name=indicator.replace(".","_")).sort_index()

def ingest_world_bank(indicator, dest=None):
    dest = dest if not dest == None else os.path.join(dest_dir, indicator + ".parquet")
    df = world_bank(indicator)
    fp.write(dest, df)
    return df
