import random

player1_totalscore = 0
player2_totalscore = 0
player1_turn_score = 0
player2_turn_score = 0


score= 0
command = " "
player_turn = 0

command = input("command r to roll > ")

while player1_totalscore < 100 and player2_totalscore < 100:

    #Player 1 rolls the dice
    if command == "r":
        roll = random.randint(1,6)
        if roll == 1:
            player1_totalscore = 0
        else:
            player1_totalscore = player1_turn_score + roll
    else:
        player_turn = 1
    
    if command == "h":
        #roll = random.randint(1,6)
        player1_turn_score = player1_totalscore + roll

command = input("Would you like to roll again? Type r, to hold type h > ")

    if command == "r":
        roll = random.randint(1,6)
        if roll == 1:
            player2_totalscore = 0
        else:
            player2_totalscore = player2_turn_score + roll
    else:
        player_turn = 1
        
    if command == "h":
        #roll = random.randint(1,6)
        player2_turn_score = player2_totalscore + roll

print(player1_totalscore) 