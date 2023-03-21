def main():
    base = input("Please enter a positive integer to be the base: ")
    pos_int = False

    while pos_int == False:
        if "." not in base and int(base) >= 0:
            pos_int = True
            print("positive integer probably")



        else:
            print("not a positive integer probably")
            base = input("Please enter a positive integer to be the base: ")

main()