def print_melon_report(inventory_file):
    my_file = open(inventory_file)

    for line in my_file:
        line.upper()
        line = line.rstrip()
        words = line.split(',')
    
        melon = words[0]
        count = words[1]
        amount = words[2]
    
        print "Delivered %s %ss for a total of: $%s" % (words[1], melon, amount)
    
    my_file.close()
    print "\n",


def main():


	
    # Day 1
	print "Day 1"
	print_melon_report("um-deliveries-20140519.csv")


	# Day 2
	print "Day 2"
	print_melon_report("um-deliveries-20140520.csv")
 
	
	# Day 3
	print "Day 3"
        print_melon_report("um-deliveries-20140521.csv")

	

if __name__ == "__main__":
    main()
