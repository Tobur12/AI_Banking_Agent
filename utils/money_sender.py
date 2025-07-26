def send_money(details):
    import main
    import time
    print (f"Amount: {details['amount']}")
    print (f"Recipient: {details['recipient']}")
    print (f"Schedule: {details['schedule']}")
    # Simulate sending money
    time.sleep(2)  # Simulate network delay
    print(f"[MOCK] Sending {details['amount']} to {details['recipient']} ({details['schedule']})")
    time.sleep(2)  # Simulate network delay
    print(f"[MOCK] Money sent successfully to {details['recipient']}!")
    main.main()