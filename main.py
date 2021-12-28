from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer
from ibapi.contract import *
from ibapi.common import SetOfString
from ibapi.common import SetOfFloat
import datetime

class TestApp(EWrapper, EClient):
    highestStrikePrice = 0
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("ERROR: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.start()

    def securityDefinitionOptionParameter(self, reqId:int, exchange:str,
        underlyingConId:int, tradingClass:str, multiplier:str,
        expirations:SetOfString, strikes:SetOfFloat):
        print("SecurityDefinitionOptionParameter.", "ReqId:", reqId, "Exchange:", exchange, "Underlying conId:", underlyingConId, "TradingClass:", tradingClass, "Multiplier:", multiplier,
              "Expirations:", expirations, "Strikes:", str(strikes), "\n")


    def securityDefinitionOptionParameterEnd(self, reqId:int):
        print("SecurityDefinitionOptionParameterEnd. ReqId:", reqId)


    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        self.highestStrike(contractDetails)



    def contractDetailsEnd(self, reqId):
        print(self.highestStrikePrice)
        print("\ncontractDetails End\n")

    def highestStrike(self, contractDetails):
        contract = contractDetails.contract
        if contract.strike > self.highestStrikePrice:
            self.highestStrikePrice = contract.strike



    def start(self):
        todayDate = datetime.date.today()
        weeklyDate = todayDate + datetime.timedelta(days=7)
        weeklyString = weeklyDate.strftime("%Y%m%d")
        #print(weeklyDate)
        contract = Contract()
        contract.symbol = "SPY"
        contract.secType = "OPT"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = weeklyString
        self.reqContractDetails(1, contract)



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

