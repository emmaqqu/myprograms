# Snakes and Ladders
player_position = 1
while True:
    dice = int(input())
    player_position = player_position + dice

    if player_position == 100:
        print(f"You are now on square {player_position}")
        break
    else:
        if player_position == 9:
            player_position = 34
        elif player_position == 40:
            player_position = 64
        elif player_position == 67:
            player_position = 86
        elif player_position == 54:
            player_position = 19
        elif player_position == 90:
            player_position = 48
        elif player_position == 99:
            player_position = 77
    if player_position > 100:
            player_position = player_position - dice
    print(f"You are now on square {player_position}")

print("You Win!")