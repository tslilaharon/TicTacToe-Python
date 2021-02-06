import os.path
from os import path

 # פונקציה הצגת התפריט
def show_menu():
    print ("\n ✲´*。Game menu *´。*✲")
    print ("1. Rules of the Game")
    print ("2. play the Game")
    print ("3. Help") 
    print ("4. Exit\n")
    
def Print_Rules():
    #חוקי המשחק
    print(' ')
    print(' ')
    print('       ✲´*。Rules for TIC TAC TOE -X-O- Game *´。*✲')
    print('      ________________________________________________')
    print(' ')
    print('1. The game played on a board of 3 squares on 3 squares')
    print('2. There are 2 players in the game one is X and the other is O')
    print('3. Players alternate turn after turn and players must place their ')
    print('   markers in the empty squares according to the position table')
    print('4. The first player to receive 3 of her consecutive scores')
    print('  (up, down, sideways or diagonally) is the winner)')
    print('5. When all 9 squares are full, the game is over.')
    print('   If no player has 3 consecutive signs, the game ends in a draw. ')
    print(' ')
    
    #טבלת מיקומים
    print('         ✲´*。Position on the Game Board *´。*✲')
    print('         _________________________________________')
    print('                     _____________')
    print(' ')
    print('                      01 |02 | 03')
    print('                       - + - + -')
    print('                      04 |05 | 06')
    print('                       - + - + -')
    print('                      07 |08 | 09')
    print('                     _____________')
    print(' ')

        
#פונקציה לקבלת עזרה            
def get_help():
 
    print('                 _   _ _____ _     ____ ') 
    print('                | | | | ____| |   |  _ \ ')
    print('                | |_| |  _| | |   | |_) | ')
    print('                |  _  | |___| |___|  __/ ')
    print('                |_| |_|_____|_____|_|  ')  
    print('')
    print('To win you need')
    print('Pay attention to the following :')
    print('Mark in the empty squares for the purpose of dipping the locations')
    print('The first players to receive 3 consecutive scores')
    print('Up, down, laterally or diagonally) is the winner')
    print('When all 9 squares are full, the game is over. Print')
    print('Position on the Game Board')
    print('')
    print('         ✲´*。Position on the Game Board *´。*✲')
    print('         _________________________________________')
    print('                     _____________')
    print(' ')
    print('                      01 |02 | 03')
    print('                       - + - + -')
    print('                      04 |05 | 06')
    print('                       - + - + -')
    print('                      07 |08 | 09')
    print('                     _____________')
    print(' ')

#כתיבה לקובץ
def w_file():
    # אם הקובץ לא קיים
    if path.exists("PlayerName.txt") == False:
        Xname = input("Please Enter Player X Name: ")
        print(f"Hey Player X {Xname} !")
        Oname = input("Please Enter Player O Name: ")
        print(f"Hey Player O {Oname} !")
        print(f"{Xname} -vs- {Oname} Let's Go!\n")
        f = open("PlayerName.txt", "w")
        f.write(f"{Xname} -vs- {Oname} \n")
        f.close()
    # אם הקובץ קיים 
    else:
        Xname = input("Please Enter Player X Name: ")
        print(f"Hey Player X {Xname} !")
        Oname = input("Please Enter Player O Name: ")
        print(f"Hey Player O {Oname} !")
        print(f"{Xname} -vs- {Oname} Let's Go!\n")
        f = open("PlayerName.txt", "a")
        f.write(f"{Xname} -vs- {Oname} \n")
        f.close()

        
#קריאה מקובץ        
def r_file():
    arrl = []
    with open('PlayerName.txt', 'r') as file:
        for line in file:
            arrl.append(line)
        arrn = arrl[-1].split(" ") #הפרדת המילים לפי הרווח
        Xname = arrn[0]
        Oname = arrn[2]
        arrn = [Xname , Oname]
        return arrn
    
#פונקציה סגירת המשחק
def get_ByeBye(Xname,Oname):
    print(' ____              ____             ')  
    print('| __ ) _   _  ___ | __ ) _   _  ___ ')
    print('|  _ \| | | |/ _ \|  _ \| | | |/ _ \ ')
    print('| |_) | |_| |  __/| |_) | |_| |  __/')
    print('|____/ \__, |\___||____/ \__, |\___|')
    print('       |___/             |___/      ')
    print(f"         - {Xname} and {Oname} -        \n")


#פונקציה המחזירה את המנצח 
def get_win(game_board,Xname,Oname):
    
    # X - Row
    
    if game_board['01'] == 'X' and game_board['02'] == 'X' and game_board['03'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1        
    if game_board['04'] == 'X' and game_board['05'] == 'X' and game_board['06'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['07'] == 'X' and game_board['08'] == 'X' and game_board['09'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    # X - column

    if game_board['01'] == 'X' and game_board['04'] == 'X' and game_board['07'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['02'] == 'X' and game_board['05'] == 'X' and game_board['08'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['03'] == 'X' and game_board['06'] == 'X' and game_board['09'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1

    # X - slant

    if game_board['01'] == 'X' and game_board['05'] == 'X' and game_board['09'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['03'] == 'X' and game_board['05'] == 'X' and game_board['07'] == 'X':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Xname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player X WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1

    # O - Row

    if game_board['01'] == 'O' and game_board['02'] == 'O' and game_board['03'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['04'] == 'O' and game_board['05'] == 'O' and game_board['06'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1
        
    if game_board['07'] == 'O' and game_board['08'] == 'O' and game_board['09'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1

    # O - column
        
    if game_board['01'] == 'O' and game_board['04'] == 'O' and game_board['07'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1       
    if game_board['02'] == 'O' and game_board['05'] == 'O' and game_board['08'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1       
        
    if game_board['03'] == 'O' and game_board['06'] == 'O' and game_board['09'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1       

    # O - slant
        
    if game_board['01'] == 'O' and game_board['05'] == 'O' and game_board['09'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1       
    
    if game_board['03'] == 'O' and game_board['05'] == 'O' and game_board['07'] == 'O':
        print('___________________________________________\n')
        print(f'        ¨¯`.。*´YAY {Oname}´*。.¨¯`          ')
        print('\n。❄。*。¨¯`*✲ Player O WIN ! ´*。.❄¨¯`*✲\n')
        print('___________________________________________')
        return 1       
    return 0



#פונקצית המשחק 
def game(Xname,Oname):
#לוח המשחק 
    game_board = {
        '01': ' ', '02': ' ', '03': ' ',
        '04': ' ', '05': ' ', '06': ' ',
        '07': ' ', '08': ' ', '09': ' '
    }
    player = 1      
    count_moves = 0
    check = 0
    while True:
        print(game_board['01'] + ' | ' + game_board['02'] + ' | ' + game_board['03'])
        print('- + - + -')
        print(game_board['04'] + ' | ' + game_board['05'] + ' | ' + game_board['06'])
        print('- + - + -')
        print(game_board['07'] + ' | ' + game_board['08'] + ' | ' + game_board['09'])
        print(' ')
        print('-Enter H For Help-\n')
        
        check = get_win(game_board,Xname,Oname)
        
        if count_moves == 9  and check == 0:
            print('___________________________________________')
            print('\n       There is no winner Equality \n')
            print('          ▐▬▬▬ game over ▬▬▬▌\n')
            print('___________________________________________')
            break
        
        if count_moves == 9 or check == 1:
            break
        
        while True:
            #הקלט של שחקן X
            if player == 1:  
                px_input = input(f'player x -{Xname}- ')
                if px_input == 'H':
                    get_help()
                    continue
                if px_input in game_board and game_board[px_input] == ' ':
                    game_board[px_input] = 'X'
                    player = 2
                    break
                else:
                    print(f'Invalid input *{px_input}*, please try again')
                    continue
            else:
                #קלט של שחקן O
                po_input = input(f'player o -{Oname}- ')
                if po_input == 'H':
                    get_help()
                    continue
                if po_input in game_board and game_board[po_input] == ' ':
                    game_board[po_input] = 'O'
                    player = 1
                    break
                else: 
                    print(f'Invalid input *{po_input}*, please try again')
                    continue
        count_moves +=1
        print('____________________')
        print(' ')


    
 #פונקציה הראשית 
def main():
    print('              _____ ___ ___   _____ _   ___   _____ ___  ___')
    print('             |_   _|_ _/ __| |_   _/_\ / __| |_   _/ _ \| __|')
    print('               | |  | | (__    | |/ _ | (__    | || (_) | _|') 
    print('               |_| |___\___|   |_/_/ \_\___|   |_| \___/|___|')
    print('             _________________________________________________')
    while True:
        show_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            Print_Rules()
        elif choice == '2':
            w_file()
            arrn = r_file()
            Xname = arrn[0]
            Oname = arrn[1]
            game(Xname,Oname)
        elif choice == '3':
            get_help()
        elif choice == '4':
             arrn = r_file()
             Xname = arrn[0]
             Oname = arrn[1]
             get_ByeBye(Xname,Oname)
             return
        else:
            print(f'Not a correct choice: *{choice}* ,please try again')
 
if __name__ == '__main__':
    main()
