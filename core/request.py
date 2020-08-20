# request.py

from datetime import datetime

from urllib3 import PoolManager

def execute_request(opts: dict)->bytes:
    """
    Executes the requisition using the API and fetches
    the content in JSON format.
    Returns the raw json data to be parsed
    """
    http = PoolManager()
    
    base_url = "https://api.exchangeratesapi.io/"
    queries = []
    query_str = ""

    if "currencies" in opts.keys():
        symbols = "symbols=" + ",".join(opts["currencies"])
        queries.append(symbols)
    
    if "base" in opts.keys():
        base = f"base={opts['base']}"
        queries.append(base)
    
    if "period" in opts.keys():
        start_date = datetime(*map(int, opts['period'][0:3])).date()
        end_date = datetime(*map(int, opts['period'][3:])).date()
        period = f"start_at={start_date}&end_at={end_date}"
        queries.insert(0, period)
        query_str = "history?" + "&".join(queries)

    elif "date" in opts.keys():
        date = str(datetime(*map(int, opts["date"])).date())
        query_str = date + "?" + "&".join(queries)
    
    else:
        today = datetime.today().date()
        query_str = str(today) + "?" + "&".join(queries)

    data = http.request("GET",base_url+query_str).data
    return data