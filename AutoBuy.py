import alpaca_trade_api as tradeapi

api_key = "PK2YDL5HZLD7MDC99FVL"

api_url= "https://paper-api.alpaca.markets"

secret_key = "RzWKFYB3kAnSh36lOnpoAlWkqF3PTgfSMu346X5i"


api = tradeapi.REST(
        api_key,
        secret_key,
        api_url
    )

#get account info and store it into a variable
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')



# Check how much money we can use to open new positions.
print('\n${} is available as buying power.\n\n\n'.format(account.buying_power))



orders = api.list_orders()
positions = api.list_positions()

# print("Current Orders: ", orders)

print("positions: ", positions)
print("Order canceled")

# Buy Order Template
api.cancel_order('Steve_Jobs_order')

api.submit_order(
    symbol='AAPL',  #Stock ticker
    qty=1,          # Number of Shares
    side='buy',     # Buy or Sell
    type='market', 
    time_in_force='gtc', #time, good til canceled
    #limit_price = 100   # Price limit to trigger order OPTIONAL
    client_order_id = 'Steve_Jobs_order' # set an id of the order, could be the politician name OPTIONAL
)

print("order received")



#print("Order cneceled")