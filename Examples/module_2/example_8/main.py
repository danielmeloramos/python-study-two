#1- flags com argparse

import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Files Reader")
    parser.add_argument("--file", type=str, help="Inform a file to read")
    parser.add_argument("--greeting", action="store_true", help="Prints the greeting message")

    args = parser.parse_args()
    if args.greeting:
        print("Hello!!!!")
    print(f"Received the file name: {args.file}")