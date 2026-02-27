raw_data = {'players': {'alice': {'level': 41, 'total_score': 2824, 'sessions_played': 13, 'favorite_mode': 'ranked', 'achievements_count': 5}, 'bob': {'level': 16, 'total_score': 4657, 'sessions_played': 27, 'favorite_mode': 'ranked', 'achievements_count': 2}, 'charlie': {'level': 44, 'total_score': 9935, 'sessions_played': 21, 'favorite_mode': 'ranked', 'achievements_count': 7}, 'diana': {'level': 3, 'total_score': 1488, 'sessions_played': 21, 'favorite_mode': 'casual', 'achievements_count': 4}, 'eve': {'level': 33, 'total_score': 1434, 'sessions_played': 81, 'favorite_mode': 'casual', 'achievements_count': 7}, 'frank': {'level': 15, 'total_score': 8359, 'sessions_played': 85, 'favorite_mode': 'competitive', 'achievements_count': 1}}, 'sessions': [{'player': 'bob', 'duration_minutes': 94, 'score': 1831, 'mode': 'competitive', 'completed': False}, {'player': 'bob', 'duration_minutes': 32, 'score': 1478, 'mode': 'casual', 'completed': True}, {'player': 'diana', 'duration_minutes': 17, 'score': 1570, 'mode': 'competitive', 'completed': False}, {'player': 'alice', 'duration_minutes': 98, 'score': 1981, 'mode': 'ranked', 'completed': True}, {'player': 'diana', 'duration_minutes': 15, 'score': 2361, 'mode': 'competitive', 'completed': False}, {'player': 'eve', 'duration_minutes': 29, 'score': 2985, 'mode': 'casual', 'completed': True}, {'player': 'frank', 'duration_minutes': 34, 'score': 1285, 'mode': 'casual', 'completed': True}, {'player': 'alice', 'duration_minutes': 53, 'score': 1238, 'mode': 'competitive', 'completed': False}, {'player': 'bob', 'duration_minutes': 52, 'score': 1555, 'mode': 'casual', 'completed': False}, {'player': 'frank', 'duration_minutes': 92, 'score': 2754, 'mode': 'casual', 'completed': True}, {'player': 'eve', 'duration_minutes': 98, 'score': 1102, 'mode': 'casual', 'completed': False}, {'player': 'diana', 'duration_minutes': 39, 'score': 2721, 'mode': 'ranked', 'completed': True}, {'player': 'frank', 'duration_minutes': 46, 'score': 329, 'mode': 'casual', 'completed': True}, {'player': 'charlie', 'duration_minutes': 56, 'score': 1196, 'mode': 'casual', 'completed': True}, {'player': 'eve', 'duration_minutes': 117, 'score': 1388, 'mode': 'casual', 'completed': False}, {'player': 'diana', 'duration_minutes': 118, 'score': 2733, 'mode': 'competitive', 'completed': True}, {'player': 'charlie', 'duration_minutes': 22, 'score': 1110, 'mode': 'ranked', 'completed': False}, {'player': 'frank', 'duration_minutes': 79, 'score': 1854, 'mode': 'ranked', 'completed': False}, {'player': 'charlie', 'duration_minutes': 33, 'score': 666, 'mode': 'ranked', 'completed': False}, {'player': 'alice', 'duration_minutes': 101, 'score': 292, 'mode': 'casual', 'completed': True}, {'player': 'frank', 'duration_minutes': 25, 'score': 2887, 'mode': 'competitive', 'completed': True}, {'player': 'diana', 'duration_minutes': 53, 'score': 2540, 'mode': 'competitive', 'completed': False}, {'player': 'eve', 'duration_minutes': 115, 'score': 147, 'mode': 'ranked', 'completed': True}, {'player': 'frank', 'duration_minutes': 118, 'score': 2299, 'mode': 'competitive', 'completed': False}, {'player': 'alice', 'duration_minutes': 42, 'score': 1880, 'mode': 'casual', 'completed': False}, {'player': 'alice', 'duration_minutes': 97, 'score': 1178, 'mode': 'ranked', 'completed': True}, {'player': 'eve', 'duration_minutes': 18, 'score': 2661, 'mode': 'competitive', 'completed': True}, {'player': 'bob', 'duration_minutes': 52, 'score': 761, 'mode': 'ranked', 'completed': True}, {'player': 'eve', 'duration_minutes': 46, 'score': 2101, 'mode': 'casual', 'completed': True}, {'player': 'charlie', 'duration_minutes': 117, 'score': 1359, 'mode': 'casual', 'completed': True}], 'game_modes': ['casual', 'competitive', 'ranked'], 'achievements': ['first_blood', 'level_master', 'speed_runner', 'treasure_seeker', 'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer']}

def list_comprehension(data: list) -> None:
    print("=== List comprehension Examples ===")
    
    count = 0
    combined_scores = 0
    players_dict = data['players']

    high_scorers = [name for name, stats in players_dict.items() 
                    if stats['total_score'] > 2000]

    active_players = [name for name, stats in players_dict.items()
                      if stats['sessions_played'] > 20]

    all_scores = [stats['total_score'] for stats in data['players'].values()]
    for score in all_scores:
        combined_scores += score
        count += 1
    average_scores = combined_scores / count

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Active players: {active_players}")
    print(f"Average scores: {average_scores:.2f}\n")

def dict_comprehension(data: list) -> None:
    print("=== Dict Comprehension Examples ===")

    player_scores = {name: stats['total_score'] for name,
                     stats in data['players'].items()}
    favorite_modes = {name : stats['favorite_mode'] for name,
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
    list_comprehension(raw_data)
    dict_comprehension(raw_data)
    set_comprehension(raw_data)
    combined_analysis(raw_data)

if __name__ == "__main__":
    main()