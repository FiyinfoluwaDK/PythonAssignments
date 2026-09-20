player_one = input("Choose (rock/paper/scissors): ")
player_two = input("Choose (rock/paper/scissors): ")

if player_one == player_two:
    print("Tie")
elif player_one == "rock" and player_two == "scissors":
    print("Player 1 Wins!")
elif player_one == "scissors" and player_two == "rock":
    print("Player 2 Wins!")
elif player_one == "paper" and player_two == "scissors":
    print("Player 2 Wins!")
elif player_one == "scissors" and player_two == "paper":
    print("Player 1 Wins!")
elif player_one == "paper" and player_two == "rock":
    print("Player 1 Wins!")
elif player_one == "rock" and player_two == "paper":
    print("Player 2 Wins!")

