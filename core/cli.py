import json 

from cashier.common.utils import error

def display(data:bytes)-> None:
    """
    Display the requested content in a more readable way
    """

    content: dict = json.loads(data.decode("utf-8"))

    if "date" in content.keys():
        print(f"Base currency: {content['base']}")
        print("Currency(ies) requested")

        for currency, rate in content["rates"].items():
            print("\t" + str(currency) + "\t" + str(rate))

        print(f"Date of search: {content['date']}")
    
    elif "start_at" in content.keys():
        print(f"Base currency: {content['base']}")
        
        for date, rates in content["rates"].items():
            print(f"Rates on date: {date}")
            for currency, rate in rates.items():
                print("\t" + str(currency) + "\t" + str(rate))
        
        print(f"Start date: {content['start_at']}")
        print(f"End date: {content['end_at']}")

    elif "error" in content.keys():
        error(f"The following error occurred: \"{content['error']}\"")