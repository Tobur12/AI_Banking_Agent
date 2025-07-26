import spacy
from intents.base_intent import BaseIntent
from utils.money_sender import send_money

class TransferMoneyIntent(BaseIntent):
    def __init__(self, nlu):
        super().__init__(nlu)
        self.nlp = spacy.load("en_core_web_trf")

    def extract_recipient(self, text):
        doc = self.nlp(text)
        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        if persons:
            return persons[0]
        
        # Fallback: check for "to Name" pattern
        tokens = text.split()
        if "to" in tokens:
            idx = tokens.index("to")
            if idx + 1 < len(tokens):
                candidate = tokens[idx + 1]
                if candidate.istitle():
                    return candidate
        return None

    def handle(self, user_input):
        transfer_details = {}

        # Interpret full sentence with spaCy
        print("Interpreting your request...")
        doc = self.nlp(user_input)

        # Recipient
        recipient = self.extract_recipient(user_input)
        if recipient:
            transfer_details["recipient"] = recipient

        # Amount
        amounts = [ent.text for ent in doc.ents if ent.label_ == "MONEY"]
        if amounts:
            transfer_details["amount"] = amounts[0]
        else:
            digits = ''.join(filter(str.isdigit, user_input))
            if digits:
                transfer_details["amount"] = digits

        # Schedule
        dates = [ent.text for ent in doc.ents if ent.label_ in ["DATE", "TIME"]]
        if "now" in user_input.lower() or "immediately" in user_input.lower():
            transfer_details["schedule"] = "immediately"
        elif dates:
            transfer_details["schedule"] = f"scheduled for {dates[0]}"

        # Fallback prompts
        while "recipient" not in transfer_details:
            recipient_input = input("Who would you like to send money to?\n")
            transfer_details["recipient"] = self.extract_recipient(recipient_input)

        while "amount" not in transfer_details:
            amount_input = input("How much would you like to send?\n")
            doc = self.nlp(amount_input)
            amounts = [ent.text for ent in doc.ents if ent.label_ == "MONEY"]
            if amounts:
                transfer_details["amount"] = amounts[0]
            else:
                digits = ''.join(filter(str.isdigit, amount_input))
                if digits:
                    transfer_details["amount"] = digits

        while "schedule" not in transfer_details:
            schedule_input = input("When would you like to send the money?\n")
            doc = self.nlp(schedule_input)
            dates = [ent.text for ent in doc.ents if ent.label_ in ["DATE", "TIME"]]
            if "now" in schedule_input.lower() or "immediately" in schedule_input.lower():
                transfer_details["schedule"] = "immediately"
            elif dates:
                transfer_details["schedule"] = f"scheduled for {dates[0]}"

        # Final confirmation
        send_money(transfer_details)