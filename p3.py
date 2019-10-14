'''game =[[1,2,2,2],
      [1,1,0,0],
      [1,0,1,0],
      [2,0,0,1],]'''
game_won =False 
curr_plyr=0

play = True 
player = [1,2]


def win(game_map):

    #horizontal
    for row in game_map:
        if row.count(row[0])== len(row) and row[0] != 0:
            print(f"Horizontal {row[0]} winner")

    #vertical_winner
    for col in range(len(game)):

        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0])== len(check) and check[0] != 0:
            print(f"Vertical {check[0]} winner")


    diags1=[]
    diags2=[]
    for ix in range(len(game)):
        diags1.append(game[ix][ix])
        diags2.append(game[ix][(len(game)-1)-ix])

    if diags1.count(diags1[0])== len(diags1) and diags1[0] != 0:
       game_won=True
       print(f"Diagonal {diags1[0]} winner")
       play = False

    elif diags2.count(diags2[0])== len(diags2) and diags2[0] != 0:
        game_won=True
        print(f"Diagonal {diags2[0]} winner")
        play=False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column]=player
        for count,row  in enumerate(game_map):
            print(count,row)
        return game_map

    except IndexError as e:
        print("Error:make sure you input row/column as 0 1 2",e)

    except Exception as e:
        print("Something went very wrong!",e)


while play:
    game =[[0,0,0],
           [0,0,0],
           [0,0,0]]

    while game_won== False:
        past_plyr=curr_plyr
        column_choice =int(input("What column do you want to play? (0,1,2):  "))
        row_choice =int(input("What row do you want to play? (0,1,2):  "))
        game = game_board(game,curr_plyr+1,row_choice,column_choice)
        curr_plyr=(1-past_plyr)
        win (game)
         
    





