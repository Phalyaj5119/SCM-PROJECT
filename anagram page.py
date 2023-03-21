print("                                                     ANAGRAMS ")
print("                                             HOW TO PLAY ANAGRAMS ?! ")
print("                                              IT IS A TWO PLAYER GAME")
print("                                     THE PLAYERS CAN CHOOSE THE DIFFICULTY LEVEL ")
print("                                                 EASY/MEDIUM/HARD")
print("       EACH PLAYERS WILL BE PROVIDED FIVE/SIX DISTINCT LETTERS AND THEY HAVE TO FORMULATE MEANINGFUL WORDS USING THE GIVEN LETTERS")
print("                                  FOR A THREE LETTER WORD, 100 POINTS WILL BE AWARDED")
print("                                  FOR A FOUR LETTER WORD, 200 POINTS WILL BE AWARDED")
print("                                  FOR A FIVE LETTER WORD, 400 POINTS WILL BE AWARDED")
print("                                  FOR A six LETTER WORD, 1200 POINTS WILL BE AWARDED")
print("                                     THE PLAYER WITH THE HIGHEST SCORE POINTS WINS")
print("                                                   GOOD LUCK!!!")



cho=input("ENTER UR OPTION: ")
print("")
if cho=='easy':
    l1 = ['lud', 'del', 'led', 'eld', 'use', 'sue', 'sel', 'leu', 'lsd', 'els', 'LUD', 'DEL', 'LED', 'ELD', 'USE',
          'SUE', 'SEL', 'LEU', 'LSD', 'ELS']
    l2 = ['duel', 'leud', 'lude', 'luds', 'dels', 'deus', 'dues', 'elds', 'lues', 'seul', 'sled', 'slue', 'sued',
          'used', 'DUEL', 'LEUD', 'LUDE', 'LUDS', 'DELS', 'DEUS', 'DUES', 'ELDS', 'LUES', 'SEUL', 'SLED', 'SLED',
          'SUED', 'USED']
    l3 = ['duels', 'dulse', 'leuds', 'ludes', 'slued', 'DUELS', 'DULSE', 'LEUDS', 'LUDES', 'SLUED']
    print("                                              PLAYER 1")
    print("                                             S/L/E/D/U")
    sum = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
        val = str(input("enter ur word: "))
        if val in l1:
            sum += 100
            print("your score is: %d" % sum)
            l1.remove(val)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum)
    print("")
    print("                                             S/L/E/D/U")
    print("FOUR LETTER WORDS ONLY!")
    sum1 = 0
    for i in range(3):
        val1 = str(input("enter ur word: "))
        if val1 in l2:
            sum1 += 200
            print("your score is: %d" % sum1)
            l2.remove(val1)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum1)
    print("")
    print("                                             S/L/E/D/U")
    print("FIVE LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(3):
        val2 = str(input("enter ur word: "))
        if val2 in l3:
            sum2 += 400
            print("your score is: %d" % sum2)
            l3.remove(val2)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum2)
    sum3 = sum + sum1 + sum2

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum3)
    print(" ")
    print("                                              PLAYER 2")
    print("                                             S/L/E/D/U")
    sum4 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
        val3 = str(input("enter ur word: "))
        if val3 in l1:
            sum4 += 100
            print("your score is: %d" % sum4)
            l1.remove(val3)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum4)
    print("")
    print("                                             S/L/E/D/U")
    print("FOUR LETTER WORDS ONLY!")
    sum5 = 0
    for i in range(3):
        val4 = str(input("enter ur word: "))
        if val4 in l2:
            sum5 += 200
            print("your score is: %d" % sum5)
            l2.remove(val4)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum5)
    print("")
    print("                                             S/L/E/D/U")
    print("FIVE LETTER WORDS ONLY!")
    sum6 = 0
    for i in range(2):
        val5 = str(input("enter ur word: "))
        if val5 in l3:
            sum6 += 400
            print("your score is: %d" % sum6)
            l3.remove(val5)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum6)
    sum7 = sum5 + sum6 + sum4

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum7)
elif cho=='EASY':
    l1 = ['lud', 'del', 'led', 'eld', 'use', 'sue', 'sel', 'leu', 'lsd', 'els', 'LUD', 'DEL', 'LED', 'ELD', 'USE',
          'SUE', 'SEL', 'LEU', 'LSD', 'ELS']
    l2 = ['duel', 'leud', 'lude', 'luds', 'dels', 'deus', 'dues', 'elds', 'lues', 'seul', 'sled', 'slue', 'sued',
          'used', 'DUEL', 'LEUD', 'LUDE', 'LUDS', 'DELS', 'DEUS', 'DUES', 'ELDS', 'LUES', 'SEUL', 'SLED', 'SLED',
          'SUED', 'USED']
    l3 = ['duels', 'dulse', 'leuds', 'ludes', 'slued', 'DUELS', 'DULSE', 'LEUDS', 'LUDES', 'SLUED']
    print("                                              PLAYER 1")
    print("                                             S/L/E/D/U")
    sum = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
        val = str(input("enter ur word: "))
        if val in l1:
            sum += 100
            print("your score is: %d" % sum)
            l1.remove(val)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum)
    print("")
    print("                                             S/L/E/D/U")
    print("FOUR LETTER WORDS ONLY!")
    sum1 = 0
    for i in range(3):
        val1 = str(input("enter ur word: "))
        if val1 in l2:
            sum1 += 200
            print("your score is: %d" % sum1)
            l2.remove(val1)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum1)
    print("")
    print("                                             S/L/E/D/U")
    print("FIVE LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(3):
        val2 = str(input("enter ur word: "))
        if val2 in l3:
            sum2 += 400
            print("your score is: %d" % sum2)
            l3.remove(val2)
        else:
            print("INVALID")
    print(" ")
    print("FINAL SCORE:%d" % sum2)
    sum3 = sum + sum1 + sum2

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum3)
    print(" ")
    print("                                              PLAYER 2")
    print("                                             S/L/E/D/U")
    sum4 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
        val3 = str(input("enter ur word: "))
        if val3 in l1:
            sum4 += 100
            print("your score is: %d" % sum4)
            l1.remove(val3)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum4)
    print("")
    print("                                             S/L/E/D/U")
    print("FOUR LETTER WORDS ONLY!")
    sum5 = 0
    for i in range(3):
        val4 = str(input("enter ur word: "))
        if val4 in l2:
            sum5 += 200
            print("your score is: %d" % sum5)
            l2.remove(val4)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum5)
    print("")
    print("                                             S/L/E/D/U")
    print("FIVE LETTER WORDS ONLY!")
    sum6 = 0
    for i in range(2):
        val5 = str(input("enter ur word: "))
        if val5 in l3:
            sum6 += 400
            print("your score is: %d" % sum6)
            l3.remove(val5)
        else:
            print("INVALID OR ALREADY USED BY PLAYER 1")
    print(" ")
    print("FINAL SCORE:%d" % sum6)
    sum7 = sum5 + sum6 + sum4

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum7)
elif cho=='medium':
    l1 = ['bam', 'ban', 'ben', 'man', 'nab', 'nam', 'neb', 'nem', 'bae', 'bee', 'eme', 'mae', 'mea', 'ane', 'nae',
          'nee', 'BAM', 'BAN', 'BEN', 'MAN', 'MEN', 'NAB', 'NAM', 'NEB', 'BAE', 'BEE', 'EME', 'MAE', 'MEA', 'ANE',
          'NAE', 'NEE']
    l2 = ['beam', 'bema', 'mabe', 'amen', 'bane', 'bean', 'been', 'bene', 'mane', 'mean', 'nabe', 'name', 'neem',
          'nema', 'BEAM', 'BEMA', 'MABE', 'AMEN', 'BANE', 'BEAN', 'BEEN', 'BENE', 'MANE', 'MEAN', 'NABE', 'NAME',
          'NEEM', 'NEMA']
    l3 = ['maneb', 'enema', 'MANED', 'ENEMA']
    l4 = ['BEMEAN', 'BENAME', 'bename', 'bemean']
    print("                                              PLAYER 1")
    print("                                             B/N/M/A/E/E")
    sum1 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
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
    print("                                             B/N/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(3):
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
    print("                                             B/N/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum3 = 0
    for i in range(1):
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
            sum4 += 1200
            print("your score is: %d" % sum4)
            l4.remove(val4)
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
    for i in range(3):
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
    for i in range(1):
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
    sum9 = sum8 + sum6 + sum5 + sum7

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum9)
elif cho=='MEDIUM':
    l1 = ['bam', 'ban', 'ben', 'man', 'nab', 'nam', 'neb', 'nem', 'bae', 'bee', 'eme', 'mae', 'mea', 'ane', 'nae',
          'nee', 'BAM', 'BAN', 'BEN', 'MAN', 'MEN', 'NAB', 'NAM', 'NEB', 'BAE', 'BEE', 'EME', 'MAE', 'MEA', 'ANE',
          'NAE', 'NEE']
    l2 = ['beam', 'bema', 'mabe', 'amen', 'bane', 'bean', 'been', 'bene', 'mane', 'mean', 'nabe', 'name', 'neem',
          'nema', 'BEAM', 'BEMA', 'MABE', 'AMEN', 'BANE', 'BEAN', 'BEEN', 'BENE', 'MANE', 'MEAN', 'NABE', 'NAME',
          'NEEM', 'NEMA']
    l3 = ['maneb', 'enema', 'MANED', 'ENEMA']
    l4 = ['BEMEAN', 'BENAME', 'bename', 'bemean']
    print("                                              PLAYER 1")
    print("                                             B/N/M/A/E/E")
    sum1 = 0
    print("THREE LETTER WORDS ONLY!")
    for i in range(3):
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
    print("                                             B/N/M/A/E/E")
    print("FOUR LETTER WORDS ONLY!")
    sum2 = 0
    for i in range(3):
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
    print("                                             B/N/M/A/E/E")
    print("FIVE LETTER WORDS ONLY!")
    sum3 = 0
    for i in range(1):
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
            sum4 += 1200
            print("your score is: %d" % sum4)
            l4.remove(val4)
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
    for i in range(3):
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
    for i in range(1):
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
    sum9 = sum8 + sum6 + sum5 + sum7

    print("                               FINAL SCORE FOR PLAYER1: %d" % sum9)
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
