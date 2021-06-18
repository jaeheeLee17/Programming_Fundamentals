class BankAccount:
    """
    Client's bank account information
    name : Bank account owner's name
    balance : bank balance, unit : won(integer), balance should be equal or more than 0
    """
    __no_of_accounts = 0
    def __init__(self, name, balance=0):
        self.__name = name
        if balance < 0:
            self.__balance = 0
        else:
            self.__balance = balance
        print("A bank account for {} is open.".format(self.__name))
        print("Your current balance is {} won.".format(self.__balance))
        BankAccount.__no_of_accounts += 1

    def __str__(self):
        """returns its string representation"""
        return self.__name + "'s BankAccount object"

    def show_balance(self):
        """print own balance in the terminal"""
        print("{}'s balance is {} won.".format(self.__name, self.__balance))

    def deposit(self, amount):
        """
        Deposit the amount into your bank account (amount should be integer)
        amount >= 0: Increase your balance by the amount
        amount < 0: Impossible to deposit into your bank account
        """
        if amount >= 0:
            self.__balance += amount
            print("{} won has been successfully deposited.".format(amount))
        else:
            print("Deposit failed")
        self.show_balance()

    def withdraw(self, amount):
        """
        Withdraw the amount from your bank account (amount should be integer)
        0 <= amount <= balance: Decrease your balance by the amount
        Otherwise: Impossible to withdraw from your bank account
        """
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            print("{} won has been successfully withdrawn.".format(amount))
        else:
            print("Withdraw failed")
        self.show_balance()

    @property
    def name(self):
        """returns bank account owner's name"""
        return self.__name

    @property
    def balance(self):
        """returns bank account owner's balance"""
        return self.__balance

    @staticmethod
    def count_accounts():
        """returns the number of bank accounts"""
        return BankAccount.__no_of_accounts
