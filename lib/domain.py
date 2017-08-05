import iso3166
import pandas as pd


def _build_countries():
    data = [{'name': c.name, 'code': c.alpha3, 'code2': c.alpha2, 'numeric': int(c.numeric)} for c in iso3166.countries]
    return pd.DataFrame(data, index = [d["code"] for d in data])

countries = _build_countries()
