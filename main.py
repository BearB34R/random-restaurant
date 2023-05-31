# The terminal version of the program

restaurants = {}

def add_restaurant():
    name = input("Enter the restaurant's name: ")
    rating = float(input("Enter the restaurant rating: "))
    restaurants[name] = rating
    print(f"{name} with rating {rating} has been added to the dictionary.")

def display_restaurants():
    if not restaurants:
        print("Doesn't exist")
    else:
        print("Restaurants and their rating: ")
        for name, rating in restaurants.items():
            print(f"{name}: {rating}")

def main():
    while True:
        print("\n Please select one of the following")
        print("1. Add a restaurant")
        print("2. Display resaurants")
        print("3.Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_restaurant()
        elif choice == "2":
            display_restaurants()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()