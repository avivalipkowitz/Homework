"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def main():
    salespeople = []
    melons_sold = []

    sales_report_dict = {}

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]      
        melons = int(entries[2])

        sales_report_dict[salesperson] = melons

    print sales_report_dict
    return sales_report_dict




if __name__ == "__main__":
    main()

sales_report = main()

sales_report



