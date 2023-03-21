print("                                                     ANAGRAMS ")
print("                                             HOW TO PLAY ANAGRAMS ?! ")
print("                                              IT IS A TWO PLAYER GAME")
print("                                     THE PLAYERS CAN CHOOSE THE DIFFICULTY LEVEL ")
print("                                                 EASY/MEDIUM/HARD")
print("       EACH PLAYERS WILL BE PROVIDED SIX DISTINCT LETTERS AND THEY HAVE TO FORMULATE MEANINGFUL WORDS USING THE GIVEN LETTERS")
print("                                  FOR A THREE LETTER WORD, 100 POINTS WILL BE AWARDED")
print("                                  FOR A FOUR LETTER WORD, 200 POINTS WILL BE AWARDED")
print("                                  FOR A FIVE LETTER WORD, 400 POINTS WILL BE AWARDED")
print("                                  FOR A six LETTER WORD, 1200 POINTS WILL BE AWARDED")
print("                                     THE PLAYER WITH THE HIGHEST SCORE POINTS WINS")
print("                                                   GOOD LUCK!!!")



cho=input("ENTER UR OPTION: ")
print("")
if cho=='easy':
    print("yes")    
elif cho=='EASY':
    print("yes1")    
elif cho=='medium': 
    print("yes2")
elif cho=='MEDIUM':
    print("yes3")
elif cho=='HARD':
    l1 = ['amp', 'map', 'pam', 'ape', 'arm', 'eme', 'mae', 'mar', 'mea', 'mer', 'par', 'pea', 'pee', 'per', 'pre',
          'ram', 'rap', 'rem', 'rep', 'are', 'AMP', 'MAP', 'PAM', 'APE', 'ARM', 'EME', 'MAE', 'MER', 'PAR', 'PEA',
          'PEE', 'PER', 'PRE', 'RAM', 'RAP', 'REM', 'REP', 'ARE']
    l2 = ['meep', 'perm', 'pram', 'ramp', 'aper', 'mare', 'mere', 'pare', 'pear', 'peer', 'pere', 'pree', 'rape',
          'ream', 'reap', 'MEEP', 'PERM', 'PRAM', 'RAMP', 'APER', 'MARE', 'MERE', 'PARE', 'PEAR', 'PEER', 'PERE',
          'PREE', 'RAPE', 'REAM', 'REAP']
    l3 = ['remap', 'ameer', 'perea', 'ramee', 'REMAP', 'AMEER', 'PEREA', 'RAMEE']
    l4 = ['ampere', 'AMPERE']
    print("                                              PLAYER 1")
    print("                                             P/R/M/A/E/E")
    sum1 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(4):
        val1 = str(input("enter ur word: "))
        if val1 in l1:
            sum1 += 100
            print("your score is: %d" % sum1)
            l1.remove(val1)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum1)
    print("")
    print("                                             P/R/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(4):
        val2 = str(input("enter ur word: "))
        if val2 in l2:
            sum2 += 200
            print("your score is: %d" % sum2)
            l2.remove(val2)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum2)
    print("")
    print("                                             P/R/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum3 = 0
    for i in range(2):
        val3 = str(input("enter ur word: "))
        if val3 in l3:
            sum3 += 400
            print("your score is: %d" % sum3)
            l3.remove(val3)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum3)
    print("")
    print("SIX LETTER WORDS ONLY!")
    sum4 = 0
    for i in range(1):
        val4 = str(input("enter ur word: "))
        if val4 in l4:
            sum4 += 400
            print("your score is: %d" % sum4)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum4)
    sum = sum3 + sum1 + sum2 + sum4

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum)
    print(" ")
    print("                                              PLAYER 2")
    print("                                             B/N/M/A/E/E")
    sum5 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(4):
        val5 = str(input("enter ur word: "))
        if val5 in l1:
            sum5 += 100
            print("your score is: %d" % sum5)
            l1.remove(val5)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum5)
    print("")
    print("                                             B/N/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum6 = 0
    for i in range(3):
        val6 = str(input("enter ur word: "))
        if val6 in l2:
            sum6 += 200
            print("your score is: %d" % sum6)
            l2.remove(val6)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum6)
    print("")
    print("                                             B/N/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum7 = 0
    for i in range(2):
        val7 = str(input("enter ur word: "))
        if val7 in l3:
            sum7 += 400
            print("your score is: %d" % sum7)
            l3.remove(val7)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum7)
    print("")
    print("SIX WORDS ONLY!")
    sum8 = 0
    for i in range(1):
        val8 = str(input("enter ur word: "))
        if val8 in l4:
            sum8 += 1200
            print("your score is: %d" % sum8)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum8)
    sum9 = sum5 + sum6 + sum7 + sum8

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum9)
else:
    l1 = ['amp', 'map', 'pam', 'ape', 'arm', 'eme', 'mae', 'mar', 'mea', 'mer', 'par', 'pea', 'pee', 'per', 'pre',
          'ram', 'rap', 'rem', 'rep', 'are', 'AMP', 'MAP', 'PAM', 'APE', 'ARM', 'EME', 'MAE', 'MER', 'PAR', 'PEA',
          'PEE', 'PER', 'PRE', 'RAM', 'RAP', 'REM', 'REP', 'ARE']
    l2 = ['meep', 'perm', 'pram', 'ramp', 'aper', 'mare', 'mere', 'pare', 'pear', 'peer', 'pere', 'pree', 'rape',
          'ream', 'reap', 'MEEP', 'PERM', 'PRAM', 'RAMP', 'APER', 'MARE', 'MERE', 'PARE', 'PEAR', 'PEER', 'PERE',
          'PREE', 'RAPE', 'REAM', 'REAP']
    l3 = ['remap', 'ameer', 'perea', 'ramee', 'REMAP', 'AMEER', 'PEREA', 'RAMEE']
    l4 = ['ampere', 'AMPERE']
    print("                                              PLAYER 1")
    print("                                             P/R/M/A/E/E")
    sum1 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(4):
        val1 = str(input("enter ur word: "))
        if val1 in l1:
            sum1 += 100
            print("your score is: %d" % sum1)
            l1.remove(val1)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum1)
    print("")
    print("                                             P/R/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(4):
        val2 = str(input("enter ur word: "))
        if val2 in l2:
            sum2 += 200
            print("your score is: %d" % sum2)
            l2.remove(val2)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum2)
    print("")
    print("                                             P/R/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum3 = 0
    for i in range(2):
        val3 = str(input("enter ur word: "))
        if val3 in l3:
            sum3 += 400
            print("your score is: %d" % sum3)
            l3.remove(val3)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum3)
    print("")
    print("SIX LETTER WORDS ONLY!")
    sum4 = 0
    for i in range(1):
        val4 = str(input("enter ur word: "))
        if val4 in l4:
            sum4 += 400
            print("your score is: %d" % sum4)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum4)
    sum = sum3 + sum1 + sum2 + sum4

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum)
    print(" ")
    print("                                              PLAYER 2")
    print("                                             B/N/M/A/E/E")
    sum5 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(4):
        val5 = str(input("enter ur word: "))
        if val5 in l1:
            sum5 += 100
            print("your score is: %d" % sum5)
            l1.remove(val5)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum5)
    print("")
    print("                                             B/N/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum6 = 0
    for i in range(3):
        val6 = str(input("enter ur word: "))
        if val6 in l2:
            sum6 += 200
            print("your score is: %d" % sum6)
            l2.remove(val6)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum6)
    print("")
    print("                                             B/N/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum7 = 0
    for i in range(2):
        val7 = str(input("enter ur word: "))
        if val7 in l3:
            sum7 += 400
            print("your score is: %d" % sum7)
            l3.remove(val7)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum7)
    print("")
    print("SIX WORDS ONLY!")
    sum8 = 0
    for i in range(1):
        val8 = str(input("enter ur word: "))
        if val8 in l4:
            sum8 += 1200
            print("your score is: %d" % sum8)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum8)
    sum9 = sum5 + sum6 + sum7 + sum8

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum9)
