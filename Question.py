import random
def question(numlist):
    qlist = list()
    while True:
        i = random.randint(0,10)
        if i in numlist and not i in qlist:
            qlist.append(i)
        if len(numlist) == len(qlist):
            break
    return qlist

def give(qlist):
    revlist = list()
    for i in range(len(qlist)):
        text = "(" + str(i+1) + ") " + "2^" + str(qlist[i]) + " = "
        answer = input(text)
        if answer == str(2**qlist[i]):
            print("正解！\n")
        else:
            correction = "不正解: " + "2^" + str(qlist[i]) + " = "  + str(2**qlist[i]) + "\n"
            print(correction)
            revlist.append(qlist[i])
    return revlist




