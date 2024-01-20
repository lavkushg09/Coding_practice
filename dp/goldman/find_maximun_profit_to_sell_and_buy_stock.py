stock_p=[100,180,260,310,40,535,695]

def find_max_price(stock_p, index):
    # if index == len(stock_p) - 1:
    profit = 0
    last_minimum = stock_p[0]
    last_maxima=stock_p[0]
    index = 0
    while index < len(stock_p):
        if last_minimum < stock_p[index] < stock_p[index+1]:
            last_minimum=stock_p[index]



        if stock_p[index] <= last_minimum and index < len(stock_p)-1:
            profit = profit + stock_p[index-1]-last_minimum
            last_minimum = stock_p[index]
        else:
            profit += last_minimum - stock_p[index]
            last_minimum = stock_p[index]
