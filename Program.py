class Products:
    def __init__(self, name, price,discountQtyAmt):
        self.name = name
        self.price = price
        self.discountQtyAmt = discountQtyAmt
    
        

class ProductBill:
    def __init__(self, name,productList):
        self.name = name
        self.productList=productList

    def processBill(self):
        # A then 50
        # AA then 100
        # AAA then 130
        # AAABB then 175
        product_count={}
        for i in self.name:
            product_exists = any(product.name in [i] for product in self.productList)
            if product_exists and i in product_count: 
                product_count[i]+=1
            elif product_exists:
                product_count[i]=1
        if not product_count:
            print("Product not Found")
        else:
            total_price = 0
            for product_name, count in product_count.items():
                for product in self.productList:
                    if product.name == product_name:
                        if product.discountQtyAmt and 'qty' in product.discountQtyAmt and 'price' in product.discountQtyAmt:
                            # Apply discoun
                            discount_qty = product.discountQtyAmt['qty']
                            discount_price = product.discountQtyAmt['price']
                            while count >= discount_qty:
                                total_price += discount_price
                                count -= discount_qty
                        # Add remaining products at regular price
                        total_price += count * product.price
            print("Total Price:", total_price)




# All Exisiting Product List
productList=[
    Products("A",50,{"qty":3,"price":130}),
    Products("B",30,{"qty":2,"price":45}),
    Products("C",20,None),
    Products("D",15,None),    
]

# Print Product List
def printProductList():
    # Create Product List
    print("\n")
    print("==============All Products============")
    print("NAME       Unit Price    Special Price")
    for product in productList:
        print(product.name,"          ",product.price,"        ",end="")
        if product.discountQtyAmt and 'qty' in product.discountQtyAmt and 'price' in product.discountQtyAmt:
            print("   ",str(product.discountQtyAmt['qty']) + " for " + str(product.discountQtyAmt['price']),end="")
        print("")
    print("\n")

def printMenu():
    print("=============Select Option============")
    print("============ 1. Add New Product ======")
    print("=============2. Buy Product ==========")
    print("============ 3. List Products ========")
    print("============ 4. Exit =================")
    option=int(input("Enter Choice: "))
    return option

option=0
printProductList();
while option!=4:
    option=printMenu()
    if option==3:
        printProductList()
        continue
    if option==1:
        name=input("Enter Product Name: ")
        price=int(input("Enter Product Price: "))
        discountYN=input("Do you want to apply discount? (y/n): ")
        if discountYN=='y':
            discountQtyAmt=int(input("Enter Discount Qty: "))
            discountPrice=int(input("Enter Discount Price: "))
            productList.append(Products(name,price,{"qty":discountQtyAmt,"price":discountPrice}))
        else:
            productList.append(Products(name,price,None))
        printProductList()
    if option==2:
        name=input("Enter Product Name: ")
        bill=ProductBill(name,productList)
        match=bill.processBill()
       