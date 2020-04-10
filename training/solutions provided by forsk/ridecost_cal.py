"""
Name: 
    Ride Cost Calculator         
Filename:
    ridecost_cal.py
Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office.
    Take the distance travelled, cost of diesel and Fuel Average from input 
Hint:    
    fuel_consumption = (travelling_km / vehicle_fuel_avg)
    cost_per_day = (diesel_cost * fuel_consumption)
"""
 
# Daily travelling kilometers
travelling_km = float(input("Enter the kilometers you travel in a day > "))
 
# Diesel cost
diesel_cost = float(input("Enter the cost of Petrol/Diesel > "))
 
# Vehicle fuel average
vehicle_fuel_avg = float(input("Enter the Vehicle Average > "))
 
# Fuel you want during travelling
fuel_consumption = (travelling_km/vehicle_fuel_avg)
print("Fuel Consumed in a day = " + str(round(fuel_consumption,2)) + " Litre" )
 

# cost of driving per day to office
cost_per_day = (diesel_cost*fuel_consumption)
print ("Cost of driving per day to office is :"+str(round(cost_per_day,2))+" INR")