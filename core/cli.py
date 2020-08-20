import json

from cashier.common.utils import error, info

def display(data:bytes)-> None:
    """
    Display the requested content in a more readable way
    """

    content: dict = json.loads(data.decode("utf-8"))

    if "date" in content.keys():
        info(f"Base currency: {content['base']}")
        print("Currency(ies) requested")

        for currency, rate in content["rates"].items():
            print("\t" + str(currency) + "\t" + str(rate))

        info(f"Date of search: {content['date']}")
    
    elif "start_at" in content.keys():
        info(f"Base currency: {content['base']}")
        
        rates = list(content.pop("rates").items())
        
        for date, exchs in rates:
            info(f"Rates on date: {date}")
            for exch in exchs.items():
                print(f"\t{exch[0]}\t{exch[1]}")

        info(f"Start date:  {content['start_at']}")
        info(f"End date:    {content['end_at']}")

    elif "error" in content.keys():
        error(f"The following error occurred: \"{content['error']}\"")