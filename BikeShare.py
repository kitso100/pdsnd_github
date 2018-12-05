import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = str(input('enter city chicago, washington or new york city: '))
        if city.lower() == 'chicago':
            city = city.lower()
            break
        elif city.lower() == 'washington':
            city = city.lower()
            break
        elif city.lower() == 'new york city':
            city = city.lower()
            break
        else:
            print('not a valid entry, please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = str(input("enter month(january to june) or 'all' for no filter: "))
        if month.lower() in months:
            month = month.lower()
            break
        else:
            print('invalid entry, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        day = str(input("enter day(monday to sunday) or 'all' for no filter: "))
        if day.lower() in days:
            day = day.lower()
            break
        else:
            print('invalid entry, please try again')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.lower()
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
       Args:
          df - Pandas DataFrame containing city data"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day is:', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is:', most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['journey'] = df['Start Station'] + ' - ' + df['End Station']
    most_frequent_station_combination = df['journey'].mode()[0]
    print('most frequent combination of start and end station is:', most_frequent_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user type counts are:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The gender counts are:\n', gender)
    except KeyError:
        print('no information on gender for washington')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('earliest year of birth is:', earliest)
        most_recent = df['Birth Year'].max()
        print('most recent year of birth is:', most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('most common year of birth is:', most_common)
    except KeyError:
        print('no information on birth year for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze """
    while True:
        city = str(input('enter city chicago, washington or new york city: '))
        if city.lower() == 'chicago':
            city = city.lower()
            break
        elif city.lower() == 'washington':
            city = city.lower()
            break
        elif city.lower() == 'new york city':
            city = city.lower()
            break
        else:
            print('not a valid entry, please try again')
    return city


def get_data():
    """
    Asks user to specify what type of data they want to view

    Returns:
    (str) data - type of data to view i.e. full data or statistics(stats) or first 5 lines of table """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        data = str(input("type 'full data' or 'stats' or 'first lines' to view data: "))
        if data.lower() == 'full data':
            data = data.lower()
            break
        elif data.lower() == 'stats':
            data = data.lower()
            break
        elif data.lower() == 'first lines':
            data = data.lower()
            break
        else:
            print('not a valid entry, please try again')
    return data

def main():
    while True:
        data = get_data()
        if data == 'stats':
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        elif data == 'full data':
            city = get_city()
            df = pd.read_csv(CITY_DATA[city])
            print(df)
        elif data == 'first lines':
            city = get_city()
            df = pd.read_csv(CITY_DATA[city])
            df = df.head()
            print(df)


        restart = input('\nrestart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
