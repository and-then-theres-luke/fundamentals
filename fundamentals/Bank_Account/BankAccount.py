class BankAccount:
    all_accounts_index = []

    def __init__(self, balance=0, interest_rate=.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts_index.append(self)

#deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance+=amount
        print(f'''Current balance is {self.balance}''')
        return self

#withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self
        else:
            self.balance-=amount
            return self

#display_account_info(self) - print to the console: eg. "Balance: $100"

    def display_account_info(self):
        print(f'''Interest Rate: {self.interest_rate}''')
        print(f'''Balance: ${self.balance}''')
        return self

#yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

    def yield_interest(self):
        if self.balance < 0:
            print("Yeilding no interest: account balance negative")
            return self
        else:
            print(f'''Interest has compounded!''')
            print(f'''Current Balance: ${self.balance}''')
            print(f'''Interest applied: {self.interest_rate}% (${round((self.balance*self.interest_rate),2)})''')
            self.balance+= (self.balance*self.interest_rate)
            print(f'''New Balance: {self.balance}''')
            return self
    

    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for item in cls.all_accounts_index:
            item.display_account_info()


luke_account = BankAccount(200,.05)
kelila_account = BankAccount(4000, .09)

luke_account.deposit(100).deposit(1200).deposit(5).withdraw(500).yield_interest().display_account_info()
kelila_account.deposit(5000).deposit(5000).withdraw(40).withdraw(50).withdraw(400).withdraw(500).yield_interest().display_account_info()

BankAccount.print_all_accounts()
