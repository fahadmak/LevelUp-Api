from api.auth.model import accounts


def search_account_by_id(accountId):
    if not accounts:
        return None
    for account in accounts:
        if accountId == account.account_id:
            return account
    return None


def search_account_by_username(username):
    if not accounts:
        return None
    for account in accounts:
        if username == account.username:
            return account
    return None

