from intents.base_intent import BaseIntent

class ExitApplication(BaseIntent):
    def handle(self, user_input):
        print("Exiting the application. Thank you!")
        exit()