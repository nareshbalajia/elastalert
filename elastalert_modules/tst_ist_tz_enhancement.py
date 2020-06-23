from datetime import datetime
from pytz import timezone

from elastalert.enhancements import BaseEnhancement
from elastalert.util import ts_to_dt, pretty_ts, elastalert_logger

"""
This Class will convert the incoming Timezone object of UTC offset to Taiwan/India Standard Timezone
"""
class ConvertTzInfo(BaseEnhancement):
    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        
        elastalert_logger.info("Received UTC Time %s" % (match['@timestamp']))
        utc_ts = match['@timestamp']
        if not isinstance(utc_ts, datetime):
            utc_ts = ts_to_dt(utc_ts)

        taipei_tz = timezone('Asia/Taipei')
        india_tz = timezone('Asia/Kolkata')

        ist_tz = utc_ts.astimezone(india_tz)
        match['@timestamp'] = pretty_ts(ist_tz, False)
