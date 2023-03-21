def main():
    dna1 = input("Enter a DNA sequence: ")
    dna2 = input("Enter a second DNA sequence: ")

    new_dna = ""

    f_dna2 = ""
    f_dna1 = ""

    for char in range(len(dna2)):
        if dna2[char] == "A" or dna2[char] == "C" or dna2[char] == "T" or dna2[char] == "G":
            f_dna2 += dna2[char]
            continue
        else:
            print("OOPS! Unwanted character in 2nd sequence", dna2[char])

    both_dna = len(dna1) + len(f_dna2)

    if len(dna1) < len(f_dna2):
        shorter = dna1
        longer = f_dna2
    else:
        shorter = f_dna2
        longer = dna1

    count_longer = 0
    count_shorter = 0

    for i in range(both_dna + 1):
        if i % 2 == 0:
            new_dna += longer[count_longer]
            count_longer += 1
        else:
            if len(shorter) > count_shorter:
                new_dna += shorter[count_shorter]
                count_shorter += 1
            else:
                continue

    print(new_dna)

    newNewStr = ""

    for character in range(len(new_dna)):
        if character == "A":
            newNewStr += "T"
        elif character == "C":
            newNewStr += "G"
        elif character == "T":
            newNewStr += "A"
        elif newNewStr == "G":
            newNewStr += "C"

    print(newNewStr)


main()
