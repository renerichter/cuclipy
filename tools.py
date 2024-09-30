from datetime import datetime, timedelta, timezone


def get_utc_offset(local_time=None,tzinfo=None,format_string="%Y%m%d %H%M%S"):
    if local_time is None:
        local_time = datetime.now()
    if isinstance(local_time,str):
        local_time = datetime.strptime(local_time, format_string)
    if local_time.tzinfo is None:
        local_time = local_time.astimezone(tzinfo)

    return local_time, local_time.utcoffset()

def convert_local_to_utc(input_time,tz_offset=None,verbose=False):
    # Step 1: parse input
    local_time = datetime.strptime(input_time, "%Y%m%d %H%M%S")
    # Step 2: Define the timezone offset (UTC+2)
    if tz_offset is None: local_time,tz_offset = get_utc_offset(local_time)
    # Step 3: Convert to UTC
    utc_time = local_time.astimezone(timezone.utc)
    if verbose: print(f"Time was: {local_time}.\n Time is: {utc_time}.")
    return utc_time

def time_to_ms(time_input):
    time_in_milliseconds = int(time_input.timestamp() * 1000)
    return time_in_milliseconds

def get_startend(local_time,utc_offset=None,tzinfo=None,format_string="%Y%m%d %H%M%S",verbose=False):
    if utc_offset is None: 
        local_time,utc_offset = get_utc_offset(local_time,tzinfo,format_string=format_string)
    if not isinstance(utc_offset, timedelta):
        raise ValueError("utc_offset must be a timedelta object")
    date = local_time.date()
    date_utc_start = datetime.combine(date, datetime.min.time(), local_time.tzinfo)-utc_offset
    date_utc_end = datetime.combine(date, datetime.max.time(), local_time.tzinfo)-utc_offset

    if verbose:
        print("Start of today in UTC:", date_utc_start)
        print("End of today in UTC:", date_utc_end)
    return date,date_utc_start,date_utc_end,utc_offset

def get_todays_startend(tzinfo=None,verbose=False):
    # Create a timezone object based on the offset
    _,date_utc_start,date_utc_end,_=get_startend(local_time=None,utc_offset=None,tzinfo=None,verbose=False)
    
    return date_utc_start,date_utc_end

def convert_ms_to_local_time(unix_time_in_ms,tzinfo=None,verbose= False):
    # Create a UTC datetime object from the Unix time in seconds
    utc_time = datetime.fromtimestamp(float(unix_time_in_ms) / 1000, tz=timezone.utc)

    # Convert to local time
    local_time = utc_time.astimezone(tzinfo)

    # Print local time in ISO format
    if verbose: 
        print(local_time.isoformat())
    return utc_time

def ms_to_hhmmss(duration_ms):
    seconds = int(duration_ms) // 1000
    minutes = seconds // 60
    hours = minutes // 60

    seconds = seconds % 60
    minutes = minutes % 60

    return f"{hours:02}h{minutes:02}m{seconds:02}s"