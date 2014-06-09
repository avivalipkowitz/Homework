def main():    
    melon_cost = 1.00

    debtors = []

    my_file = open("customer_orders.csv")
    
    for line in my_file:
        # line = line.rstrip()
        token = line.split(",")
	
        customer_name = token[1]
        melons_received = int(token[2])
        customer_paid = float(token[3])
        customer_charged = melon_cost * melons_received
        customer_owes = customer_charged - customer_paid

        if customer_owes > 0:
            debtors.append(customer_name)
       
    
    print debtors
    debtors

 
    


if __name__ == "__main__":
    main()

    

