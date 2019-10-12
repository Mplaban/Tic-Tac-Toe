game =[[1,1,1,1],
      [1,1,0,0],
      [1,0,1,0],
      [1,0,0,1],]


'''cols = reversed(range(len(game)))
rows = range(len(game))

for col,row in enumerate(cols):
    print(col,row)'''


'''diags1=[]
diags2=[]
for ix in range(len(game)):
    diags1.append(game[ix][ix])
    diags2.append(game[ix][(len(game)-1)-ix])

if diags1.count(diags1[0])== len(diags1) and diags1[0] != 0:
    print("winner")
print(diags2)
if diags2.count(diags2[0])== len(diags2) and diags2[0] != 0:
    print("winner")'''





#vertical_winner

'''for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0])== len(check) and check[0] != 0:
        print("winner")'''




def game_board(game_map):
    for row in game_map:
        if row.count(row[0])== len(row) and row[0] != 0:
            print("Horizontal winner")

    #vertical_winner
    for col in range(len(game)):

        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0])== len(check) and check[0] != 0:
            print("Vertical winner")


    diags1=[]
    diags2=[]
    for ix in range(len(game)):
        diags1.append(game[ix][ix])
        diags2.append(game[ix][(len(game)-1)-ix])

    if diags1.count(diags1[0])== len(diags1) and diags1[0] != 0:
        print("Diagonal winner")

    elif diags2.count(diags2[0])== len(diags2) and diags2[0] != 0:
        print("Diagonal winner")


    return game_map

game_board(game)




