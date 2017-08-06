import wbdata
import pandas as pd
import domain

def _build_countries():
    countries = wbdata.get_country(display=False)
    return pd.DataFrame([{"id": x['id'], 'iso2': x['iso2Code'], 'name': x['name']} for x in countries], index=[x['id'] for x in countries])

countries = _build_countries()
