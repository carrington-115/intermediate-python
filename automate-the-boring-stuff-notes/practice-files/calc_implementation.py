def main():
    print('hello world')
    try:
        number = int(input("\nWhat is the number?\n"))
        print(f"The number is {number}")
    except ValueError:
        print("The value you entered is not an integer")

if __name__ == "__main__":
    main()