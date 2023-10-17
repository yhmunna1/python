class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_count = 0

    def generate_account_number(self):
        return hash(self.email)

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited ${amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Withdrawal amount exceeded'
        self.balance -= amount
        self.transaction_history.append(f'Withdrew ${amount}')

    def check_balance(self):
        return f'Available balance: ${self.balance}'

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            self.transaction_history.append(f'Loan of ${amount} taken')

    def transfer(self, account_number, amount, bank):
        if amount > self.balance:
            return 'You have not enough balance'

        target_user = None
        for user in bank.user_accounts:
            if user.account_number == account_number:
                target_user = user
                break

        if target_user is None:
                return 'Account does not exist'

        self.balance -= amount
        target_user.deposit(amount)
        self.transaction_history.append(f'Transferred ${amount} to Account number {account_number}')
            
        return f'Transferred ${amount} to Account number {account_number}'


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.bank.user_accounts.append(user)
        return user

    def delete_user(self, account_number):
        user_to_delete = None
        for user in self.bank.user_accounts:
            if user.account_number == account_number:
                user_to_delete = user
                break

        if user_to_delete:
            self.bank.user_accounts.remove(user_to_delete)
            print(f"User with account number {account_number} has been deleted.")
        else:
            print(f"User with account number {account_number} not found.")

    def view_user_accounts(self):
        for user in self.bank.user_accounts:
            print(f'Account Number: {user.account_number}, Name: {user.name}, Type: {user.balance}')

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.user_accounts)
        return f'Total bank balance: ${total_balance}'

    def check_total_loan(self):
        total_loan = sum(user.balance for user in self.bank.user_accounts if user.loan_count > 0)
        return f'Total loan amount: ${total_loan}'

    def toggle_loan_feature(self, enable):
        self.bank.loan_enabled = enable


class Bank:
    def __init__(self):
        self.user_accounts = []
        self.loan_enabled = True



bank = Bank()
admin = Admin(bank)

# ================================================================================================

while True:
    print('=====Welcome to Banking Management=====')
    print('1. Create an User account')
    print('2. Admin account')
    print('3. No need account, aktu ACr batash khaite ashlam')
    print('4. Exit')

    welcome = int(input())

    if welcome == 1:
        name = input('Your name: ')
        email = input('Your email: ')
        address = input('Your address: ')
        account_type = input('Enter your account type (Savings/Current): ')
        user = admin.create_account(name, email, address, account_type)

        while True:
            print('1. Deposit Amount')
            print('2. Withdraw Amount')
            print('3. Check Balance')
            print('4. Transaction History')
            print('5. Loan Needed')
            print('6. Transfer Money')
            print('99. Back')

            action = int(input())
            if action == 1:
                amount = float(input('Enter the deposit amount: '))
                user.deposit(amount)
                print(f'Deposited ${amount}. {user.check_balance()}')
            elif action == 2:
                amount = float(input('Enter the withdraw amount: '))
                result = user.withdraw(amount)
                if result == 'Withdrawal amount exceeded':
                    print(result)
                else:
                    print(f'Withdrew ${amount}. {user.check_balance()}')
            elif action == 3:
                print(user.check_balance())

            elif action == 4:
                print('Transaction History:')
                for transaction in user.transaction_history:
                    print(transaction)

            elif action == 5:
                amount = float(input('Enter the Loan amount: '))
                result = user.take_loan(amount)
                print(user.check_balance())
                
            elif action == 6:
                amount = float(input('Enter the Transfer amount: '))
                account_number = int(input('Enter the Account Number: '))
                result = user.transfer(account_number, amount, bank)
                print(result)


            elif action == 99:
                break

            else:
                print('Wrong input!')



    elif welcome == 2:
        print('Welcome to Admin panel')
        print('Enter Admin Password')
        password = int(input())
        if password == 123:
            while True:
                print('1. Create an account')
                print('2. Delete any user account')
                print('3. All users accounts list')
                print('4. Total available balance of the bank')
                print('5. Total loan amount')
                print('6. Turn OFF the loan feature')
                print('7. Turn ON the loan feature')
                print('99. Back')

                action = int(input())
                if action == 1:
                    name = input('Your name: ')
                    email = input('Your email: ')
                    address = input('Your address: ')
                    account_type = input('Enter your account type (Savings/Current): ')
                    user = admin.create_account(name, email, address, account_type)
                    admin.view_user_accounts()

                elif action == 2:
                    account_number = int(input('Enter the Account Number: '))
                    admin.delete_user(account_number)

                elif action == 3:
                    admin.view_user_accounts()

                elif action == 4:
                    print(admin.check_total_balance())

                elif action == 5:
                    print(admin.check_total_loan())

                elif action == 6:
                    admin.toggle_loan_feature(False)
                
                elif action == 7:
                    admin.toggle_loan_feature(True)


                elif action == 99:
                    break

                else:
                    print('Wrong input!')


        else:
            print('Wrong Password')
        


    elif welcome == 3:
        print('Sathe ki aktu Coke dibo?')
    elif welcome == 4:
        break
    else:
        print('Wrong input!')