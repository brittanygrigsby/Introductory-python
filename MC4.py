# Mini Challenge 4

product_list = [100,200,300,400,500]

def get_total(flist):
    total=0
    for product in flist:
        total=total+product
    return total
    
def get_average(ftotal,flength):
    return ftotal/flength

total = get_total(product_list)
avg = get_average(total, len(product_list))


print(f"The total is: {total}")
print(f"The average is:{avg}")

