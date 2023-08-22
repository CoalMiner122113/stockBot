import robin_stocks.robinhood as rs
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('ROBINHOOD_USERNAME')
password = os.getenv('ROBINHOOD_PASSWORD')


login = rs.login(
    username=username,
    password=password,
    expiresIn=86400,
    store_session=True
)

print(login)

