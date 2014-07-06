# -*- coding: utf-8 -*-
import cexapi

demo = cexapi.api(username, api_key, api_secret)
print "Ticker (GHS/BTC)"
print demo.ticker() ## or demo.ticker('GHS/BTC')
print "Ticker (BF1/BTC)"
print demo.ticker('BF1/BTC')
print "Order book (GHS/BTC)"
print demo.order_book() ## or demo.order_book('GHS/BTC')
print "Order book (BF1/BTC)"
print demo.order_book('BF1/BTC')
print "Trade history since=100 (GHS/BTC)"
print demo.trade_history(100) ## or (100,'GHS/BTC')
print "Trade history since=100 (BF1/BTC)"
print demo.trade_history(100,'BF1/BTC')
print "Balance"
print demo.balance()
print "Open orders (GHS/BTC)"
print demo.current_orders() ## or ('GHS/BTC')
print "Open orders (BF1/BTC)"
print demo.current_orders('BF1/BTC')
print "Cancel order (order_id=100)"
print demo.cancel_order(100)
print "Plaсe order buy 4GHS/0.1BTC)"
print demo.place_order('buy',1,0.1) ## or ('buy',1,0.1,'GHS/BTC')
print "Open orders sell 1BF1/1.5BTC"
print demo.place_order('sell',1,1.5,'BF1/BTC')
