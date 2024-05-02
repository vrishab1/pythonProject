"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Final Project - Starbucks
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import streamlit as st
import pandas as pd
import folium as fo
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
from geopy.distance import geodesic

#Loading the data[PY3][DA1]
@st.cache_data
def load_data():
    data = pd.read_csv("Starbucks_Data.csv")
    data['CountrySubdivisionCode'] = data['CountrySubdivisionCode'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    data['City'] = data['City'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    data['OwnershipType'] = data['OwnershipType'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return data

#Container that acts as an introduction to the page
def welcome_message():
    expander = st.expander("Welcome to my Starbucks Locator!", expanded=True)
    with expander:
        st.image("Starbucks_welcome_image.jpeg", width=500)
        st.write("""This interactive web application allows you to explore Starbucks locations based on your selections for country, state, city, and ownership type.
                    Use the sidebar to filter locations and visualize them on the map as well as play around with the radius to see just how far certain Starbucks are. Scroll down to view detailed charts about Starbucks ownership types.
                    If you're interested to see the Total Number of Starbucks Per Ownership Type used in Dataset and/or The Pivot Table of Starbucks Locations and Ownership (limited to 10000 rows), click the button(s) in the sidebar and scroll down on the main page. You can also see the top 10 timezones with the most Starbucks locations. In addition, you can also see the different charts used by scrolling down and clicking the buttons.""")
        st.write("Thank you for viewing my website. Hope you enjoyed!")

#Different Streamlit features added and dict[ST1][ST2][ST3][ST4][PY5][DA4]
def user_input_sidebar(data):
    st.sidebar.image("Starbucks_image.jpeg", caption='Starbucks', use_column_width=True)
    st.sidebar.header("User Input Options")
    selected_country = st.sidebar.selectbox('Select a country', data['CountryCode'].unique())
    selected_state = st.sidebar.selectbox('Select a state', data[data['CountryCode'] == selected_country]['CountrySubdivisionCode'].unique())
    selected_city = st.sidebar.selectbox('Select a city', data[(data['CountryCode'] == selected_country) & (data['CountrySubdivisionCode'] == selected_state)]['City'].unique())
    radius_miles = st.sidebar.slider("Select radius (in miles)", min_value=1, max_value=50, value=1)
    ownership_dict = {'CO': "Company Owned", 'FR': "Franchised", 'JV': "Joint Venture", 'LS': "Licensed Store"}
    ownership_types = st.sidebar.multiselect("Select Ownership Type(s)", options=list(ownership_dict.keys()), format_func=lambda x: f"{x} - {ownership_dict[x]}", default=['CO', 'FR', 'JV', 'LS'])
    return selected_country, selected_state, selected_city, radius_miles, ownership_types

#Sets up the filtering options using the data for Streamlit[DA5]
def filter_data(data, selected_country, selected_state, selected_city, ownership_types):
    state_data = data[(data['CountryCode'] == selected_country) & (data['CountrySubdivisionCode'] == selected_state)]
    city_data = state_data[(state_data['City'] == selected_city) & (state_data['OwnershipType'].isin(ownership_types))]
    return state_data, city_data

#Displays the map using the data and creates the yellow and green blue circles
def display_map_and_data(state_data, city_data, selected_city, selected_state, selected_country, radius_miles):
    if city_data.empty:
        st.error("The selected ownership type does not exist in this area. Please pick another choice.")
    else:
        center_lat = city_data['Latitude'].mean()
        center_lon = city_data['Longitude'].mean()

        # Filter data within radius using miles.[PY2]
        def filter_data_within_radius(data, state_data, center_lat, center_lon, radius_miles):
            filtered = data[data.apply(lambda x: geodesic((x['Latitude'], x['Longitude']), (center_lat, center_lon)).miles <= radius_miles,axis=1)]
            return filtered, len(filtered)

        filtered_data, location_count = filter_data_within_radius(state_data, city_data, center_lat, center_lon,radius_miles)

        st.write(f"Number of Starbucks locations within a {radius_miles} mile radius of {selected_city}, {selected_state}, {selected_country}: {len(filtered_data)}")

        # Create map
        m = fo.Map(location=[center_lat, center_lon], zoom_start=8)

        # Yellow circle for the state
        fo.Circle(
            location=[center_lat, center_lon],
            radius=80467.2,  #50 miles in meters
            color='yellow',
            fill=True,
            fill_color='yellow',
            popup=(f"{selected_state}")
        ).add_to(m)

        # Blue circle for the city
        fo.Circle(
            location=[center_lat, center_lon],
            radius=radius_miles * 1609.34,  # Convert miles to meters for visualization
            color='blue',
            fill=True,
            fill_color='blue',
            popup=(f"{selected_city} {radius_miles} miles")
        ).add_to(m)

        # Adds Icons and markers and popup to map [MAP1][PY4][DA8]
        markers = [fo.Marker(
            location=[row['Latitude'], row['Longitude']],
            icon=fo.Icon(icon="glyphicon glyphicon-glass", color='green'),
            popup=f"{row['Street1']}<br>{row['City']}, {row['PostalCode']}"
        ).add_to(m) for idx, row in filtered_data.iterrows()]

        folium_static(m)

#Creation of Summary table, top 10 table, and Pivot table[DA7]
def tables(data):
    if st.sidebar.button('Show Starbucks Ownership Summary'):
        ownership_summary = data['OwnershipType'].value_counts().reset_index()
        ownership_summary.columns = ['Ownership Type', 'Number of Locations']
        total_locations = ownership_summary['Number of Locations'].sum()
        total_row = pd.DataFrame([['Total', total_locations]], columns=ownership_summary.columns)
        ownership_summary = pd.concat([ownership_summary, total_row], ignore_index=True)
        st.write("Total Number of Starbucks Per Ownership Type in the entire Dataset:")
        st.table(ownership_summary)

    #Pivot Table [DA9][DA2][DA6]
    if st.sidebar.button('Show Pivot Table of Starbucks Locations and Ownership Summary'):
        pivot_table = pd.pivot_table(data, values='StoreNumber', index='CountryCode', columns='OwnershipType', aggfunc='count', fill_value=0)
        pivot_table['Total by Country'] = pivot_table.sum(axis=1)
        pivot_table = pivot_table.sort_values(by='Total by Country', ascending=False)
        pivot_table.loc['Total by Ownership Type'] = pivot_table.sum()
        st.write("Pivot Table of Starbucks Locations by Country and Ownership Type:")
        st.table(pivot_table)

    # Top 10 timezones. [DA3]
    if st.sidebar.button("Analyze Time Zones"):
        timezone_counts = data['TimezoneId'].value_counts().head(10)
        st.write("Top 10 Time Zones with Most Starbucks Locations:")
        st.write(timezone_counts)

#Creation on Charts. Bar, Pie, and Donut
def charts(data):
    ownership_count = data['OwnershipType'].value_counts()

    # Bar Chart [VIZ1]
    if st.button('Show Bar Chart of Starbucks Ownership Types'):
        fig, ax = plt.subplots()
        ax.set_title('Starbucks Ownership Types')
        st.subheader('Total Number of Starbucks Per Ownership Type (Bar Chart)')
        ownership_count.plot(kind='bar', color=['blue', 'green', 'red', 'yellow'], ax=ax)
        ax.set_xlabel('Ownership Type')
        ax.set_ylabel('Count')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

    # Pie Chart [VIZ2]
    if st.button('Show Pie Chart of Starbucks Ownership Types'):
        fig1, ax1 = plt.subplots()
        ax1.set_title('Distribution of Starbucks Ownership Types\n')
        st.subheader('Proportion of Starbucks Ownership Types (Pie Chart)')
        ax1.pie(ownership_count, labels=ownership_count.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red', 'yellow'])
        ax1.axis('equal')
        st.pyplot(fig1)

    # Donut Chart [VIZ3]
    if st.button('Show Donut Chart of Starbucks Ownership Types'):
        fig2, ax2 = plt.subplots()
        ax2.set_title('Distribution of Starbucks Ownership Types')
        st.subheader('Proportion of Starbucks Ownership Types (Donut Chart)')
        ax2.pie(ownership_count, labels=ownership_count.index, autopct='%1.1f%%', startangle=90,colors=['blue', 'green', 'red', 'yellow'], wedgeprops=dict(width=0.6))
        ax2.set_aspect('equal')
        st.pyplot(fig2)

def main():
    data = load_data()
    welcome_message()
    selected_country, selected_state, selected_city, radius_miles, ownership_types = user_input_sidebar(data)
    state_data, city_data = filter_data(data, selected_country, selected_state, selected_city,ownership_types)
    display_map_and_data(state_data, city_data, selected_city, selected_state, selected_country, radius_miles)
    tables(data)
    charts(data)

if __name__ == "__main__":
    main()