import time
import pandas as pd
import numpy as np

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Please choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city.")

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (january to june) or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")

    # Get user input for day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of the week or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day or 'all'.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day, and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month}")

    # Most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day}")

    # Most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most common start station
    start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {start_station}")

    # Most common end station
    end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {end_station}")

    # Most frequent combination of start and end station
    df['trip'] = df['Start Station'] + " → " + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"Most common trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"Total travel time: {total_duration} seconds")

    # Mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_duration:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data upon request in chunks of 5 rows."""
    i = 0
    show_data = input("\nWould you like to view 5 rows of raw data? Enter yes or no: ").lower()
    
    while show_data == 'yes':
        if i >= len(df):
            print("No more data to display.")
            break
        print(df.iloc[i:i+5])
        i += 5
        show_data = input("\nWould you like to view 5 more rows of raw data? Enter yes or no: ").lower()



def name()
    print ("her name rana")


def printinfo()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()


