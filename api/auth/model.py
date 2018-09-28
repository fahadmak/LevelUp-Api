class Account:
    def __init__(self, account_id, name, username, password):
        self.account_id = account_id
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return "{self.username} of ID {self.account_id} account has been successfully created".format(self=self)

    def to_json(self):
        account = {
            'account_id': self.account_id,
            'name': self.name,
            'username': self.username,
            'password': self.password
        }
        return account


account1 = Account(1, 'fahad', 'fahad3', 'pass123')
account2 = Account(2, 'mina', 'minatti', 'pass1233')
account3 = Account(3, 'mina', 'phillip', 'pass12334')
account4 = Account(4, 'mina', 'phillipwere', 'pass12345')
account5 = Account(5, 'mina', 'reality', 'pass12345')
account6 = Account(6, 'minattt', 'Andela', 'pass12345')
accounts = [account1, account2, account3, account4, account5, account6]
logged_in_accounts = []
deleted_accounts = []