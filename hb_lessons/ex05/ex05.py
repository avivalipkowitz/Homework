def main():

    input_file = raw_input("What file would you like to count? ")

    myfile = open(input_file)
    filetext = myfile.read()
    textlist = [filetext]
    print textlist


    char_list = []
    def create_charlist(filetext):    
        for char in filetext:
            char_list.append(char)
            print char_list
            return char_list

    characterlist = create_charlist(filetext)
    print "This is characterlist: "
    print characterlist


    print "This is char_list: "
    print char_list
    myfile.close()
    
    

if __name__ == "__main__":
    main()