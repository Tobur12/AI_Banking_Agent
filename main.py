from utils.nlu import NLUModel
from intents.transfer_money import TransferMoneyIntent
from intents.open_account import OpenAccountIntent
from intents.check_balance import CheckBalanceIntent
from intents.exit_application import ExitApplication
from config.labels import INTENT_LABELS

def main():
    nlu = NLUModel()
    user_input = input("Please enter your banking request:\n")
    intent = nlu.classify(user_input, INTENT_LABELS)

    intent_map = {
        "transfer money": TransferMoneyIntent(nlu),
        "open savings account": OpenAccountIntent(nlu),
        "check account balance": CheckBalanceIntent(nlu),
        "exit application": ExitApplication(nlu)
    }

    handler = intent_map.get(intent)
    if handler:
        handler.handle(user_input)
    else:
        print("I'm sorry, I can't handle that request.")

if __name__ == "__main__":
    main()