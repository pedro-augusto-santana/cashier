### CASHIER
# COMMAND LINE PROGRAM FOR CONSULTING EXCHANGE RATES
# THIS SOFTWARE USES https://exchangeratesapi.io/ ALL CREDIT IS DUE TO MADIS VÄIN (https://github.com/madisvain).

# AUTHOR: PEDRO AUGUSTO SANTANA
# GITHUB: https://github.com/pedro-augusto-santana
###

from cashier.core import args
from cashier.core import request
from cashier.core import cli

def main():
    opts = args.parse_args()
    data = request.execute_request(opts)
    cli.display(data)

if __name__ == "__main__":
    main()
    exit(0)