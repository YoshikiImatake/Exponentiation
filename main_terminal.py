import Memorize, Question, os

print("こんにちは２のべき乗暗記ドリルです\n")
while True:
    MemoDrill = input("すぐ問題を始めるなら1を、まだ暗記が終わっていないなら2を入力してください\n")

    if MemoDrill == "1":
        input("それでは問題を始めます。\n")
        numlist = Question.question(range(0,11,1))
        revlist = Question.give(numlist)
        text = "11問中" + str(11-len(revlist)) + "問正解です\n"
        input(text)
        if len(revlist) != 0:
            input("復習問題を開始します\n")
            input("Enterを押すと解答が消えて復習問題が始まります\n今のうちに答えをおぼえましょう\n")
            os.system('cls')
            numlist2 = Question.question(revlist)
            correct_answer = Question.give(numlist2)
            if len(correct_answer) == 0:
                print("全問正解！復習完了です")
            else:
                print("まだまだ復習が必要ですね")
        break
    else:
        Memorize.memorize()