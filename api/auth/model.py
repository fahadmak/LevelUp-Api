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
accounts = [account1, account2]
logged_in_accounts = []
deleted_accounts = []