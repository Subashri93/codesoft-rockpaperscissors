import random

def get_user_pick():
    while True:
        user_pick = input("Choose your weapon (rock, paper, or scissors): ").lower()
        if user_pick in ['rock', 'paper', 'scissors']:
            return user_pick
        else:
            print("Invalid choice. Please select rock, paper, or scissors.")

def get_computer_pick(user_pick):
    responses = {
        'rock': ['paper', 'scissors', 'scissors'],
        'paper': ['rock', 'scissors', 'scissors'],
        'scissors': ['rock', 'paper', 'paper']
    }
    return random.choice(responses[user_pick])

def determine_victor(user_pick, computer_pick):
    if user_pick == computer_pick:
        return "It's a stalemate!"
    elif (user_pick == 'rock' and computer_pick == 'scissors') or \
         (user_pick == 'paper' and computer_pick == 'rock') or \
         (user_pick == 'scissors' and computer_pick == 'paper'):
        return "You emerge victorious!"
    else:
        return "Computer prevails!"

def play_match(rounds):
    print(f"Let's engage in {rounds} rounds of Rock, Paper, Scissors!")
    user_wins = 0
    computer_wins = 0
    for _ in range(rounds):
        user_pick = get_user_pick()
        computer_pick = get_computer_pick(user_pick)
        print("Computer chooses:", computer_pick)
        result = determine_victor(user_pick, computer_pick)
        print(result)
        if "victorious" in result:
            user_wins += 1
        elif "Computer" in result:
            computer_wins += 1
    print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
    if user_wins > computer_wins:
        print("You win the match!")
    elif computer_wins > user_wins:
        print("Computer wins the match!")
    else:
        print("The match ends in a tie!")

if __name__ == "__main__":
    rounds = int(input("How many rounds do you want to play? "))
    play_match(rounds)
