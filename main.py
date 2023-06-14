class BankAccount:
    def __init__(self, account_number, balance, owner, account_type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете")


class Client:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.bank_accounts = []

    def add_bank_account(self, account):
        self.bank_accounts.append(account)


class Bank:
    def __init__(self):
        self.clients = []
        self.bank_accounts = []

    def add_client(self, client):
        self.clients.append(client)

    def create_bank_account(self, account_number, balance, owner, account_type):
        account = BankAccount(account_number, balance, owner, account_type)
        self.bank_accounts.append(account)
        owner.add_bank_account(account)


# Создание объектов классов
bank = Bank()
client1 = Client("Иван", "Иванов", "ул. Пушкина, д. 10")
client2 = Client("Петр", "Петров", "ул. Ленина, д. 5")
bank_account1 = BankAccount("1234567890", 10000, client1, "дебетовый")
bank_account2 = BankAccount("0987654321", 50000, client2, "кредитный")

# Добавление клиентов и банковских счетов
bank.add_client(client1)
bank.add_client(client2)
bank.create_bank_account("1111111111", 20000, client1, "депозитный")
bank.create_bank_account("2222222222", 100000, client2, "дебетовый")

# Пополнение и списание со счетов
bank_account1.deposit(5000)
bank_account2.withdraw(20000)

# Вывод информации о банковских счетах
for account in bank.bank_accounts:
    print("Номер счета:", account.account_number)
    print("Баланс:", account.balance)
    print("Владелец:", account.owner.first_name, account.owner.last_name)
    print("Тип счета:", account.account_type)
    print()