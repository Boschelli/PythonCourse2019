import random
from sys import exit

class Portfollio():
    def __init__(self, cash=0):
        # Initial cash for account
        self.cash=cash
        # Creates empty dictionary with item types
        self.items={"Stock":{},"MutualFund":{}}
        # Creates empty list to contain transactions
        self.log=[]

    ## Add/Withdraw Methods For Cash: ##

    def addCash(self,cash):
        # Adds new cash amount to account total
        self.cash+=cash
        # Adds deposit to account log
        self.log.append("Added $%d To Account"%cash)

    def withdrawCash(self,cash):
        # Temporary variable to calculate cash delta
        tempAmount=self.cash-cash
        # Checks if account has sufficent funds for withdraw
        if tempAmount <0:
            return "Error Insufficent Funds"
        # Sets cash amount to withdrawn amount
        self.cash= tempAmount
        # Adds withdraw to account log
        self.log.append("Withdrew $%d From Account"%cash)


    ## Default item buy/sell methods: ##

    def defaultBuy(self,quantity,item,itemType):
        # Checks if quantity is appropriate for item type
        item.quanityCheck(quantity)
        # Checks if account has enough funds
        if self.cash<quantity*item.value:
            return "Error Not Enough Funds"
        # Checks if item already exists in account dictionary and adjusts number
        if item.symbol in self.items[itemType]:
            self.items[itemType][item.symbol]+=quantity
        # Creates item in account dictionary
        else: self.items[itemType][item.symbol]=quantity
        # Subtracts cost of purchase
        self.cash-=quantity*item.value
        # Adds purchase to account log
        self.log.append("Bought %d Shares Of %s For %d"%(quantity,item.symbol,item.value*quantity))

    def defaultSell(self,quantity,item,itemType):
        # Checks if quantity is appropriate for item type
        item.quanityCheck(quantity)
        # Checks if account owns the item
        if item.symbol not in self.items[itemType]:
            return "You Don't Own Any Shares Of %s"%item.symbol
        # Checks if the account owns enough of the item
        if quantity > self.items[itemType][item.symbol]:
            return "You only own %d Shares Of %s"%(self.items[itemType][item.symbol],item.symbol)
        # Adjusts items quantity in account dictionary
        self.items[itemType][item.symbol]-=quantity
        # If item amount is zero removes from account dictionary
        if self.items[itemType][item.symbol] == 0:
            del self.items[itemType][item.symbol]
        # Grabs item's sell value
        sellValue=quantity*item.sell()
        # Adds profits from sale
        self.cash+=sellValue
        # Adds sale to account log
        self.log.append("Sold %d Shares Of %s For %d"%(quantity,item.symbol,sellValue))


    ## Buy/Sell methods for Stocks: ##

    def buyStock(self,quantity,stock):
        self.defaultBuy(quantity,stock,"Stock")

    def sellStock(self,quantity,stock):
        self.defaultSell(quantity,stock,"Stock")

    ## Buy/Sell methods for Mutual Funds ##

    def buyMutualFund(self,quantity,mf):
        self.defaultBuy(quantity,mf,"MutualFund")

    def sellMutualFund(self,quantity,mf):
        self.defaultSell(quantity,mf,"MutualFund")

    ## Formatted Class String: ##

    def __str__(self):
        results=("Account Summary:\n Cash: $%d\n"%self.cash)
        for itemType in self.items:
            results+=(" %s: \n"%itemType)
            for item in self.items[itemType]:
                results+=("\t%d %s\n"%(self.items[itemType][item],item))
        return results


    ## Account Log Printer: ##

    def history(self):
        for i in self.log:
            print(i)

class Financialitem():
    def __init__(self,value, symbol):
        self.value=value
        self.symbol=symbol
    # Default sell value
    def sell(self):
        return self.value
    # Defualt quantity check
    def quanityCheck(self,quantity):
        if quantity <=0:
            exit("Please Enter A Postive Non-Zero Amount")

class Stock(Financialitem):
    def sell(self):
        return random.uniform((0.5*self.value),(1.5*self.value))
    def quanityCheck(self,quantity):
        if quantity<=0 or type(quantity) != int:
            exit("Error Stocks Must Be In Integer Units Greater Than Or Equal To One")

class MutualFund(Financialitem):
    def __init__(self,symbol):
        Financialitem.__init__(self,1,symbol)
    def sell(self):
        return random.uniform(0.9,1.2)

portfollio = Portfollio()
portfollio.addCash(300.50)
s =Stock(20,"HFH")
portfollio.buyStock(5,s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfollio.buyMutualFund(10.3,mf1)
portfollio.buyMutualFund(2,mf2)
print(portfollio)
portfollio.sellMutualFund(3,mf1)
portfollio.sellStock(1,s)
portfollio.history()
