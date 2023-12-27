#Shopping cart program
print("       WELCOME TO MEMON'S FAST FOOD ")
name=input('Enter your name :')
print(name)
items = {'Burger':400, 'Pizza': 500, 'Broast': 450, 'Roll' : 250}
foods=[]
total=0
items['Burger']

while True:
    food=input('Enter the Item (Burger, Pizza, Broast, Roll) to buy (q to quit) :')

    if food.lower()=='q':
        break
    food = food.capitalize()
    if not food in items:
        print("Item not Found")
    else:
        foods.append(food)
        total += items[food]


print('-----YOUR CART-----')
for i in range(len(foods)) :
    if i == 0:
        print("Items\t\tPrice")
    print(f'{foods[i]}\t\t{items[foods[i]]}')


print(name.upper() + f' Your total is : Rs{total}')