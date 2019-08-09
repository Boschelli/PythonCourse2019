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
        # Truncates cash amount to avoind rounding exploit
        self.cash+=int(cash*100)/100.0
        # Temp string to announce deposit
        temp="Added $%.2f To Account"%cash
        print(temp)
        # Adds deposit to account log
        self.log.append(temp)

    def withdrawCash(self,cash):
        # Temporary variable to calculate cash delta
        # Cash is rounded to nearest whole cent
        tempAmount=self.cash-round(cash,2)
        # Checks if account has sufficent funds for withdraw
        if tempAmount <0:
            exit("Error Insufficent Funds")
        # Sets cash amount to withdrawn amount
        self.cash= tempAmount
        # Temp string to announce withdrawl
        temp="Withdrew $%.2f From Account"%cash
        print(temp)
        # Adds withdraw to account log
        self.log.append(temp)


    ## Default item buy/sell methods: ##

    def defaultBuy(self,quantity,item,itemType):
        # Checks if quantity is appropriate for item type
        item.quanityCheck(quantity)
        # Checks if account has enough funds
        if self.cash<quantity*item.value:
            exit("Error Not Enough Funds")
        # Checks if item already exists in account dictionary and adjusts number
        if item.symbol in self.items[itemType]:
            self.items[itemType][item.symbol]+=quantity
        # Creates item in account dictionary
        else: self.items[itemType][item.symbol]=quantity
        # Subtracts cost of purchase
        self.cash-=quantity*item.value
        # Temp string to announce sale
        temp="Bought %s Shares Of %s For $%.2f"%(str(quantity),item.symbol,item.value*quantity)
        print(temp)
        # Adds purchase to account log
        self.log.append(temp)

    def defaultSell(self,quantity,item,itemType):
        # Checks if quantity is appropriate for item type
        item.quanityCheck(quantity)
        # Checks if account owns the item
        if item.symbol not in self.items[itemType]:
            exit("You Don't Own Any Shares Of %s"%item.symbol)
        # Checks if the account owns enough of the item
        if quantity > self.items[itemType][item.symbol]:
            exit("You only own %s Shares Of %s"%(str(self.items[itemType][item.symbol]),item.symbol))
        # Adjusts items quantity in account dictionary
        self.items[itemType][item.symbol]-=quantity
        # If item amount is zero removes from account dictionary
        if self.items[itemType][item.symbol] == 0:
            del self.items[itemType][item.symbol]
        # Grabs item's sell value
        sellValue=quantity*item.sell()
        # Adds profits from sale
        self.cash+=sellValue
        # Temp string to announce sale
        temp="Sold %s Shares Of %s For $%.2f"%(str(quantity),item.symbol,sellValue)
        print(temp)
        # Adds sale to account log
        self.log.append(temp)


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
        results=("Account Summary:\n Cash: $%.2f\n"%self.cash)
        for itemType in self.items:
            results+=(" %s: \n"%itemType)
            for item in self.items[itemType]:
                results+=("\t%s %s\n"%(str(self.items[itemType][item]),item))
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

## Function Tests  ##

# Creation
portfollio = Portfollio()

# Add/Remove Cash
portfollio.addCash(300.50)
portfollio.withdrawCash(67.45)

# Stock Creation
s_HFH =Stock(20.56,"HFH")
s_FOX=Stock(60.45,"FOX")

# Stock Buy/Sell
portfollio.buyStock(5,s_HFH)
portfollio.buyStock(1,s_FOX)
portfollio.sellStock(1,s_HFH)


# MutualFund Creation
mf_BRT = MutualFund("BRT")
mf_GHT = MutualFund("GHT")

# MutualFund Buy/Sell
portfollio.buyMutualFund(1000.75,mf_BRT)
portfollio.buyMutualFund(2,mf_GHT)
portfollio.sellMutualFund(7,mf_BRT)
portfollio.sellMutualFund(1,mf_GHT)

portfollio.items
# Printing Portfollio
print(portfollio)

# Portfollio History
portfollio.history()
