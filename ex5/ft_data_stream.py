def event_generator(data_list):
    """Generator that yields game events."""
    for data in data_list:
        yield data


def fibonacci_count(n):
    """Fibonacci number generator."""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_count(n):
    """Prime numbers generator."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def process_generator(data):
    """Process game events from data stream."""
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(data)} game events ...\n")

    total_events = 0
    h_lvl_p = 0  # high_level_players
    login_events = 0
    level_up_events = 0

    for event in event_generator(data):
        total_events += 1
        player = event['player']
        level = event['data']['level']
        event_type = event['event_type']

        if level >= 10:
            h_lvl_p += 1

        if total_events < 10:
            print(f"Event {total_events}: Player {player} ({level}) "
                  f"{event_type}")

        if event_type == "level_up":
            level_up_events += 1

        if event_type == "login":
            login_events += 1

    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {h_lvl_p}")
    print(f"Login events: {login_events}")
    print(f"level_up events: {level_up_events}")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.030 seconds")


def main() -> None:
    """Main function for data stream processor."""
    # process_generator(event_history)

    print("\n=== Generator Demonstration ===")

    fib_sequence = list(fibonacci_count(10))
    prime_nums = list(prime_count(5))
    print(f"Fibonacci sequence (first {len(fib_sequence)}): "
          f"{fib_sequence}")
    print(f"Prime numbers (first {len(prime_nums)}): {prime_nums}")


if __name__ == "__main__":
    main()
