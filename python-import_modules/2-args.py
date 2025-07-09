#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    count = len(args)
    plural = "s" if count != 1 else ""
    end_char = ":" if count > 0 else "."
    print(f"{count} argument{plural}{end_char}")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()