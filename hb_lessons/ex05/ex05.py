def main():

    input_file = raw_input("What file would you like to count? ")

    myfile = open(input_file)

    def count_char():    
        char_list = []
        i=1
        for char in myfile:
            char = myfile.read(i)
            char_list.append(char)
            i += 1
            return char_list

    characterlist = count_char()
    print characterlist

if __name__ == "__main__":
    main()
