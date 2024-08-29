def check_validity(choice: str) -> int:
    """
    Validates the player's choice and returns a corresponding integer.

    Parameters:
        choice (str): The player's choice ('rock', 'paper', or 'scissors').

    Returns:
        int: 2 for 'rock', 1 for 'scissors', 0 for 'paper'.

    Raises:
        ValueError: If the choice is not 'rock', 'paper', or 'scissors'.
    """
    choice = choice.lower()
    if choice == "rock":
        return 2
    elif choice == "scissors":
        return 1
    elif choice == "paper":
        return 0
    else:
        raise ValueError("illegal choice")


def check_winner(player1_choice: int, player2_choice: int) -> int:
    """
    Determines the winner of the game based on players' choices.

    Parameters:
        player1_choice (int): Choice of player 1 (0 for 'paper', 1 for 'scissors', 2 for 'rock').
        player2_choice (int): Choice of player 2 (0 for 'paper', 1 for 'scissors', 2 for 'rock').

    Returns:
        int: 0 for a tie, 1 if player 1 wins, 2 if player 2 wins.

    Raises:
        ValueError: If any choice is not 0, 1, or 2.
    """
    if player1_choice not in [0, 1, 2] or player2_choice not in [0, 1, 2]:
        raise ValueError("illegal game option")

    if player1_choice == player2_choice:
        return 0
    elif (player1_choice == 0 and player2_choice == 2) or \
            (player1_choice == 1 and player2_choice == 0) or \
            (player1_choice == 2 and player2_choice == 1):
        return 1
    else:
        return 2


def play_game():
    """
    Runs the game loop, getting player inputs and determining the winner.
    """
    player1 = input("Player 1, enter your choice (rock, paper, scissors): ")
    player2 = input("Player 2, enter your choice (rock, paper, scissors): ")

    try:
        player1_choice = check_validity(player1)
        player2_choice = check_validity(player2)

        result = check_winner(player1_choice, player2_choice)

        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    play_game()
