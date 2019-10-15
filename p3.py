import itertools

play = True 
player = [1,2]


def win(game_map):

    #horizontal
    for row in game_map:
        if row.count(row[0])== len(row) and row[0] != 0:
            print(f"Horizontal {row[0]} winner")
            return True

    #vertical_winner
    for col in range(len(game)):

        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0])== len(check) and check[0] != 0:
            print(f"Vertical {check[0]} winner")
            return True


    diags1=[]
    diags2=[]
    for ix in range(len(game)):
        diags1.append(game[ix][ix])
        diags2.append(game[ix][(len(game)-1)-ix])

    if diags1.count(diags1[0])== len(diags1) and diags1[0] != 0:
       print(f"Diagonal {diags1[0]} winner")
       return True

    elif diags2.count(diags2[0])== len(diags2) and diags2[0] != 0:
        print(f"Diagonal {diags2[0]} winner")
        return True

    return False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    
    if game_map[row][column]!=0:
        played=False
        print("This Place is occupied please choose another position to play!")
        return game_map,played

    try:
        s="   " +"  ".join([str(i)for i in range(game_size)])
        print(s)
        if not just_display:
            game_map[row][column]=player
        for count,row  in enumerate(game_map):
            print(count,row)
        return game_map,True

    except IndexError as e:
        print("Error:make sure you input row/column as 0 1 2",e)
        return game_map,True

    except Exception as e:
        print("Something went very wrong!",e)
        return game_map,True

    return True


while play:
    game_size=int(input("please input the gameboard size you wanna play on:  "))
    game=[[0 for i in range(game_size)]for i in range(game_size)]


    game_won =False 

    game,_=game_board(game,just_display=True)
    player_choice =itertools.cycle([1,2])

    while not game_won:
        curr_plyr =next(player_choice)
        print(f"Current PLayer: {curr_plyr}")
        played =False

        while not played:
            column_choice =int(input("What column do you want to play? (0,1,2):  "))
            row_choice =int(input("What row do you want to play? (0,1,2):  "))
            game,played = game_board(game,curr_plyr,row_choice,column_choice)

        if win(game):
            game_won=True
            again = input("GAME OVER DO YOU WANT TO PLAY AGAIN, y/n??  ")
            if again.lower() == 'y':
                print("Restrating game....")

            elif again.lower() =='n':
                print("Byeeeeeeee....THANK YOU FOR PLAYING!")
                play=False

            else:
                print("NOT A VALID ANSWER ,SO....seee yaaa")
                play =False
