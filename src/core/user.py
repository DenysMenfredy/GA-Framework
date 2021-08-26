
class User:
    """
    User class
    """

    def __init__(self, user_name:str, password:str, email:str, name:str, notification_email:str):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.name = name
        self.notification_email = notification_email