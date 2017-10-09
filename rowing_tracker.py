times = []
class session:
    def __init__(self, date, distance, time):
        self.date = date
        self.distance = distance
        self.time = time

def greeting():
    print("welcome to my program to track your rowing progress")
    print("if at any time you wish to quit enter 'quit'")
    print("to see a history of your rowing times enter 'history'")
    print("to enter a new time enter 'new'")
    print("if you wish to see this again enter 'rules'")

def history():
    if len(times) > 0:
        for history in times:
            print("on {} your time for {} was {}".format(history.date, history.distance, history.time))
    else:
        print("there are no times saved yet")

def new():
    date = raw_input("date >>  ")
    distance = raw_input("distance >>  ")
    time = raw_input("time >>  ")
    new_session = session(date, distance, time)
    times.append(new_session)
    history()

while True:
    greeting()
    prompt = raw_input(">>  ").lower()
    if prompt == 'quit':
        break
    elif prompt == 'history':
        history()
    elif prompt == 'new':
        new()
    elif prompt == 'rules':
        greeting()
    else:
        print("your answer didn't compute")
