class Users:
    def __init__(self):
        self.users = {}

    def add_user(self,users):
        self.users = users

    def is_valid_user(self, id, pw):
        db_pw = self.users.get(id, None)
        if db_pw:
            return pw == db_pw
        else:
            return False


db_users = Users()
db_users.add_user({'test':'jwt-test'})
