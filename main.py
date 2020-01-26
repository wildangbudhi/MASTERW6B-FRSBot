from FRSBot import FRSBot, load, Process, Event, sleep

def main():
    print("----------Welcom to MASTERW6B-FRSBot---------")
    sel = input("do you want to prev your error [y/n] : ")

    if(sel == 'y' or sel == 'Y'): err = True
    elif(sel == 'n' or sel == 'N'): err = False

    program = []
    programProcess = []
    e = Event()
    for i in load(open('user.json')): program.append(FRSBot(i, ErroPrev=err))
    for i in program: programProcess.append(Process(target=i.run, args=(e, )))
    for i in programProcess: i.start()

    sleep(2)

    while(True):
        is_start = input('Start Now [Y] ? ')
        if(is_start in ["Y", "y"]): 
            e.set()
            break

    for i in programProcess: i.join()

if __name__ == "__main__":
    main()
