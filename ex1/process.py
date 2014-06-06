def main():
    my_file = open("log.txt")
    for line in my_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print line

if __name__ == "__main__":
    main()
