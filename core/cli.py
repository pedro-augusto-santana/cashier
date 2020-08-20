#cli.py
from datetime import datetime

from cashier.common.utils import error, info

def display(content: dict)-> None:
    """
    Display the requested content in a more readable way
    """

    if "date" in content.keys():
        info(f"Base currency: {content['base']}\n")
        print("Currency(ies) requested")

        for currency, rate in content["rates"].items():
            print("\t" + str(currency) + "\t" + str(rate))

        info(f"\nDate of search: {content['date']}")
    
    elif "start_at" in content.keys():
        info(f"Base currency: {content['base']}\n")
        
        rates = list(content.pop("rates").items())
        rates.sort(key=str) # sorting is using alphanumeric sorting, works well enough
        for date, exchs in rates:
            info(f"Rates on date: {date}")
            for exch in exchs.items():
                print(f"\t{exch[0]}\t{exch[1]}")

        info(f"\nStart date:  {content['start_at']}")
        info(f"End date:    {content['end_at']}")

    elif "error" in content.keys():
        error(f"The following error occurred: \"{content['error']}\"")