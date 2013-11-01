cex.io-api-python
=================

CEX.IO API integration. Python sources.

Intro
=====

I. Download lib
II. Get API key and API secret on https://cex.io/trade/profile

USE
===

I. Create your python project
II. add "import cexapi" to your 
III. create class 
  "cexapiv = cexapi.api(username,api_key,api_secret)"
  where username - your username on cex.io
  api_key - your api key
  api_secret - your api secret code
IV. Use:
   a) API method parametrs
    1)couple = ("GHS\BTC" | "BF1\BTC") currency pair
    2)since = integer  return trades with tid >= since
    3)order_id = integer 
    4)ptype = ("sell" | "buy") type of order
    5)amount = float 
    6)price = float
      
    b) API methods
     1)ticker(couple = 'GHS/BTC') - get ticker
     2)order_book(couple = 'GHS/BTC') - get order
     3)trade_history(since = 1, couple = 'GHS/BTC') -  get all order
     4)balance() - get your balance
     5)open_orders(couple = 'GHS/BTC') - get open order
     6)cancel_order(order_id) - cancel order №order_id
     7)place_order(ptype = 'buy', amount = 1, price = 1, couple = 'GHS/BTC') - create order
     
    c) Full API documentation here: https://cex.io/api
    
V. Good use!
