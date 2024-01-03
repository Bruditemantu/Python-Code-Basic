def runCustomerSimulation(n, seq):
    occupied = set()  
    customers_without_computer = 0

    for customer in seq:
        if customer in occupied:  
            occupied.remove(customer)
        else: 
            if len(occupied) < n:  
                occupied.add(customer)
            else:  
                customers_without_computer += 1

    return customers_without_computer


n = 3
seq = " GACCBDDBAGEE"
result = runCustomerSimulation(n, seq)
print("Number of customers who could not get a computer:", result)
