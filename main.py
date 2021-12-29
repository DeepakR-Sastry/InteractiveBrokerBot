from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer
from ibapi.contract import *
from ibapi.common import SetOfString
from ibapi.common import SetOfFloat
from ibapi.ticktype import TickTypeEnum
import datetime
from datetime import date
from datetime import datetime

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("ERROR: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()

    def securityDefinitionOptionParameter(self, reqId:int, exchange:str,
        underlyingConId:int, tradingClass:str, multiplier:str,
        expirations:SetOfString, strikes:SetOfFloat):
        print("SecurityDefinitionOptionParameter.", "ReqId:", reqId, "Exchange:", exchange, "Underlying conId:", underlyingConId, "TradingClass:", tradingClass, "Multiplier:", multiplier,
              "Expirations:", expirations, "Strikes:", str(strikes), "\n")


    def securityDefinitionOptionParameterEnd(self, reqId:int):
        print("SecurityDefinitionOptionParameterEnd. ReqId:", reqId)


    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        print(contractDetails)



    def contractDetailsEnd(self, reqId):
        print("\ncontractDetails End\n")

    def tickPrice(self, reqId, tickType, price, attrib):
        #print("Price:",price, "TickType:",TickTypeEnum.to_str(tickType),"Price:", price, end = " ")
        return price

    def tickSize(self, reqId, tickType, size):
        print("Tick Size. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)


    def weekDay(self):
        weeklyDate = datetime.date.today()
        while weeklyDate.weekday() != 0:
            weeklyDate += datetime.timedelta(1)
        weeklyString = weeklyDate.strftime("%Y%m%d")
        return weeklyString

    def accountSummary(self, reqId:int, account:str, tag:str, value:str,
                       currency:str):
        super().accountSummary(reqId, account, tag, value, currency)
        print("AccountSummary. ReqId:", reqId, "Account:", account, "Tag:", tag, "Value:", value, "Currency:", currency)

    def accountSummaryEnd(self, reqId: int):
        super().accountSummaryEnd(reqId)
        print("AccountSummaryEnd. ReqId:", reqId)

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print("OrderStatus. Id:", orderId, ", Status: ", status, ", Filled: ", filled, ", Remaining: ", remaining, ", LastFillPrice: ", lastFillPrice)

    def openOrder(self, orderId, contract, order,
                  orderState):
        print(orderId, contract.symbol, contract.secType, contract.exchange, order.action, order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId:int, contract:Contract, execution):
        print("ExecDetails. ", reqId, contract.symbol, contract.secType,contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)








    def start(self):
        now = datetime.now()
        current_time = now.strftime("%H%M%S")


        if date.today().weekday()==0 and current_time == "073000":
            contract = Contract()
            contract.symbol = "SPY"
            contract.secType = "STK"
            contract.exchange = "SMART"
            contract.currency = "USD"

            #weeklyString = self.weekDay()

        # check if it is a monday. Sell a put with strike price = underlying - 10 if
        # todayDate = datetime.date.today()
        # while d.weekday() != 0:
        #     d += datetime.timedelta(1)
        # weeklyDate = todayDate + datetime.timedelta(days=7)
        # weeklyString = weeklyDate.strftime("%Y%m%d")
        #print(weeklyDate)
        #weeklyString = self.weekDay()
        # contract = Contract()
        # contract.symbol = "SPY"
        # contract.secType = "OPT"
        # contract.exchange = "SMART"
        # contract.currency = "USD"
        # contract.right = "PUT"
        # contract.strike = 467
        # contract.lastTradeDateOrContractMonth = 20220103
        #
        #
        #
        # order = Order()
        # order.action = "SELL"
        # order.totalQuantity = 1
        # order.orderType = "MKT"
        #
        # self.placeOrder(self.nextOrderId, contract, order)

        #contract.lastTradeDateOrContractMonth = weeklyString
        #self.reqMarketDataType(3)
        #self.reqMktData(1, contract, "", False, False, [])
        #self.reqAccountSummary(2, "All", "TotalCashValue")

        #self.reqContractDetails(1, contract)



    def stop(self):
        self.done = True
        self.disconnect()

def main():
    app = TestApp()
    app.nextOrderId = 11
    app.connect("127.0.0.1", 7497, 0)

    Timer(4, app.stop).start()
    app.run()

if __name__ == "__main__":
    main()

