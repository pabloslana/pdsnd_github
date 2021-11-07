import time
import pandas as pd
import numpy as np

"""used the template with helper code provided here in the workspace"""

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
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    list_cities = ['chicago', 'new york city', 'washington']
    city = None
    
    while city not in list_cities:
        city = input("Enter one of these following cities: chicago, new york city, washington. Use lowercase.\nResponse:   ")
        city = city.lower()
    print()
    print('You choose:',city)
    print()
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    list_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = None
    
    """Checking if the month select is in the list, if not, user must type again"""
    
    while month not in list_months:
        month = input("Choose all or one of the months from january to june. Type 'all' to get all months or just type the corresponding month. Use lowercase. \nResponse:   ")
        month = month.lower()
        
    print()
    print('You choose:',month)
    print()
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    list_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = None
    
    while day not in list_days:
        day = input("Choose all or one of the days from monday to sunday. Type 'all' to get all days or just type the corresponding day. Use lowercase. \nResponse:   ")
        day = day.lower()
        
    print()
    print('You choose:',day)

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
    #loading file
    df = pd.read_csv(CITY_DATA[city])
    
    #converting "start time" column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #converting "end time" column to datetime type
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #creating new column according to month
    df['month'] = df['Start Time'].dt.month
    
    #creating new column according to hour
    df['hour'] = df['Start Time'].dt.hour
    
    #creating new column combination of stations
    df['combination'] = df[['Start Station', 'End Station']].agg('-'.join, axis=1)
    
    #creating new column travel time in hours
    """part documented in the readme.txt, point (1) """
    df['travel_time'] = (df['End Time'] - df['Start Time']).astype('timedelta64[h]')
    
    #creating new column according to day of the week
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month, using the same template from the exercise part 3
    """part documented in the readme.txt, point (3) """
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filtering by the choosen month
        df = df[df.month == month]

    # # filter by day of the week, using the same template from the exercise part 3
    if day != 'all':
        # filtering by the choosen day of the week
        df = df[df.day_of_week == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month: {}".format(common_month))
    print()
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of the week: {}".format(common_day))
    print()
    
    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].mode()[0]
    print("Most common start time: {}".format(common_start_hour))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_s_station = df['Start Station'].mode()[0]
    print("Most common start station: {}".format(common_s_station))
    print()

    # TO DO: display most commonly used end station
    common_e_station = df['End Station'].mode()[0]
    print("Most common end station: {}".format(common_e_station))
    print()

    # TO DO: display most frequent combination of start station and end station trip

    combination = df['combination'].mode()[0]
    print("Most common combination: {}".format(combination))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    travel_t = df['travel_time'].sum()
    print("Total travel time: {}".format(travel_t))
    print()

    # TO DO: display mean travel time
    
    travel_mean = df['travel_time'].mean()
    print("Mean travel time: {}".format(travel_mean))
    print()
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("User types as following: \n{}".format(user_types))
    print()
    
    # TO DO: Display counts of gender
    """Checking if "Gender" exists as a column in the selected dataframe"""
    """part documented in the readme.txt, point (2) """
    
    if 'Gender' not in df:
        user_genders = 'No gender stats available for this city'
        print("User gender stats as following: \n{}".format(user_genders))
        print()
    else:
        user_genders = df['Gender'].value_counts()
        print("User gender stats as following: \n{}".format(user_genders))
        print()

    # TO DO: Display earliest, most recent, and most common year of birth
  
    """Checking if "Birth Year" exists as a column in the selected dataframe"""
    """part documented in the readme.txt, point (2) """
    
    if 'Birth Year' not in df:
        no_birth_data = 'No birth year stats available for this city'
        print("User birth year stats as following: \n{}".format(no_birth_data))
        print()
    else:
         earliest = df['Birth Year'].min()
         print("Earliest year of birth: {}".format(earliest))
         print()
    
         recent = df['Birth Year'].max()
         print("Recent year of birth: {}".format(recent))
         print()   

         common = df['Birth Year'].mode()[0]
         print("Common year of birth: {}".format(common))
         print() 

         print("\nThis took %s seconds." % (time.time() - start_time))
         print('-'*40)

      
def chunker(df, size):
    """Displays raw data from the dataframe used in the iteration."""
    """part documented in the readme.txt, point (4) """
    
    answer = input('would you like to see raw data from the dataframe used for the calculations? (type "yes" or "no") \n Response:   ')
    i = 0
    while i <= len(df) and answer != 'no':
        print(df[i:i + size])
        answer = input('would you like to see more raw data from the dataframe used for the calculations? (type "yes" or "no") \n Response:   ')
        i+=5   
        
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        chunker(df,5)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
