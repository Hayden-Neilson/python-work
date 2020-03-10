main_menu = {
'1': 'Check Balance',
'2': 'Withdrawal Cash',
'3': 'Deposit Cash',
'4': 'Go back to the main menu',
'5': 'Exit the Program'
}

class Wallet:
    def __init__(self, balance):
        self.balance = 100

    def deposit(self):
        amount = float(input("Enter amout to Deposit:") )
        self.balance + 1000
        print("\n Amount Deposited:", 1000)
        
    new_balance = self.balance + amout

    print(new_balance)


    def user_withdrawal(self,amount):
        self.balance -= amountt
        return self.balance 
    print(self.balance)



user_one = Wallet(150)
user_two = Wallet(2000)


def check_pin(pin):
    if pin == '5685':
        return True
    else: 
        return False

# def user_log_in():
#     tries = 0 
#     while tries < 3:
#         pin = input('Please enter your pin')
#         if check_pin(pin):
#             print('Please wait for Main Menu')
#         else:
#             print('incorrect pin')
#             tries -= 2 
#             print('enter again')
#             tries -= 1
#             print('last try')
#             return('Remove card')
# print('Failure')


