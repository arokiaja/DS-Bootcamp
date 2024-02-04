"Program to calculate the cost of a holiday expenditure for an user."

"Getting user input of the flight."

while True:
    print(" 1 - London\n 2 - Birmingham\n 3 - Edinburgh\n 4 - Belfast")
    try:  #Checking for Numbers only input.
        city_flight = int(input("\nSelect the city you want to fly to "
                                "(Enter the number of your choice): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if city_flight <1 or city_flight >4:  # Check inputs are only between 
                                          # 1 and 4 included.
        print("Wrong city selection, try again")
    
    else:
        break

"Getting user input of the hotel stay duration."
while True:
    try:  # Check if only Numbers are entered.
        num_nights = int(input("\nEnter the number of nights at hotel: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if num_nights <1:  # Checking for only positive integer inputs.
        print("Wrong input, try again. Enter 1 or more than 1 night")
    
    else:
        break   

"Getting user input for car rental duration."
while True:
    try:  #Checking for Numbers only input.
        rental_days = int(input("\nEnter the number of days of car rental: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if rental_days <1:  # Checking for only positive integer inputs.
        print("Wrong input, try again. Enter 1 or more than 1 day")
    
    else:
        break   

city_selection = {
    1 : 'London',
    2 : 'Birmingham',
    3 : 'Edinburgh',
    4 : 'Belfast'
}
price_per_night = 100
rental_price_per_day = 25

def hotel_cost(x):  # A function to calculate the total hotel cost.
    hotel_cost = x * price_per_night
    return hotel_cost
    
def plane_cost(x):  # A function to calculate the total flight cost.
    if city_flight == 1:
        plane_cost = 50
            
    elif city_flight == 2:
        plane_cost = 40
            
    elif city_flight == 3:
        plane_cost = 60
            
    else:
        plane_cost = 70
        
    return plane_cost

def car_rental(x):  # A function to calculate the total car rental cost.
    car_rental = x * rental_price_per_day
    return car_rental

def holiday_cost(x, y, z):  # A function to calculate total holiday cost.
    holiday_cost = x + y + z
    return holiday_cost

print("\n***************************************************************"
      "******************")
print(f"\nYour flight is booked for {city_selection[city_flight]} and the "
      f"flight cost is £{plane_cost(city_flight)}.")
print(f"\nYour stay there at a hotel is for {num_nights} nights for the "
      f"price of {hotel_cost(num_nights)} (£{price_per_night} per night).")
print(f"\nYour car is rented for {rental_days} days, for the price of "
      f"£{car_rental(rental_days)} (£{rental_price_per_day} per day).")
total_cost = holiday_cost(
    plane_cost(city_flight),
    hotel_cost(num_nights),
    car_rental(rental_days)
    )
print(f"\nAnd your total cost of this holiday is £{total_cost}\n")
print("*****************************************************************"
      "****************\n")