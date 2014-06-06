def main():

	def melon_report_output(inventory_file):
		my_file = open(inventory_file)

   		for line in my_file:
			line.upper()
			line = line.rstrip()
        	words = line.split(',')
        
        	melon = words[0]
        	count = words[1]
        	amount = words[2]
        
        	print "Delivered %s %ss for a total of: $%s" % (words[1], melon, amount)
 
    	print "\n",
	
    # Day 1
	print "Day 1"
	melon_report_output("um-deliveries-20140519.csv")


	# Day 2
	print "Day 2"
	my_file = open("um-deliveries-20140520.csv")

	for line in my_file:
	    line = line.rstrip()
	    words = line.split(',')
        
	    melon = words[0]
	    count = words[1]
	    amount = words[2]
        
    	print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    
	my_file.close()
	print "\n",

	# Day 3
	print "Day 3"
	my_file = open("um-deliveries-20140521.csv")

	for line in my_file:
	    line = line.rstrip()
	    words = line.split(',')
	  
        
	    melon = words[0]
	    count = words[1]
	    amount = words[2]
	    
	   
        
	    print "Delivered %s %ss for a total of: $%s" % (count, melon.upper, amount)
	my_file.close()
	print "\n",

if __name__ == "__main__":
    main()
