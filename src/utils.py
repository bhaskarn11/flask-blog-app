from datetime import datetime, timezone
from dateutil import tz

def utc2local(utc_dt: datetime):
    tz_local = tz.tzlocal()
    utc_time = utc_dt.replace(tzinfo=timezone.utc)
    local_time = utc_time.astimezone(tz_local)
    
    return local_time
