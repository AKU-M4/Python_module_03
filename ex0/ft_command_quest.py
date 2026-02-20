from sys import argv

def main():
    print("=== Command Quest ===")
    av_len = len(argv)
    if av_len == 1:
        print("No arguments provided!")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {len(argv) - 1}")
        i = 1
        for p in argv[1:]:
            print(f"Argument {i}: {p}")
            i += 1
        print(f"Total arguments: {av_len}")
        

if __name__ == "__main__":
    main()
