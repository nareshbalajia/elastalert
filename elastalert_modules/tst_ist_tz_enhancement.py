from datetime import datetime
from pytz import timezone

from elastalert.enhancements import BaseEnhancement
from elastalert.util import pretty_ts

"""
This Class will convert the incoming Timezone object of UTC offset to Taiwan/India Standard Timezone
"""
class ConvertTzInfo(BaseEnhancement):
    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        utc_ts = pretty_ts(match['@timestamp'])
        taipei_tz = timezone('Asia/Taipei')
        india_tz = timezone('Asia/Kolkata')

        ist_tz = utc_ts.astimezone(india_tz)
        match['@timestamp'] = pretty_ts(ist_tz, False)
