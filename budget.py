import budget_chart_data as chart_data

class Category:

    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.balance = 0.00
        self.withdraws = []
        self.deposits = []
        
    def __str__(self):
        #30 is the line char limit
         numberOfStarsPerSide = (30 - len(self.category)) // 2
         stars = "*" * numberOfStarsPerSide
         title = (f"{stars}{self.category}{stars}")
         
         transactions = ""
         total = f"Total: {self.balance}"
         
         for transaction in self.ledger:
             transactionDesc = transaction["description"][0:23]
             transactionAmount = str(transaction["amount"])[0:7]
             numberOfSpaces =  30 - (len(transactionDesc) + len(f"{float(transactionAmount):.2f}"))
                     
             transactions += f'\n{transactionDesc}{" " * numberOfSpaces}{float(transactionAmount):.2f}'

         output = f"{title}{transactions}\n{total}" 
             
         return output

    def deposit(self, depositAmount, description=""):
        self.balance += depositAmount
        self.ledger.append({"amount": depositAmount, "description": description})
    
    def withdraw(self, withdrawAmount, description=""):
        if not self.check_funds(withdrawAmount):
            return False
        else:
            self.balance -= withdrawAmount
            self.withdraws.append(withdrawAmount)
            self.ledger.append({"amount": -abs(withdrawAmount), "description": description})
            return True

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, toCategory):        
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {toCategory.category}")
            toCategory.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else: 
            return False


def create_spend_chart(categories):
    chart = ""
                
    totalWthdrawn = 0
    for category in categories:
        totalWthdrawn += sum(category.withdraws)
    
    chart_data_dict = chart_data.get_chart_data(categories, totalWthdrawn)
              
    #chart label 
    chart += "Percentage spent by category\n"
    
    for key, value in chart_data_dict.items():
        if key == 0:
            chart += f'{key:>2}| {"  ".join(value)}  \n '
        else:
            chart += f'{key}| {"  ".join(value)}  \n '
    
    #chart bottom line
    dashes = "----------\n"
    
    chart += f"{dashes:>14}"
    chart += chart_data.get_spend_chart_labels(categories)
    
    return chart
            

            
        