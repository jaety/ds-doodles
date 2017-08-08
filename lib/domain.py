import wbdata
import pandas as pd
import domain
from functools import total_ordering

from enum import Enum
def _build_countries():
    countries = wbdata.get_country(display=False)
    return pd.DataFrame([{"id": x['id'], 'iso2': x['iso2Code'], 'name': x['name']} for x in countries], index=[x['id'] for x in countries])

# countries = _build_countries()



"""
# Use Pandas Periods & DateTimes 
class Frequency(Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


@total_ordering
class Period(object):
    def __init__(self, freq, offset):
        self.freq = freq
        self.offset = offset

    ZERO_YEAR = 1970

    def __eq__(self, other):
        return (
            hasattr(other, 'freq') and
            hasattr(other, 'offset') and
            self.freq == other.freq and
            self.offset == other.offset
        )

    def __lt__(self, other):
        return self.offset < other.offset

    def __repr__(self):


    @classmethod
    def parse(cls, string_period):
        """ Takes string representation of period. 1970-01-01 """
        pieces = string_period.split("-")
        if (len(pieces) == 1):
            (year,) = pieces.map(int)
            offset = year - Period.ZERO_YEAR
            return Period(Frequency.YEAR, offset)
        elif (len(pieces) == 2):
            (year, month) = pieces.map(int)
            assert month >= 1 and month <= 12, "month %d is not in 1-12" % month
            offset = (year - Period.ZERO_YEAR)*12 + month
            return Period(Frequency.MONTH, offset)
        elif (len(pieces) == 3):
            raise NotImplementedError("Daily period math not yet implemented")
            (year, month, day) = pieces.map(int)
            return Period(Frequency.DAY, offset)
"""
