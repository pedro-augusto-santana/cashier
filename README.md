# cashier
Python command line utility for checking exchange rates 

# Usage
python3 -m cashier [ options ]

- -l --list [ currencies ] : Display only the selected currencies ( using iso 4217 notation )
- -b --base [ base ] : To wich currencies will be compared against
- -d --date [ date ] : Request a specific date to be compared
- -p --period [ start_at end_at ] : Request a specific time period

# Dependencies
  cashier does not have any dependencies and is writen in python 3 (developed in 3.8.2 in Ubuntu 20.04 LTS ) using the standard libraries.
 
# Installation
As of now, cashier cannot be installed as a program utility. But it can be executed as a module with "python3 -m cashier [options]"

# Credit
cashier uses Exchange Rates API ( exchangeratesapi.io/ ). All credit is due.
