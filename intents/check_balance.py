from intents.base_intent import BaseIntent

class CheckBalanceIntent(BaseIntent):
    def handle(self, user_input):
        account_number = input("Please provide your account number:\n").strip()
        print(f"Fetching the balance for account {account_number}.")