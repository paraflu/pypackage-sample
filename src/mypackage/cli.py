
import argparse

from mypackage.module.lib import module_print

def main():
    parser = argparse.ArgumentParser(description="Descr")
    parser.add_argument("-l", help='Some help')

    args = parser.parse_args()
    print(f"main.py {args.l}")
    module_print()

if __name__ == "__main__":
    main()