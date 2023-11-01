import pandas as pd
import numpy as np
import time

# Creating a dictionary with the cities as keys and their file locations as values
CITY_DATA = {
    'chicago': 'D:\\Bike-Share\\chicago.csv',
    'new york city': 'D:\\Bike-Share\\new_york_city.csv',
    'washington': 'D:\\Bike-Share\\washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.
    args: none
    Returns:
        str (city): - name of the city to analyze
        str (month): - name of the month to filter by, or "all" to apply no month filter
        str (day): - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print(f"Hello! Let's explore some US bikeshare data!")
    # Get user input for city (chicago, new york city, washington).
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWelcome!")
        print("\nWhich City Do You Want to Explore?")
        print("1. Chicago\n2. New York City\n3. Washington")
        print("City Name is NOT case sensitive")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nPlease check your input and use the correct format.")
            print("Let's try again...")

    print(f"\nLet's explore {city.title()}!")

    # Get user input for month (all, january, february, ..., june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month, between January to June, that you would like to see:")
        print("Accepted input:")
        print("Full month name; not case sensitive (e.g. january or JANUARY).")
        print("Full month name in title case (e.g. April).")
        print("(If you wish to view data for all months, please type 'all' or 'All' or 'ALL'.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("Restarting...")

    print(f"\nGreat! Let's explore data for {month.title()} month(s).")

    # Get user input for day of the week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in DAY_DATA:
        print("\nPlease select the day of the week, from Monday to Sunday, that you would like to explore.")
        print("You can also select 'all' to view all the days of the week.")
        print("The Day field is NOT case sensitive, so MONDAY and monday are the same.")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nPlease check your input and use the correct format.")
            print("Let's try again...")

    print(f"\nGreat! Now, let's explore data for {city.upper()}")
    print(f"In the month of {month.upper()}")
    print(f"And for the following day(s): {day.upper()}")

    print('-' * 40)
    return city, month, day

# Rest of your code remains unchanged.
# ...

if __name__ == "__main__":
    main()
