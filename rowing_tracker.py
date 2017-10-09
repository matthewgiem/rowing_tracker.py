def greeting():
    print("welcome to my program to track your rowing progress")
    print("if at any time you wish to quit enter 'quit'")
    print("to see a history of your rowing times enter 'history'")
    print("to enter a new time enter 'new'")
    print("if you wish to see this again enter 'rules'")

while True:
    greeting()
    prompt = raw_input(">> ").lower()
    if prompt == 'quit':
        break
    elif prompt == 'history':
        pass
    elif prompt == 'new':
        pass
    elif prompt == 'rules':
        greeting()
    else:
        print("your answer didn't compute")
        # greeting()
