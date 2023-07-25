
def bonAppetit(bill, k, b):
    realBill = int((sum(bill) - bill[k])/2)
    if b == realBill:
        print( "Bon Appetit")
    else:
        return print(b - realBill)
