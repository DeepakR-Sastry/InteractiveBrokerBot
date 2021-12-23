import ibapi

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.contract import Contract
from ibapi.order import *
import threading
import time

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

class Bot():
    ib = None
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7497, 1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)


        symbol = input("Enter the symbol you want to trade")
        order = Order()
        order.orderType = "MKT"
        order.action = "BUY"
        quantity = 1
        order.totalQuantity = quantity

        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK"

        contract.exchange = "SMART"
        contract.primaryExchange = "ISLAND"
        contract.currency = "USD"

        self.ib.placeOrder(3, contract, order)

    def run_loop(self):
        self.ib.run()




bot = Bot()
