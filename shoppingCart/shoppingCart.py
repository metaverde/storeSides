#https://www.youtube.com/watch?v=kbyHLU9JqjE

##I want myPythonStore to respond to misspellings and plurals as well.
##Things are just funelling through to the end...
##
##Passing?
##Breaking?
##Relearning terminology. Thinking about my shortcomings before.
##I'm a lot better equipped now.
##Really enjoying Python atm and thinking about Viper.


foods = []
prices = []
total = 0

###using lists because casnnot append tuple
##not using sets because sets are unordered.

while True:

    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
        break
    
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)

print(10*("*"))


for food in foods:
    print(food, end=" ** ")
    #print("\n")

print("\n") #print() should also work.

for price in prices:
    total += price
    print(price, end=" * ")

print("\n")
print(10*"*", total, 10*"*")
