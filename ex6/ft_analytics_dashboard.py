def list_comprehension(data: list) -> None:
    """Demonstrate list comprehension with player data."""
    print("=== List comprehension Examples ===")
    count = 0
    combined_scores = 0
    players_dict = data['players']

    high_scorers = [name for name, stats in players_dict.items()
                    if stats['total_score'] > 2000]

    active_players = [name for name, stats in players_dict.items()
                      if stats['sessions_played'] > 20]

    all_scores = [stats['total_score']
                  for stats in data['players'].values()]
    for score in all_scores:
        combined_scores += score
        count += 1
    average_scores = combined_scores / count

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Active players: {active_players}")
    print(f"Average scores: {average_scores:.2f}\n")


def dict_comprehension(data: list) -> None:
    """Demonstrate dict comprehension with player data."""
    print("=== Dict Comprehension Examples ===")

    player_scores = {name: stats['total_score'] for name,
                     stats in data['players'].items()}
    favorite_modes = {name: stats['favorite_mode'] for name,
                      stats in data['players'].items()}
    achievement_counts = {name: stats['achievements_count'] for name,
                          stats in data['players'].items()}

    print(f"{player_scores}")
    print(f"{favorite_modes}")
    print(f"{achievement_counts}\n")


def set_comprehension(data: list) -> None:
    print("=== Set Comprehension Examples ===")
    unique_players = {u_player for u_player in data['players']}
    incomplete_modes = {s['mode'] for s in data['sessions']
                        if not s['completed']}
    print(f"{incomplete_modes}")
    print(f"{unique_players}")


def combined_analysis(data: list) -> None:
    max_duration = max([s['duration_minutes'] for s in data['sessions']])

    print("\n=== Combined Analysis ===")
    print(f"Total Players: {len(data['players'])}")
    print(f"Longest Session: {max_duration} minutes\n")


def main():
    print("=== Game Analytics Dashboard ===\n")
    # list_comprehension(raw_data)
    # dict_comprehension(raw_data)
    # set_comprehension(raw_data)
    # combined_analysis(raw_data)


if __name__ == "__main__":
    main()
