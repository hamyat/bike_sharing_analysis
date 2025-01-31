import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# Load the dataset
data_path = 'bikeshare_hour_clean.csv'
df = pd.read_csv(data_path)

# Convert the 'dteday' column to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Create Function

# Bike Monthly Rentals
def bike_monthly_rentals(df):
    monthly_rentals = df.groupby('mnth')['cnt'].sum()
    return monthly_rentals

# Bike Daily Rentals
def bike_daily_rentals(df):
    daily_rentals = df.groupby('dteday')[['cnt', 'casual', 'registered']].sum()
    return daily_rentals

# Bike Hourly Rentals
def bike_hourly_rentals(df):
    hourly_rentals = df.groupby('hr')['cnt'].sum()
    fig, ax = plt.subplots()
    hourly_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Season
def bike_by_season(df):
    season_rentals = df.groupby('season')['cnt'].sum()
    fig, ax = plt.subplots()
    season_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Weather
def bike_by_weather(df):
    weather_rentals = df.groupby('weathersit')['cnt'].sum()
    fig, ax = plt.subplots()
    weather_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Weather Situation')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Temperature
def bike_by_temp(df):
    fig, ax = plt.subplots()
    sns.histplot(df['temp'], kde=True, ax=ax)
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Weekday
def bike_by_weekday(df):
    weekday_rentals = df.groupby('weekday')['cnt'].sum()
    fig, ax = plt.subplots()
    weekday_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Holiday
def bike_by_holiday(df):
    holiday_rentals = df.groupby('holiday')['cnt'].sum()
    fig, ax = plt.subplots()
    holiday_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Holiday')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Working Day
def bike_by_workingday(df):
    workingday_rentals = df.groupby('workingday')['cnt'].sum()
    fig, ax = plt.subplots()
    workingday_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Working Day')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike by Year
def bike_by_year(df):
    year_rentals = df.groupby('yr')['cnt'].sum()
    fig, ax = plt.subplots()
    year_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Rentals')
    return fig

# Filter the data
min_date = df['dteday'].min()
max_date = df['dteday'].max()

# Create the Web App

# Sidebar
with st.sidebar:
    # Menambahkan logo dari <a href="https://www.flaticon.com/free-icons/rental" title="rental icons">Rental icons created by surang - Flaticon</a>
    st.title('Bike Sharing Dashboard')
    st.image("https://github.com/hamyat/bike_sharing_analysis/blob/main/rent.png")
    st.subheader('Filters')
    # Mengambil start date dan end date dari user
    start_date = st.date_input('Start Date', min_date)
    end_date = st.date_input('End Date', max_date)

    # start_date, end_date = st.date_input(
    #     label='Rentang Waktu',min_value=min_date,
    #     max_value=max_date,
    #     value=[min_date, max_date]
    # )

main_df = df[(df['dteday'] >= str(start_date)) & (df['dteday'] <= str(end_date))]

daily_rentals = bike_daily_rentals(main_df)
monthly_rentals = bike_monthly_rentals(main_df)
season_rentals = bike_by_season(main_df)
weather_rentals = bike_by_weather(main_df)
hourly_rentals = bike_hourly_rentals(main_df)

# Dashboard
# Set the title of the dashboard
st.header('Bike Sharing Dashboard')
st.subheader('Exploratory Data Analysis')

# Display interactive plots
st.write('## Bike Rentals Over Time')
st.line_chart(daily_rentals)
st.write('## Monthly Bike Rentals')
st.bar_chart(monthly_rentals)
st.write('## Hourly Bike Rentals')
st.pyplot(hourly_rentals)
st.write('## Bike Rentals by Season')
st.pyplot(season_rentals)
st.write('## Bike Rentals by Weather Situation')
st.pyplot(weather_rentals)
st.write('## Bike Rentals by Temperature')
st.pyplot(bike_by_temp(main_df))
st.write('## Bike Rentals by Day of the Week')
st.pyplot(bike_by_weekday(main_df))
st.write('## Bike Rentals by Holiday')
st.pyplot(bike_by_holiday(main_df))
st.write('## Bike Rentals by Working Day')
st.pyplot(bike_by_workingday(main_df))
