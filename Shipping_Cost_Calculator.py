#Shipping Cost Calculator 

##Input package weight and shipping rate
weight = float(input("Enter the package weight in kilogrammes:"))
rate = float(input("Enter the shipping rate per kilogrammes:"))

##Calculate shipping cost
shipping_cost= weight*rate

##Display the result
print(f"Shipping Cost:{shipping_cost}USD")