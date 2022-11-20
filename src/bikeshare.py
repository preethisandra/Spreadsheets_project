import time
import pandas as pd
import numpy as np
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def get_filters():
    
    cities = ['chicago', 'new york city', 'washington']
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    """
     Asks user to specify a city, month, and day to analyze.
     Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Please choose a city : chicago, new york city or washington\n").lower().strip()
    while city not in cities:
        city = input('Invalid city, please select another city\n').lower().strip()
    
    # get user input for month (all, january, february, ... , june)
    
    month = input("Please choose a month from : january through june or select all\n").lower().strip()
    while month not in months:
        month = input('Please select a valid month (january - june)').lower().strip()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Please choose a day of the week: monday - sunday or select all\n").lower().strip()
    while day not in days:
        day = input('Please select a valid day (monday - sunday)').lower().strip()

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
    #load the dataframe based on city

    df = pd.read_csv(CITY_DATA[city])
    
    #convert Start Time to datetime to access hour
   
    df['Start Time'] = pd.to_datetime(df['Start Time'])   
    
    #Extract month and day of the week data to create month and day columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour
    

    #filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
        
    # filter by month to create the new dataframe      
    elif month == 'all':
        df.loc[df['month'].isin(MONTHS)]
        
        
    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    elif day == 'all':
        df.loc[df['day_of_week'].isin(DAYS)]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    popular_month = df['Start Time'].dt.month.mode()[0]
    
    print("The most common month is :", popular_month)
    
    #display the most common day of week
    
    most_common_day_of_the_week = df['day_of_week'].mode()[0]
    print("The most common day of the week :", most_common_day_of_the_week)
    
    # display the most common start hour
   
    most_common_start_hour = df['hour'].mode()[0]
    print(" the most common start hour:", most_common_start_hour)
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is :", most_common_start_station)
    
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common End Station is :", most_common_end_station)
    
    # display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("the most common combination of Start station and End station is:", popular_start_end) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ("the total travel time is :", total_travel_time)
    # display mean travel time
    Average_travel_time = df['Trip Duration'].mean()
    print ("the average travel time is :", Average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print(" the number of user types:", count_user_types) 
    
    # Display counts of gender
    if city != ('washington'):
        count_gender = df['Gender'].value_counts()

        print(" Gender type ", count_gender)
    else:
        print('There is no gender data in the source.')
        
  # Display earliest, most recent, and most common year of birth
    if city != ('washington'):
        earliest_year_of_birth = min(df['Birth Year'])
        most_recent_birth_year  = max(df['Birth Year'])
        most_common_birth_year = df['Birth Year'].mode()
        print("The most recent year of birth:", int(most_recent_birth_year))
        print("The earliest year of Birth :", int(earliest_year_of_birth))       
        print("the most common year of birth:" , int(most_common_birth_year)) 
    else:
        print('There is no Birth Year data in the source.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data(df):
    """ if the user is interested to see the raw data , it can be displayed in rows of 5 at a time"""
    row_count = 0
    # lets the user have an option to view a few rows of raw data from the selected dataframe.
    
    raw_data = input("would you like to see the first five rows of data? yes / no ").lower().strip()
    
    while raw_data =='yes':
        print(df.iloc[row_count:row_count+5])
        row_count += 5
        raw_data = input("would you like to see the next 5 rows of data? yes/no ").lower().strip()
        if raw_data !='yes' :
            break
   
    
    
def main():
    while True:
        city, month, day = get_filters()
        #print(get_filters())
        df = load_data( city , month , day)
        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
             