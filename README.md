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

II. add "import cexapi" to your project

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
    
V. Live Use
        >>> import ceapi<br>
        >>> api = cexapi.api(username, api_key, api_secret)<br>
        >>> print api.balance()<br>
        {u'timestamp': u'1383378763', u'BTC': {u'available': u'0.04722110', u'orders': u'0.00170000'}, u'GHS': {u'available': u'0.01000000'}}<br>
        >>> print api.order_book('BF1/BTC')<br>
        {u'timestamp': u'1383378967', u'bids': [[u'1.7', u'0.30100000'], [u'1.67', u'0.00011000'], [u'0.8', u'0.02070000'], [u'0.1002', u'0.27748002'], [u'0.1', u'0.10000000'], [u'0.011', u'0.30500000'], [u'0.009', u'1.00000000'], [u'0.00171', u'0.00100000'], [u'0.0012', u'1.00000000'], [u'0.00116819', u'0.50000000'], [u'0.001002', u'33.00000000'], [u'0.001001', u'53.00000000'], [u'0.001', u'3.00000000'], [u'0.00097626', u'36.00000000'], [u'0.0006', u'85.00000000'], [u'0.00058409', u'0.50000000'], [u'0.0004889', u'0.06823960'], [u'0.0003', u'1.00000000'], [u'0.00029204', u'0.90000000'], [u'0.0001', u'101.00000000']], u'asks': []}<br>
        >>> print api.open_orders('BF1/BTC')<br>
        [{u'price': u'1.7', u'amount': u'0.00100000', u'time': u'1383378514737', u'type': u'buy', u'id': u'6219104', u'pending': u'0.00100000'}]<br>
        >>> print api.place_order('buy', 0.001, 1.7, 'BF1/BTC')<br>
        {u'price': u'1.7', u'amount': u'0.00100000', u'time': 1383378987622, u'type': u'buy', u'id': u'6219145', u'pending': u'0.00100000'}<br>
        >>> print api.cancel_order(6219145)<br>
        True<br>
        >>> print api.place_order('buy', 0.01, 0.10789, 'GHS/BTC')<br>
        {u'price': u'0.10789', u'amount': u'0.01000000', u'time': 1383379024072, u'type': u'buy', u'id': u'6219150', u'pending': u'0.00000000'}<br>
        >>> print api.ticker('GHS/BTC')<br>
        {u'volume': u'7154.78339022', u'last': u'0.1078', u'timestamp': u'1383379041', u'bid': u'0.10778', u'high': u'0.10799999', u'low': u'0.10670076', u'ask': u'0.10780000000000001'}<br>
        >>> print api.balance()<br>
        {u'timestamp': u'1383379054', u'BTC': {u'available': u'0.04614310', u'orders': u'0.00170000'}, u'GHS': {u'available': u'0.02000000'}}<br>
