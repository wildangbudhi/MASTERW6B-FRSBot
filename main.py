from FRSBot import FRSBot, json, Thread

def main():
    print("----------Welcom to MASTERW6B-FRSBot---------")
    sel = input("do you want to prev your error [y/n] : ")

    if(sel == 'y' or sel == 'Y'): err = True
    elif(sel == 'n' or sel == 'N'): err = False

    program = []
    programThread = []
    for i in json.load(open('user.json')): program.append(FRSBot(i, ErroPrev=err))
    for i in program: programThread.append(Thread(target=i.run, daemon=True))
    for i in programThread: i.start()
    for i in programThread: i.join()

if __name__ == "__main__":
    main()