
import argparse, secrets, string

def generate(length, use_symbols=False):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument("--length", "-l", type=int, default=16)
    parser.add_argument("--count", "-n", type=int, default=1)
    parser.add_argument("--symbols", action="store_true")
    args = parser.parse_args()

    for _ in range(args.count):
        print(generate(args.length, args.symbols))
