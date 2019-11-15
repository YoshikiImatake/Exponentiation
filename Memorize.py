import os
from msvcrt import getch

def memorize():
    """
    問題の前に表示して２のべき乗を覚えさせる
    """
    input("これから、２のべき乗を暗記してもらいます。\n")
    input("１行ずつ２のべき乗が表示されていくので、覚えたらEnterを押すと次に進みます。\n")
    powers = powers_of_two()
    for k in powers.keys():
        text = "2^" + str(k) + " = " + str(powers[k]) + "\n"
        input(text)
    input("全部覚えましたか？\n準備が出来たらEnterを押すとメニューに戻ります。\n")
    os.system('cls')



def powers_of_two():
    powers = dict()
    for i in range(11):
        powers[i] = 2**i
    return powers
