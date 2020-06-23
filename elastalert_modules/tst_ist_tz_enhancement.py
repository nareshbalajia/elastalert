from elastalert.enhancements import BaseEnhancement

"""
This Class will convert the incoming Timezone object of UTC offset to Taiwan/India Standard Timezone
"""
class ConvertTzInfo(BaseEnhancement):
    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        utc_ts = match['@timestamp']
        
