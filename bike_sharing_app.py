import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# Load the dataset
data_path = 'bikeshare_hour_clean.csv'
df = pd.read_csv(data_path)

# Create Function

# Bike Montthly Rentals
def bike_monthly_rentals(df):
    monthly_rentals = df.groupby('mnth')['cnt'].sum()
    fig, ax = plt.subplots()
    monthly_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Rentals')
    return fig

# Bike Daily Rentals
def bike_daily_rentals(df):
    daily_rentals = df.groupby('weekday')['cnt'].sum()
    fig, ax = plt.subplots()
    daily_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Rentals')
    return fig

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

# Bike by Week
def bike_by_week(df):
    week_rentals = df.groupby('week')['cnt'].sum()
    fig, ax = plt.subplots()
    week_rentals.plot(kind='bar', ax=ax)
    ax.set_xlabel('Week')
    ax.set_ylabel('Number of Rentals')
    return fig

# Filter the data
min_date = df['dteday'].min()
max_date = df['dteday'].max()

# Create the Web App

# Sidebar
st.sidebar.title('Bike Sharing Dashboard')
st.sidebar.subheader('Filters')
start_date = st.sidebar.date_input('Start Date', min_date)
end_date = st.sidebar.date_input('End Date', max_date)

# Set the title of the dashboard
st.header('Bike Sharing Dashboard')
st.subheader('Exploratory Data Analysis')

# Display the dataframe
st.subheader('Bike Sharing Data')
st.write(df.head())

# Plot the number of bike rentals per hour
st.subheader('Number of Bike Rentals per Hour')
hourly_rentals = df.groupby('hr')['cnt'].sum()
fig, ax = plt.subplots()
hourly_rentals.plot(kind='bar', ax=ax)
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)

# Plot the number of bike rentals per day of the week
st.subheader('Number of Bike Rentals per Day of the Week')
daily_rentals = df.groupby('weekday')['cnt'].sum()
fig, ax = plt.subplots()
daily_rentals.plot(kind='bar', ax=ax)
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)

# Plot the number of bike rentals per month
st.subheader('Number of Bike Rentals per Month')
monthly_rentals = df.groupby('mnth')['cnt'].sum()
fig, ax = plt.subplots()
monthly_rentals.plot(kind='bar', ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)