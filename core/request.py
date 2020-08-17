# request.py

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
        period = f"start_at={'-'.join(opts['period'][0:3])}&end_at={'-'.join(opts['period'][3:])}"
        queries.insert(0, period)
        query_str = "history?" + "&".join(queries)

    elif "date" in opts.keys():
        date = "-".join(opts["date"])
        queries.insert(0, date)
        query_str = queries[0] + "?" + "&".join(queries[1:])
    
    else:
        query_str = "latest?" + "&".join(queries)

    data = http.request("GET",base_url+query_str).data
    return data