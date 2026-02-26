from sys import exit
from readwrite_lib import Rfid
from app_vars import AppVariables

def main():
    print("\nRead/Write tool for RC522")
    while True:
        mode = getOption()
        if mode == 0:
            print("Good bye!")
            exit()
        elif mode == 1:
            Rfid.read()
        elif mode == 2:
            Rfid.write()
        elif mode == 3:
            Rfid.writeIdRange()
        else:
            print("Something wrong. Reboot app.")
            exit(-1)

def printMenu():
    print("""
Choose option:
1 - Read RFID card
2 - Write to RFID card
3 - Write ID range
0 - Exit
""")

def getOption() -> int:
    while True:
        printMenu()
        choice = input("Your choice: ").strip()
        try:
            choice = int(choice)
            if choice not in range(4):
                print("Invalid option! Try again...")
            else:
                return choice
        except ValueError:
            print("Your input is not a number! Try again...")

if __name__ == "__main__":
    main()