# Snakes and Ladders
player_position = 1
while True:
    dice = int(input("Enter dice roll data: "))
    player_position = player_position + dice

    if player_position == 100:
        print(f"You are now on square {player_position}")
        print("You Win!")
        break
    elif player_position < 100:
        game_dict = {
            9 : 34,
            54 : 19,
            40 : 64,
            90 : 48,
            67 : 86,
            99 : 77
        }
        if player_position in game_dict:
            player_position = game_dict[player_position]
        else:
            player_position = player_position - dice

        # if player_position == 9:
        #     player_position = 34
        # elif player_position == 40:
        #     player_position = 64
        # elif player_position == 67:
        #     player_position = 86
        # elif player_position == 54:
        #     player_position = 19
        # elif player_position == 90:
        #     player_position = 48
        # elif player_position == 99:
        #     player_position = 77
    # else:
    #     player_position = player_position - dice
    print(f"You are now on square {player_position}")