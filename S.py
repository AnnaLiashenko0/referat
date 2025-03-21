Порушується:
class UserManager:
    def create_user(self, username: str, password: str):
        print(f"Creating user {username}"

    def save_user_to_database(self, user):
        print(f"Saving user {user} to database")

    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user}")








 Приклад застосування в Python:
class Order:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

class OrderPrinter:
    def print_order(self, order):
        print(f"Order ID: {order.id}, Amount: {order.amount}")
