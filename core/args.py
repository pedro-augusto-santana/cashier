# args.py

"""
Argument processing and cli option parsing
"""

import argparse
import datetime

from cashier.common.utils import error

parser = argparse.ArgumentParser(
    description="Command line interface for displaying exchange rates.",
    usage="cashier [OPTIONS]")
parser.add_argument("-b", "--base", type=str, help="The base used for the conversion ( defaults to EUR )")
parser.add_argument("-d","--date", help="Query for a specific date (min year = 1999) (defaults to latest)",nargs="+")
parser.add_argument("-p","--period", help="Query for a specific time period (min year = 1999)",nargs="+")
parser.add_argument("-l","--list", help="List only the selected currencies", nargs="+")


args = parser.parse_args()

def parse_args()->dict:
    """
    Parses the command line arguments and returns a dictionary
    with the options
    """
    opts = {}

    if args.date and args.period:
        error("Conflicting arguments || invalid use of --period and --date")
        exit(-1)

    if args.base:
       opts["base"] = args.base

    if args.list:
        opts["currencies"] = args.list
    
    if args.period:
        if not (_check_date_fmt([int(i) for i in args.period[0:3]])and
        _check_date_fmt([int(i) for i in args.period[3:]])):
            error("Invalid time period provided")
            exit(-1)
        elif len(args.period) < 6:
                error("An incomplete date was provided")
                error("REQUIRED FORMAT - START DATE [YY MM DD] - END DATE [YY MM DD]")
                exit(-1)
        opts["period"] = args.period
    
    if args.date:
        if len(args.date) < 3:
            error("An incomplete date was provided")
            error("REQUIRED FORMAT - DATE [YY MM DD]")
            exit(-1)

        if not _check_date_fmt([int(i) for i in args.date]):
            error("Invalid date provided")
            exit(-1)
        
        opts["date"] = args.date

    return opts or {}

def _check_date_fmt(date:list)->bool:
    """
    Verifies if the dates provided are valid, preventing
    unnecessary API requisitions
    """
    try:
        datetime.datetime(date[0],date[1],date[2])
    
    except ValueError:
        return False

    # if the provided date is ahead of present day (TODO: implement precognition)
    if datetime.datetime(date[0],date[1],date[2]) > datetime.datetime.now():
        return False

    # the API used only goes back to 1999
    if date[0] < 1999:
        return False
    
    return True