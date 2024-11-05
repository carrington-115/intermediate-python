def main():
    print('hello world')
    while True:
        try:
            number = int(input("\nWhat is the number?\n"))
        except ValueError:
            print("The value you entered is not an integer")
        else:
            break
    print(f"The number is {number}")
    
if __name__ == "__main__":
    main()