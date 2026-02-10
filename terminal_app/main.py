from scan_card import ScanCard

# application config
from config import Config

# init configuration
config = Config()

scan = ScanCard(config)
# read returns list with 2 elements [code 0 or 1, error message or card data]
print(scan.read())

