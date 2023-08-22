import robin_stocks.gemini as rg
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
gemini_api_secret = os.getenv('GEMINI_API_SECRET')

rg.login(gemini_api_key, gemini_api_secret)

# rg.use_sand_box_urls(use_sandbox=True)

# my_trades, error = rg.get_trades_for_crypto("BTCUSD", jsonify=True)

# if error:
#     print(error)
# else:
#     print(my_trades)
    
balance = rg.check_available_balances(jsonify=True)

print(balance)

