#mathematical operator 
#Union ()


numbers1 = {1,2,3,400}
numbers2 = {400,500,600,700}
union = numbers1 | numbers2
print(union)

#real time
luxury_makeup = {"concealer", "foundation","lipstick","eyeshadow","blush"}
budget_makeup = {"mascara","eyliner","lipstick","blush"}
all_makeup = luxury_makeup | budget_makeup
print(all_makeup)

#intersection()


numbers1 = {1,200,300,400}
numbers2 = {400,500,300,200}
common_number = numbers1 & numbers2
print("common number:", common_number)

#real time
products_a_faetures = {"fast_charging","wireless_charging","waterproof"}
products_b_faetures = {"waterproof","fast_charging","long_battery_life"}
common_proudcts = products_a_faetures & products_b_faetures
print("common proudcts:", common_proudcts)

#difference ()

numbers1 = {1,2,3,400}
numbers2 = {400,500,600,700}
number = numbers1 - numbers2
print(number)

#real time
'''
products_in_stock = {"top","jeans","leggins","kurtis","night suits"}
customer_orders = {"night suits","kurtis","top"}
available_products = products_in_stock - customer_orders
print(available_products)
'''
#symmetric()

numbers1 = {1,2,3,400}
numbers2 = {400,500,600,700}
number = numbers1 ^ numbers2
print(number)

#real time 
"""indian_language = {"Marathi","Hindi","Telugu","English","spain"}
foreign_language = {"English","Franch","spain","japan","china"}
Languages = indian_language ^ foreign_language
print(Languages)
"""
#set comprehension 
list1 = [1,2,3]
list2 = [5,6,4]
pairs = {(a,b) for a in list1 for b in list2}
print(pairs)

grades = [20,90,30,70,50,40]
max_value = max(grades)
min_value = min(grades)
print("maximum value:", max_value)
print("minimum value:", min_value)

#all()
"""
products_in_stock = {"top","jeans","leggins","kurtis","night suits"}
customer_orders = {"night suits","kurtis","top"}
available_products = all(products_in_stock - customer_orders)
print(available_products)"""


#any()

indian_language = {"Marathi","Hindi","Telugu","English","spain"}
foreign_language = {"English","Franch","spain","japan","china"}
Languages = any("indian_language foreign_language")
print(Languages)
