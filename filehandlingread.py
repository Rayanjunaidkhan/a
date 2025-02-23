order = str(input("what is your order? "))

file = open("orders.txt","w")
file.write(order)
file.close()

menu = ["weshi burger \n","gochu wings \n","nugg wrap \n","next cola \n"]
file = open("orders.txt","w")
file.writelines(menu)
file.close()

