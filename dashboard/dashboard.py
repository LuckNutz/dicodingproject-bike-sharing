import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menyiapkan data
df = pd.read_csv("hour.csv")

# Mengubah tipe data 'dteday' ke datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Memberi label pada nilai 'season'
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df['season'] = df['season'].map(season_mapping)

# Memasang judul dashboard
st.title("Bike Sharing Dashboard")

# Mengatur Sidebar
st.sidebar.image("data:image/png;base64,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", caption="Bike Sharing", use_column_width=True)
st.sidebar.title("Option")
start_date = pd.Timestamp(st.sidebar.date_input("Start Date", min(df['dteday'])))
end_date = pd.Timestamp(st.sidebar.date_input("End Date", max(df['dteday'])))
user_type = st.sidebar.selectbox("User Type", ["Casual", "Registered", "Total"])

# Mengatur pilihan rentang waktu berdasarkan input user
filtered_df = df[(df['dteday'] >= start_date) & (df['dteday'] <= end_date)]

# Total rental
st.header("Total Rental")
total_rental = filtered_df[user_type.lower()].sum()
st.write(f"Total {user_type} Rental: {total_rental}")

# Total rental berdasarkan jam dalam sehari
st.subheader("Rental by Hour in A Day")
fig_hourly = plt.figure()
sns.lineplot(x='hr', y=user_type.lower(), data=filtered_df, estimator='sum', ci=None)
plt.xlabel("Hour of the Day")
plt.ylabel("Total Rentals")
plt.title(f"Hourly Rentals for {user_type} Users")
st.pyplot(fig_hourly)

# Total rental berdasarkan bulan
st.subheader("Rental by Month")
fig_monthly = plt.figure()
sns.lineplot(x='mnth', y=user_type.lower(), data=filtered_df, estimator='sum', ci=None)
plt.xlabel("Month")
plt.ylabel("Total Rentals")
plt.title(f"Monthly Rentals for {user_type} Users")
st.pyplot(fig_monthly)

# Total rental berdasarkan musim
st.subheader("Rental by Season")
fig_season = plt.figure()
sns.lineplot(x='season', y=user_type.lower(), data=filtered_df, estimator='sum', ci=None)
plt.xlabel("Season")
plt.ylabel("Total Rentals")
plt.title(f"Seasonal Rentals for {user_type} Users")
st.pyplot(fig_season)

# Hak Cipta
st.markdown("© 2023 Armand Maulana")