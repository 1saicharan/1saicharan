l= True
k = 1
def assign_tiktok(value,place):
    if value == "o" or value == "O":
        places[place] ='O'
        return places[place]

    elif value=='x' or value == 'X':
        places[place]='X'
        return places[place]
    else:
        print('!!!!!!!you enterd wrong letter !!!!!! please enter x or o')

def check(places):
    if [places[0],places[1],places[2]] != [' ',' ',' ']:
        if places[0]==places[1] and places[1] == places[2]:
            return ('you won the game') 
    elif [places[0],places[3],places[6]] != [' ',' ',' ']:
        if places[0]==places[3] and places[3] == places[6]:
            return ('you won the game')
    elif [places[0],places[3],places[6]] != [' ',' ',' ']:
        if places[2]==places[5] and places[5] == places[8]:
            return('you won the game')
    elif [places[0],places[3],places[6]] != [' ',' ',' ']:
        if places[6]==places[7] and places[7] == places[8]:
            return ('you won the game')
    elif [places[0],places[3],places[6]] != [' ',' ',' ']:
        if places[0]==places[4] and places[4] == places[8]:
            return ('you won the game')
    elif [places[0],places[3],places[6]] != [' ',' ',' ']:
        if places[2]==places[4] and places[4] == places[6]:
            return ('you won the game')
    elif ' ' not in places:
        return ('game is tie\n both are good\n play again ')
    else:
        return ('continue the game')

def display_tiktok(places):
    print(f'|{places[0]}|{places[1]}|{places[2]}|\n|{places[3]}|{places[4]}|{places[5]}|\n|{places[6]}|{places[7]}|{places[8]}| \n')

def num():
    global l
    if  l:
        l = False
        return 1
    else:
        l = True
        return 2


places = [' ',' ' , ' ', ' ', ' ',' ' ,' ' , ' ',' ' ]
places = [' ',' ' , ' ', ' ', ' ',' ' ,' ' , ' ',' ' ]
print('welcome to tik tok toe')
print("|0|1|2|\n|3|4|5|\n|6|7|8|\nplease enter values according\n please enter string values o or x\n !!!!don't enter entered values ")
print("| | | |\n| | | |\n| | | |")
while k!=0:
    print('|0|1|2|\n|3|4|5|\n|6|7|8|\nplease enter values according\n please enter string values o or x')
    number = num()
    if number == 1:
        value = input(f"it's  turn of number {number} player give input as x  ....")
    else:
        value = input(f"it's  turn of number {number} player give input as o  ....")
    place = int(input('give input corresponding to displayed numbers...'))
    if places[place] not in['X','O','x','o']:
        assign_tiktok(value,place)
        print('\n'*100)
        display_tiktok(places)
        name = check(places)
        if  name =='you won the game' :
            print(f'player {number} has won the game')
            break
        elif name == 'game is tie\n both are good\n play again' :
            print('both are great no one won the game')
            break
        else:
            continue
       
    else:
        print('you have entered position which has been already entered so you lost the chance')
        continue
    
    
    


