def main():

    num_input = int(input("Please enter a positive integer: "))
    num_spaces = num_input

    for i in range(num_input+2):
        row_str = ""

        if i == 0 or i == (num_input+1):
            row_str += "+"
            for x0 in range(num_input+1):
                row_str += "-"
            row_str += "+"
        else:
            row_str += "|"
            for numbers in range(i, 0, -1):
                row_str += str(numbers)
            for spaces in range(num_spaces+1, 1, -1):
                row_str += " "
            row_str += "|"
            num_spaces -= 1

        print(row_str)


main()
