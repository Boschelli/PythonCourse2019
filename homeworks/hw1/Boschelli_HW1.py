import random



class Portfollio():
    def __init__(self, cash=0):
        self.cash=cash
        self.items={"Stock":{},"MutualFund":{}}
        self.log=[]

    def addCash(self,cash):
        self.cash+=cash
        self.log.append("Added $%d To Account"%cash)

    def withdrawCash(self,cash):
        tempAmount=self.cash-cash
        if tempAmount <0:
            return "Error Insufficent Funds"
        self.cash-=cash
        self.log.append("Withdrew $%d From Account"%cash)


    def buyStock(self,quantity,stock):
        if type(quantity)!=int or quantity<=0:
            return "Error Stocks Can Only Be Purchased As Whole Units Greater Than Or Equal To One"
        if self.cash<quantity*stock.value:
            return "Error Not Enough Funds"
        if stock.symbol in self.items["Stock"]:
            self.items["Stock"][stock.symbol]+=quantity
        else: self.items["Stock"][stock.symbol]=quantity
        self.cash-=quantity*stock.value
        self.log.append("Bought %d Shares Of %s For %d"%(quantity,stock.symbol,stock.value*quantity))

    def sellStock(self,quantity,stock):
        if type(quantity)!=int or quantity<=0:
            return "Error Stocks Can Only Be Sold In Whole Units Greater Than Or Equal To One"
        if stock.symbol not in self.items["Stock"]:
            return "You Don't Own Any %s Stock"%stock.symbol
        if quantity > self.items["Stock"][stock.symbol]:
            return "You only own %d of %s"%(self.items["Stock"][stock.symbol],stock.symbol)
        self.items["Stock"][stock.symbol]-=quantity
        sellValue=quantity*stock.sell()
        self.cash+=sellValue
        self.log.append("Sold %d Shares Of %s For %d"%(quantity,stock.symbol,sellValue))


    def buyMutualFund(self,quantity,mf):
        if quantity<=0:
            return "Please Enter A Positive Non-Zero Amount"
        if self.cash<quantity*mf.value:
            return "Error Not Enough Funds"
        if mf.symbol in self.items["MutualFund"]:
            self.items["MutualFund"][mf.symbol]+=quantity
        else: self.items["MutualFund"][mf.symbol]=quantity
        self.cash-=quantity*mf.value
        self.log.append("Bought %d Shares Of %s For %d"%(quantity,mf.symbol,mf.value*quantity))

    def sellMutualFund(self,quantity,mf):
        if type(quantity)!=int or quantity<=0:
            return "Please Enter A Positive Non-Zero Amount"
        if mf.symbol not in self.items["MutualFund"]:
            return "You Don't Own Any Shares Of %s"%mf.symbol
        if quantity > self.items["MutualFund"][mf.symbol]:
            return "You only own %d of %s"%(self.items["MutualFund"][mf.symbol],mf.symbol)
        self.items["MutualFund"][mf.symbol]-=quantity
        sellValue=quantity*mf.sell()
        self.cash+=sellValue
        self.log.append("Sold %d Shares Of %s For %d"%(quantity,mf.symbol,sellValue))

    def __str__(self):
        results=("Account Summary:\n Cash: $%d\n"%self.cash)
        results+=(" Stocks: \n")
        for stocks in self.items['Stock']:
            results+=("\t%d %s\n"%(self.items['Stock'][stocks],stocks))
        results+=(" MutualFunds: \n")
        for mf in self.items['MutualFund']:
            results+=("\t%d %s\n"%(self.items['MutualFund'][mf],mf))
        return results

    def history(self):
        for i in self.log:
            print(i)

class Financialitem():
    def __init__(self,value, symbol):
        self.value=value
        self.symbol=symbol
    def sell(self):
        return self.value

class Stock(Financialitem):
    def sell(self):
        return random.uniform((0.5*self.value),(1.5*self.value))

class MutualFund(Financialitem):
    def __init__(self,symbol):
        Financialitem.__init__(self,1,symbol)
    def sell(self):
        return random.uniform(0.9,1.2)

portfollio = Portfollio()
portfollio.addCash(300000.50)
portfollio.withdrawCash(4567)

mf1=MutualFund("BRT")
mf2=MutualFund("EUP")
mf3=MutualFund("FVG")
s1 = Stock(20,"HFH")
s2 = Stock(54,"DCF")
s3 = Stock(43,"EEE")
s4 = Stock(20,"MMM")

portfollio.buyStock(10,s1)
portfollio.buyStock(10,s2)
portfollio.buyStock(10,s3)
portfollio.buyStock(10,s4)

portfollio.buyMutualFund(100.5,mf1)
portfollio.buyMutualFund(56.89,mf2)
portfollio.buyMutualFund(43.67,mf3)



portfollio.sellStock(5,s2)
portfollio.sellMutualFund(10,mf1)
print(portfollio)
portfollio.history()
