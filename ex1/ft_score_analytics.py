from sys import argv

def main():
    """ Function that takes scores """
    print("=== Player Score Analytics === \n")
    av_len = len(argv)
    if (av_len == 1):
        print(f"No Scores were provided. Usage: python3 {argv[0]} <score 1> <score 2> ...")
        return
    try:
        # Storing all the values
        scores = [int(num) for num in argv[1:]]
        total_players = av_len - 1
        total_score = sum(scores)
        average_score = float(total_score / total_players)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        # Printing the required scores
        print(f"Scores processed: {scores}")
        print(f"Total Players {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: %.2f" %(average_score))
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")

    except ValueError:
        print("Bruhh we're expecting an int value")

if __name__ == "__main__":
    main()