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

    print('*'*80)
    print('\n\n\nHello! Let\'s explore some US bikeshare data!\n\n\n')
    print('*'*80)


    # Make loop to account for user input mistakes
    while True:

        # Get user input for the city
        print('\nCITY: Which city do you want to see data for: Chicago, \
New York City or Washington?')
        city = input('\nEnter the name of the city: ').lower()

        # Make a list of available cities
        cities = ['chicago','new york city', 'washington']

        # Print error if user input is not in the list
        if city not in cities:
            print('\n\n\nERROR: Data for {} is NOT available. Please check your \
spelling or choose one of the available cities.\n\n\n'.format(city))
        else:
            # Break the loop if user input is in the list
            break

    print('*'*80)


    # Make loop to account for user input mistakes
    while True:

        # Get user input for month
        print('\nMONTH: What month would you like to see data for?')
        print('\nAvailable months:\n\nJanuary\nFebruary\nMarch\nApril\nMay\nJune')
        print('\n(If you want to see data for all available months, please enter \'all\'.)')
        month = input('\nEnter the name of the month: ').lower()

        # Make list of available months
        months = ['january', 'february', 'march', 'april', 'may', 'june','all', '\'all\'']

        # Print error if user input is not in the months list
        if month not in months:
            print('\n\n\nERROR: Data for {} is NOT available! Please check \
your spelling or choose one of the available months.\n\n\n'.format(month))
        else:
            # Break the loop if the user input is in the months list
            break

    print('*'*80)


    # Make loop to account for mistakes in user input
    while True:

        # Get user input for the day of the week
        print('\nDAY: What day in the week would you like to see the data for?')
        print('\n\n(If you want to see the data for all days, please enter \'all\'.)')
        day = input('\n\nEnter the day of the week: ').lower()

        # Make a list of available days
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

        # Print error if user input is not in the days list
        if day not in days:
            print('\n\n\nERROR: That\'s NOT a valid day. Please enter the day one more time.\n\n\n')
        else:
            # Break the loop if user input is in the days list
            break


    print('*'*80, '\n\n\n')
    print('Let\'s look at some bike sharing statistics for {} (month: {}, day: {}).'.\
format(city.title(), month.title(), day.title()))
    print('\n\n\n', '*'*80, '\n')


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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time and create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # If applicable, filter by month
    if month != 'all':

        # Use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create a new dataframe
        df = df[df['month'] == month]

    # If applicable, filter by day
    if day != 'all':

        # Use the index of the day list to get the corresponding integer
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)

        # Filter by day to create a new dataframe
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Save current time to calculate process duration later
    start_time = time.time()


    # Find the most popular month
    popular_month = df['month'].mode()[0]
    # Make dictionary to store and access string values of months
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print('\nThe most popular month for bicycle renting was {}.'.format\
(months[popular_month]))


    # Find the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    # Make dictionary to store and access string values of days of week
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',\
5: 'Saturday', 6: 'Sunday'}
    print('\nThe most popular day of the week for bicycle renting was \
{}.'.format(days[popular_day]))


    # Make new column for hour
    df['hour'] = df['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # Make dictionary to store and access string values of hours
    hours = {0: '12am', 1: '1am', 2: '2am', 3: '3am', 4: '4am', 5: '5am', 6: '6am',\
7: '7am', 8: '8am', 9: '9am', 10: '10am', 11: '11am', 12: '12pm', 13: '1pm',\
14: '2pm', 15: '3pm', 16: '4pm', 17: '5pm', 18: '6pm', 19: '7pm', 20: '8pm',\
21: '9pm', 22: '10pm', 23: '11pm'}
    print('\nThe most popular hour for bicycle renting was {}.\n'.format(hours[popular_hour]))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def time_stats_mfilter(df):
    """Displays statistics on the most frequent times of travel without the\
     most popular month when data is filtered by month."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Save current time to calculate process duration later
    start_time = time.time()

    # Find the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    # Make dictionary to store and access string values of days of week
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',\
5: 'Saturday', 6: 'Sunday'}
    print('\nThe most popular day of the week for bicycle renting was \
{}.'.format(days[popular_day]))


    # Make new column for hour
    df['hour'] = df['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # Make dictionary to store and access string values of hours
    hours = {0: '12am', 1: '1am', 2: '2am', 3: '3am', 4: '4am', 5: '5am', 6: '6am',\
7: '7am', 8: '8am', 9: '9am', 10: '10am', 11: '11am', 12: '12pm', 13: '1pm',\
14: '2pm', 15: '3pm', 16: '4pm', 17: '5pm', 18: '6pm', 19: '7pm', 20: '8pm',\
21: '9pm', 22: '10pm', 23: '11pm'}
    print('\nThe most popular hour for bicycle renting was {}.\n'.format(hours[popular_hour]))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def time_stats_dfilter(df):
    """Displays statistics on the most frequent times of travel without the \
    most popular day of week when data is filtered by day."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Save current time to calculate process duration later
    start_time = time.time()


    # Find the most popular month
    popular_month = df['month'].mode()[0]
    # Make dictionary to store and access string values of months
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print('\nThe most popular month for bicycle renting was {}.'.format\
(months[popular_month]))


    # Make new column for hour
    df['hour'] = df['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # Make dictionary to store and access string values of hours
    hours = {0: '12am', 1: '1am', 2: '2am', 3: '3am', 4: '4am', 5: '5am', 6: '6am',\
7: '7am', 8: '8am', 9: '9am', 10: '10am', 11: '11am', 12: '12pm', 13: '1pm',\
14: '2pm', 15: '3pm', 16: '4pm', 17: '5pm', 18: '6pm', 19: '7pm', 20: '8pm',\
21: '9pm', 22: '10pm', 23: '11pm'}
    print('\nThe most popular hour for bicycle renting was {}.\n'.format(hours[popular_hour]))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_stats_mdfilter(df):
    """Displays statistics on the most frequent times of travel without the\
    most popular month and the most popular day when data is filtered by both \
    month and day."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Save current time to calculate process duration later
    start_time = time.time()


    # Make a new column for hour
    df['hour'] = df['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # Make dictionary to store and access string values of hours
    hours = {0: '12am', 1: '1am', 2: '2am', 3: '3am', 4: '4am', 5: '5am', 6: '6am',\
7: '7am', 8: '8am', 9: '9am', 10: '10am', 11: '11am', 12: '12pm', 13: '1pm',\
14: '2pm', 15: '3pm', 16: '4pm', 17: '5pm', 18: '6pm', 19: '7pm', 20: '8pm',\
21: '9pm', 22: '10pm', 23: '11pm'}
    print('\nThe most popular hour for bicycle renting was {}.\n'.format(hours[popular_hour]))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    #Save current time to calculate process duration later
    start_time = time.time()

    # Find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station was {}.'.format(popular_start_station))

    # Find the most popular end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station was {}.'.format(popular_end_station))

    # Make a new column 'Trip' by combining start and end station
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']
    #Find the most popular trip
    popular_trip = df['Trip'].mode()[0]
    print('\nThe most popular trip was {}.\n'.format(popular_trip))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # Save current time to calculate process duration later
    start_time = time.time()

    # Find total travel time
    total_time = df['Trip Duration'].sum()
    print('\nTotal travel time for the chosen city and period was {} hours.'.format(total_time/3600))

    # Find average travel time
    mean_time = df['Trip Duration'].mean()
    print ('\nThe average duration of the trip was {} hours.\n'.format(mean_time/3600))


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # Save current time to calculate process duration later
    start_time = time.time()

    # Find and display the number of each user type
    users_count = df['User Type'].value_counts()
    print('\nThe number of users was:\n', users_count.to_string())


    # Check if there is data about gender
    if 'Gender' in df.columns:
        # If there is, find and display gender count
        users_gender = df['Gender'].value_counts()
        print('\nThe gender of users was:\n', users_gender.to_string())
    else:
        # If no data, print a notification
        print('There is no information about gender.')


    # Check if there is data about birth year
    if 'Birth Year' in df.columns:
        # If there is data, find and display the earliest birth year
        min_year = int(df['Birth Year'].min())
        print('\nThe oldest user was born in {}.'.format(min_year))
        # If there is data, find and display the latest birth year
        max_year = int(df['Birth Year'].max())
        print('\nThe youngest user was born in {}.'.format(max_year))
        # If there is data, find the most common birth year
        mode_year = int(df['Birth Year'].mode()[0])
        print('\nThe majority of users were born in {}.\n'.format(mode_year))
    else:
        # If not data, print a notification
        print('There is no information about birth year.')


    # Calculate process duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():

    # Make a loop for restart option
    while True:
        # Get city, month and day specifications from user
        city, month, day = get_filters()
        # Load data
        df = load_data(city, month, day)

        # Depending whether there is filtering by day and/or month, calculate time stats
        if month == 'all' and day == 'all':
            time_stats(df)
        elif month != 'all' and day == 'all':
            time_stats_mfilter(df)
        elif month == 'all' and day != 'all':
            time_stats_dfilter(df)
        else:
            time_stats_mdfilter(df)
        # Calculate station statistics
        station_stats(df)
        # Calculate trip duration statistics
        trip_duration_stats(df)
        # Calculate statistics about users
        user_stats(df)


        # Get user input whether they want to see a snippet of raw data
        view_data = input('\nWould you like to view 5 rows of trip data? Enter yes or no: \n').lower()
        # Set start index for selecting data rows
        start_loc = 0
        # Make a loop to continue asking for input until user says 'no'
        while view_data == 'yes':
            # Select and display 5 rows of the data
            print(df.iloc[start_loc:start_loc + 5])
            # Change index for data selection to get next 5 rows
            start_loc += 5
            # Question to be repeated until user says 'no'
            view_data = input('\n\nDo you wish to see more data? Enter yes or no: ').lower()


        # Get user input whether they want a restart
        restart = input('\n\nWould you like to restart? Enter yes or no.\n')
        # If user wants restart, start again
        if restart.lower() != 'yes':
            # If user doesn't want input, break the loop
            break

if __name__ == "__main__":
    main()
