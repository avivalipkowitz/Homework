melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

def count_the_melons(): 
    f = open("orders_by_type.csv")
    
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    return melon_tallies
    

def total_the_revenues():
    f = open("orders_by_type.csv")
    total_revenue = 0
        
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
    f.close()
    print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

def compare_sales_methods():

    f = open("orders_with_sales.csv")
        
    saletype = [0, 0]
    
    for line in f:
        data = line.split(",")
        if data[1] == "0":
            saletype[0] += float(data[3])
        else:
            saletype[1] += float(data[3])

    internet_sales = saletype[0] 
    salespeople = saletype[1]
    
    print "Salespeople generated %0.2f in revenue." % internet_sales
    print "Internet sales generated %0.2f in revenue." % salespeople
    
    if salespeople > internet_sales:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

    f.close()

def main():
    
    count_the_melons()
    total_the_revenues()
    compare_sales_methods()
    


if __name__ == "__main__":
    main()
