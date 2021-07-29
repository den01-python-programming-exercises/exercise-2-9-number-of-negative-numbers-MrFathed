def main():
    #write your code below this line
    neg_count = 0

    while True:
        number = int(input("Give a number:"))

        if number == 0:
            break

        if number < 0:
            neg_count += 1

if __name__ == '__main__':
    main()
