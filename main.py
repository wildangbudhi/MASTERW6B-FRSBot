from FRSBot import FRSBot, load, Process

def main():
    print("----------Welcom to MASTERW6B-FRSBot---------")
    sel = input("do you want to prev your error [y/n] : ")

    if(sel == 'y' or sel == 'Y'): err = True
    elif(sel == 'n' or sel == 'N'): err = False

    program = []
    programProcess = []
    for i in load(open('user.json')): program.append(FRSBot(i, ErroPrev=err))
    for i in program: programProcess.append(Process(target=i.run))
    for i in programProcess: i.start()
    for i in programProcess: i.join()

if __name__ == "__main__":
    main()
