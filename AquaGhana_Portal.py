import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk

# --- DEMO MODE MOCK DATA ---
mock_businesses = pd.DataFrame({
    'business_name': ['Lake Aqua Farms', 'Tilapia Gold Ltd'],
    'owner_name': ['Kwame Mensah', 'Ama Boateng'],
    'region': ['Greater Accra', 'Ashanti'],
    'district': ['Tema', 'Kumasi'],
    'gps_lat': [5.6037, 6.6885],
    'gps_lon': [-0.1870, -1.6244],
    'business_type': ['Hatchery', 'Grow-out'],
    'fish_species': [['Tilapia'], ['Catfish']],
    'production_capacity': [5000, 7000],
    'certification': [['FDA'], ['MoFA']],
    'challenges': ['Access to quality feed', 'Cold chain logistics']
})

mock_alerts = pd.DataFrame({
    'title': ['New Funding Opportunity', 'Disease Control Workshop'],
    'message': [
        'Apply now for the Aquaculture SME Fund by August 30th.',
        'Join our free training on disease management this weekend in Kumasi.'
    ],
    'created_at': ['2025-07-28', '2025-07-25']
})

# --- NAVIGATION ---
menu = ["Home", "Register Business", "Market & Investor Registration", "Matchmaking", "Business Directory", "Media Upload/Download", "Visual Board", "Business Alerts", "Admin Dashboard",]
choice = st.sidebar.selectbox("Navigation", menu)

# --- PAGE: HOME ---
if choice == "Home":
        st.title("🇬🇭 AquaData Portal")
        st.subheader("Demo mode")
        st.markdown("""Connecting Ghanaian-owned aquaculture businesses with suppliers, markets, investors, and service providers.""")
# --- PAGE: REGISTER BUSINESS ---
elif choice == "Register Business":
    st.subheader("Demo: Register Aquaculture Business")
    st.info("Form submission disabled in demo mode.")

# --- PAGE: MARKET & INVESTOR REGISTRATION ---
elif choice == "Market & Investor Registration":
    st.subheader("Demo: Market & Investor Registration")
    st.info("Registration forms are disabled in demo mode.")

# --- PAGE: MATCHMAKING ---
elif choice == "Matchmaking":
    st.subheader("Demo: Investor Matchmaking")
    selected_business = st.selectbox("Select a Business", mock_businesses["business_name"])
    st.write("Investor matches are simulated in demo mode.")

# --- PAGE: BUSINESS DIRECTORY ---
elif choice == "Business Directory":
    st.subheader("Registered Businesses (Demo Data)")
    st.dataframe(mock_businesses)

# --- PAGE: MEDIA UPLOAD/DOWNLOAD ---
elif choice == "Media Upload/Download":
    st.subheader("Demo: Upload/Download Business Files")
    st.info("File upload and download features are disabled in demo mode.")

# --- PAGE: VISUAL BOARD ---
elif choice == "Visual Board":
    st.subheader("Geospatial Distribution (Demo)")
    st.map(mock_businesses.rename(columns={"gps_lat": "latitude", "gps_lon": "longitude"}))

# --- PAGE: BUSINESS ALERTS ---
elif choice == "Business Alerts":
    st.title("🗞️ News Alerts & Notifications")
    for _, row in mock_alerts.iterrows():
        st.info(f"**{row['title']}**\n\n{row['message']}\n\n*Posted on {row['created_at']}*")

# --- PAGE: ADMIN DASHBOARD ---
elif choice == "Admin Dashboard":
    st.title("📊 Admin Panel")
    st.subheader("Business Registrations by Region")
    region_summary = mock_businesses.groupby("region").size().reset_index(name="count")
    fig = px.bar(region_summary, x="region", y="count", color="region", title="Businesses by Region")
    st.plotly_chart(fig)

    st.subheader("Production Capacity")
    prod_summary = mock_businesses.groupby("region")["production_capacity"].sum().reset_index()
    st.dataframe(prod_summary)

    st.download_button("Download Demo Data", mock_businesses.to_csv(index=False).encode(), "mock_businesses.csv", "text/csv")
