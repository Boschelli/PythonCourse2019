import random



test={"Stock":{"Test":1},"MF":{}}
test["Stock"]["Test"]


class Portfollio():
    def__init__(self, name, cash=0):
        self.name=name
        self.cash=cash
        self.items={"Stock":{},"MF":{}}
        self.log=[]
    def addCash(self,cash):
        self.cash+=cash

    def subCash(self.cash):
        #MAKE SURE NO OVER DRAFT
        self.cash-=cash

    def buyStock(quantity,stock):
        if cash<quantity*stock.value:
            return "Error Not Enough Funds"
        if stock.symbol in self.items["Stock"]:
            self.items["Stock"][stock.symbol]+=1
        else: self.items["Stock"][stock.symbol]=1
        self.log.append("Bought %s for $d"%(stock.symbol,stock.value))



class Financialitem():
    def__init__(self,value, symbol):
        self.value=value
        self.symbol=symbol
    def sell(self):
        return self.value


class Stock(Financialitem):
    def sell(self):
        return random.uniform(0.5*self.value,1.5*self.value)

class MF(Financialitem):
    def__init__(self,value=1,symbol)
        self.value=value
        self.symbol=symbol
    def sell(self):
        return random.uniform(0.9-1.2)
