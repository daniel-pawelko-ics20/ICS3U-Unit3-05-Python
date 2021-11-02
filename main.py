#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program will convert number to month


def main():
    # This function inputs integer and outputs month equivalent
    # input
    integer = int(input("Enter number of a month(ex: 3 for March): "))

    # process/output
    if integer == 1:
        print(f"January")
    elif integer == 2:
        print(f"February")
    elif integer == 3:
        print(f"March")
    elif integer == 4:
        print(f"April")
    elif integer == 5:
        print(f"May")
    elif integer == 6:
        print(f"June")
    elif integer == 7:
        print(f"July")
    elif integer == 8:
        print(f"August")
    elif integer == 9:
        print(f"September")
    elif integer == 10:
        print(f"October")
    elif integer == 11:
        print(f"November")
    elif integer == 12:
        print(f"December")
    else:
        print("Not a valid month number")

    # output finished
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
