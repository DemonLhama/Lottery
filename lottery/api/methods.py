from lottery.db.models import UserTable

def user_not_exists(data):
    user = not UserTable.find_user(data.get("email"))
    return user