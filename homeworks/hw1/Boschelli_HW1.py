import random

class Portfollio():
    def __init__(self, cash=0):
        self.cash=cash
        self.items={"Stock":{},"MF":{}}
        self.log=[]
    def addCash(self,cash):
        self.cash+=cash

    def subCash(self,cash):
        #MAKE SURE NO OVER DRAFT
        self.cash-=cash

    def buyStock(self,quantity,stock):
        if type(quantity)!=int:
            return "Error Stocks Can Only Be Purchased As Whole Units"
        if self.cash<quantity*stock.value:
            return "Error Not Enough Funds"
        if stock.symbol in self.items["Stock"]:
            self.items["Stock"][stock.symbol]+=1
        else: self.items["Stock"][stock.symbol]=1
        self.cash-=quantity*stock.value
        self.log.append("Bought %s for %d"%(stock.symbol,stock.value))

    def sellStock(self,quantity,stock):
        if type(quantity)!=int:
            return "Error Stocks Can Only Be Purchased As Whole Units"
        if stock.symbol not in self.items["Stock"]:
            return "You Don't Own Any %s Stock"%stock.symbol
        if quantity > self.items["Stock"][stock.symbol]:
            return "You only own %d of %s"%(self.items["Stock"][stock.symbol],stock.symbol)
        self.items["Stock"][stock.symbol]-=1
        sellValue=quantity*stock.sell
        self.cash+=sellValue
        self.log.append("Sold %s for %d"%(stock.symbol,sellValue))


class Financialitem():
    def __init__(self,value, symbol):
        self.value=value
        self.symbol=symbol
    def sell(self):
        return self.value


class Stock(Financialitem):
    def sell(self):
        return random.uniform(0.5*self.value,1.5*self.value)

class MF(Financialitem):
    def __init__(self,symbol):
        self.value=1
        self.symbol=symbol
    def sell(self):
        return random.uniform(0.9-1.2)

portfollio = Portfollio()
portfollio.addCash(300.50)
s = Stock(20,"HFH")
portfollio.buyStock(5,s)
portfollio.log
