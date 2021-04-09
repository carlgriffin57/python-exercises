# Exercise #1
# Write the code to take a string and produce a dictionary out of that string 
truck = "toyota tacoma"
make = truck.split()[0]
model = truck.split()[1]
makemodel = {
    'make' : make,
    'model' : model
}
print(makemodel)

# Exercise #2
# Write the code that takes a dictionary containing make/model for a vehicle and 
# capitalizes the first character of the make and the model:
truck = "toyota tacoma"
make = truck.split()[0]
model = truck.split()[1]
make = make.capitalize()
model = model.capitalize()
makemodel = {
    'make' : make,
    'model' : model
}
print(makemodel)

# Exercise #3
# Create a list of 3 dictionaries where each dictionary represents a vehicle, as above Write the code that operates 
# on that list of dictionaries in order to uppercase the entire make and model values.
vehicles = [
    {
    'make' : 'ford',
    'model' : 'mustang'
    },
    {
    'make' : 'toyota',
    'model' : 'tacoma'
    },
    {
    'make' : 'nissan',
    'model' : 'sentra'
    }
]
for vehicle in vehicles:
    vehicle['make'] = vehicle['make'].upper()
    vehicle['model'] = vehicle['model'].upper()
print(vehicles)

