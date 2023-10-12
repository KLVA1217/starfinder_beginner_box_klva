turn = 1

while ( (int(player_instance.hp) > 0) or (int(character_instance.hp) > 0) ):
    if (turn == 1):
        # player attempt to attack character
        turn = turn - 1
    else:
        # character attemtps to attack player
        turn = turn + 1