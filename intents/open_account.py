from intents.base_intent import BaseIntent

class OpenAccountIntent(BaseIntent):
    def handle(self, user_input):
        account_type = input("What type of savings account are you interested in? (e.g., regular, high-yield)\n").strip()
        print(f"Opening a {account_type} savings account for you.")