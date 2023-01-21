import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'C:/Users/hazem/PycharmProjects/chicago.csv',
              'new york city': 'C:/Users/hazem/PycharmProjects/new_york_city.csv',
              'washington': 'C:/Users/hazem/PycharmProjects/washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').title()
        if city in ['Chicago', 'New York City', 'Washington']:
            break
        else:
            print('invalid input! try again')
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month - January, February, March, April, May, June, or All?').title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
            break
        else:
            print('invalid input! try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('(Which day - Friday, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or All?').title()
        if day in ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'All']:
            break
        else:
            print('invalid input! try again')

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
    listOfMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    m = listOfMonths.index(month) + 1
    filename = CITY_DATA[city.lower()]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    if m != 7:
        df = df[df['month'] == int(m)]
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    listOfMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    m = listOfMonths[int(df['month'].mode() - 1)]
    print('The Most Common Month: ' + str(m))

    # display the most common day of week
    print('The Most Common Day: ' + str(df['day'].mode()[0]))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    print('The Most Common Hour: ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The Most Common Start Station: ' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The Most Common End Station: ' + str(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The Most Common Trip From Start To End : ' + str((df['Start Station'] + ' to ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time: ' + str(df['Trip Duration'].sum()))

    # display mean travel time
    print('Avarage Travel Time: ' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest Year Of Birth: ' + str(df['Birth Year'].max()))
        print('Most Recent Year Of Birth: ' + str(df['Birth Year'].min()))
        print('Most Common Year Of Birth: ' + str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    df = pd.read_csv(CITY_DATA[city.lower()])
    check = input('Would you like to display 5 raws of data type "yes" if need and "no" to terminate: ').lower()
    i = 0
    while check == 'yes':
        if i >= df.shape[0]:
            break
        print(df.iloc[i:i+5])
        check = input('Would you like to display 5 raws of data type "yes" if need and "no" to terminate: ').lower()
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes to restart other to terminate.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
