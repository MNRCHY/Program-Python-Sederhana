# Made By MNRCH
# https://github.com/MNRCHY

print ("")
print ("============================")
print ("=== Ayo main Tic Tac Toe ===")
print ("============================")
print ("")

# Conf_Papan
papan = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

papan_key = []

for key in papan:
    papan_key.append(key)

def printPapan(papan):
    print (papan['7'] + '|' + papan['8'] + '|' + papan['9'])
    print ('--+--+--')
    print (papan['4'] + '|' + papan['5'] + '|' + papan['6'])
    print ('--+--+--')
    print (papan['1'] + '|' + papan['2'] + '|' + papan['3'])

# Main_Func
def game():

    turn = 'X'
    count = 0

for i in range(10):
    printPapan(papan)
    print ( "Sekarang giliranmu,", turn, ". mau pasang dimana?")

    move = input()

    if papan[move] == ' ':
        papan[move] = turn
        count += 1

    else:
        print("Spot sudah ditempati, silahkan pilih spot lain.")
        continue
    





''' Reference: https://bit.ly/3mftrA3 '''