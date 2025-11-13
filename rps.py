
import random

CHOICES = ["rock", "paper", "scissors"]

def decide(player, comp):
    if player == comp:
        return 0  # tie
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    return 1 if wins[player] == comp else -1

def get_choice(prompt="Choose (rock/paper/scissors): "):
    while True:
        s = input(prompt).strip().lower()
        if s in CHOICES:
            return s
        print("Invalid choice. Type rock, paper, or scissors.")

def play_round():
    player = get_choice()
    comp = random.choice(CHOICES)
    outcome = decide(player, comp)
    print(f"You chose: {player}  |  Computer chose: {comp}")
    if outcome == 0:
        print("Result: It's a tie!")
    elif outcome == 1:
        print("Result: You win this round 🎉")
    else:
        print("Result: Computer wins this round 😢")
    return outcome

def play_best_of(n):
    needed = n // 2 + 1
    score_p = score_c = 0
    round_no = 1
    while score_p < needed and score_c < needed:
        print(f"\n--- Round {round_no} (First to {needed}) ---")
        result = play_round()
        if result == 1:
            score_p += 1
        elif result == -1:
            score_c += 1
        print(f"Score -> You: {score_p}  Computer: {score_c}")
        round_no += 1
    return 1 if score_p > score_c else -1

def main():
    print("Welcome to Rock Paper Scissors!")
    try:
        while True:
            raw = input("Play best of how many rounds? (enter odd number e.g. 1,3,5) [default 3]: ").strip()
            if raw == "":
                n = 3
            else:
                try:
                    n = int(raw)
                    if n <= 0 or n % 2 == 0:
                        print("Please enter a positive odd number.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue

            winner = play_best_of(n)
            if winner == 1:
                print("\n🎊 Congratulations — you won the match!")
            else:
                print("\n🤖 The computer won the match. Better luck next time!")

            again = input("Play another match? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Thanks for playing — bye!")
                break
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")

if __name__ == "__main__":
    main()
