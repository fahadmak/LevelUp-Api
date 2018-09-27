class Account:
    def __init__(self, account_id, name, username, password):
        self.account_id = account_id
        self.name = name
        self.username = username
        self.password = password
        self.finished = False
        self.active = False

    def __str__(self):
        return "{self.username} of ID {self.account_id} account has been successfully created".format(self=self)