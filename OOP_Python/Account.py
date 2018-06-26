import datetime
import pytz


class Account:
    """ Its good to use docstring to specify the description of the class."""
    """Static Methods:
        #   They are placed before __init__ method
        #   They start with single underscore
        #   It should not contain self as parameter
        #   Annotation '@staticmethod' must be provided
        #   Static methods are non-public.
        #   Static methods can be called using instance reference like self._current_time() instead of using class name, 
            however performance may suffer because the use of self will first search the method in namespace of 
            the instance which can be time consuming on a large scale implementation
        """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, client_name, balance):
        """ NOTE : ANY data member which is not to be used by the instances directly
        should start with single underscore."""
        self._client_name = client_name
        self._transaction_list = list()
        self._transaction_list.append(("AC/OPEN", Account._current_time(), 0, balance))
        self.__balance = balance
        print("Account Created FOR "+client_name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append(("Credited", Account._current_time(), amount, self.__balance))

    def withdraw(self, amount):
        if self.__balance > 0:
            if amount > 0:
                self.__balance -= amount
                self._transaction_list.append(("Debited", Account._current_time(), amount, self.__balance))

    def show_balance(self):
        print("Your current balance is {}".format(self.__balance))

    def view_all_transaction(self):
        print("State\t\t\t\t\tDATE(UTC)\t\t\t\t\t\tDATE/TIME(LOCAL)\t\t\tAmount\t\tBalance")
        print("-"*105)
        for transaction in self._transaction_list:
            state, date, amount, balance = transaction
            print("{0:8}\t{1}\t{2}\t{3:8}\t{4:8}".format(state, date, date.astimezone(), amount, balance))


""" we can see the for date time we ae using functions twice at different locations, so we can make a method that would 
not be included into the instances of the Class. And these methods are known as static method. """
if __name__ == '__main__':

    rohan_account = Account("ROHAN", 100000)
    rohan_account.withdraw(20.78)
    rohan_account.show_balance()
    rohan_account.deposit(188.86)
    rohan_account.show_balance()
    rohan_account.view_all_transaction()

    tim = Account("TIM", 1000)
    tim.withdraw(200)
    tim.show_balance()
    tim.deposit(100)
    tim.show_balance()
    tim.view_all_transaction()
    print(tim.__dict__)
    tim.__balance=200
    print(tim.__dict__)