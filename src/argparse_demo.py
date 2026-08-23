import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("language")

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed information"
)

args = parser.parse_args()

print(f"hello, {args.name}!")
print(f"you are learning {args.language}")

if args.verbose:
    print("Verbose mode is enabled.")
    print("This program received all required arguments successfully")