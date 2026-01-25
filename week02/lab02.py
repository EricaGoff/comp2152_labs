# Week 02 Lab - Rock, Paper, Scissors Game

choices = ["Rock", "Paper", "Scissors"]

# Get Player Input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

# Convert to Integer
playerChoice = int(playerChoice)

# Error Handling (player)
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # Get Computer's Choice (simulated input for now)
    computerChoice = input("Enter computer's choice (1-3): ")
    computerChoice = int(computerChoice)

    # Error Handling (computer)
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        # Array Indexing (0-indexed)
        playerName = choices[playerChoice - 1]
        computerName = choices[computerChoice - 1]

        print(f"You chose: {playerName}")
        print(f"Computer chose: {computerName}")

        # Determine the Winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        # String Comparison requirement
        if playerName != "Rock":
            print("You didn't pick the classic Rock...")
