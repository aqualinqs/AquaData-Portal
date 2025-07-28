import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from supabase import create_client, Client


# --- CONFIG ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Upload handler for Supabase ---
def upload_to_supabase(file):
    file_name = file.name
    data = file.read()
    response = supabase.storage.from_('business-files').upload(file_name, data, {"content-type": file.type})
    return response


# --- NAVIGATION ---
menu = ["Home", "Register Business", "Market & Investor Registration", "Matchmaking", "Business Directory", "Media Upload/Download", "Visual Board", "Business Alerts", "Admin Dashboard",]
choice = st.sidebar.selectbox("Navigation", menu)

# --- PAGE: HOME ---
if choice == "Home":
        st.title("🇬🇭 AquaData Portal")
        st.markdown("""Connecting Ghanaian-owned aquaculture businesses with suppliers, markets, investors, and service providers.""")

# --- PAGE: REGISTER BUSINESS ---
elif choice == "Register Business":
    st.subheader("Register Aquaculture Business")
    with st.form("register_form"):
            business_name = st.text_input("Business Name")
            owner_name = st.text_input("Owner Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            region = st.selectbox("Region", ["Greater Accra", "Ashanti", "Bono", "Volta", "Northern"])
            district = st.text_input("District")
            gps_lat = st.number_input("Latitude", format="%0.6f")
            gps_lon = st.number_input("Longitude", format="%0.6f")
            business_type = st.selectbox("Business Type", ["Hatchery", "Grow-out", "Processor", "Wholesaler"])
            fish_species = st.multiselect("Fish Species", ["Tilapia", "Catfish", "Other"])
            prod_capacity = st.number_input("Production Capacity (kg/month)", min_value=0)
            certification = st.multiselect("Certifications", ["FDA", "MoFA", "None"])
            challenges = st.text_area("Current Challenges")
            submitted = st.form_submit_button("Register")
        

            if submitted:
                with engine.connect() as conn:
                    conn.execute("""
                        INSERT INTO aquaculture_business (business_name, owner_name, contact_email, contact_phone,
                        region, district, gps_lat, gps_lon, business_type, fish_species, production_capacity,
                        certification, challenges)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (business_name, owner_name, email, phone, region, district, gps_lat, gps_lon,
                          business_type, fish_species, prod_capacity, certification, challenges))
                st.success("Business Registered Successfully!")

# --- PAGE: MARKET & INVESTOR REGISTRATION ---
elif choice == "Market & Investor Registration":
    tab1, tab2 = st.tabs(["Register Market", "Register Investor"])

    with tab1:
            st.subheader("Market Registration")
            with st.form("market_form"):
                m_name = st.text_input("Market Name")
                m_type = st.selectbox("Buyer Type", ["Retail", "Wholesale", "Institutional"])
                m_region = st.selectbox("Region", ["Greater Accra", "Ashanti", "Bono"])
                m_fish = st.multiselect("Fish Required", ["Tilapia", "Catfish"])
                m_vol = st.number_input("Volume Required (kg)")
                m_email = st.text_input("Email")
                m_phone = st.text_input("Phone")
                m_submit = st.form_submit_button("Submit Market")
                if m_submit:
                    with engine.connect() as conn:
                        conn.execute("""
                            INSERT INTO market (name, buyer_type, region, fish_required, volume_required, contact_email, contact_phone)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                        """, (m_name, m_type, m_region, m_fish, m_vol, m_email, m_phone))
                    st.success("Market registered.")

    with tab2:
            st.subheader("Investor Registration")
            with st.form("investor_form"):
                i_name = st.text_input("Investor Name")
                i_type = st.selectbox("Investment Type", ["Equity", "Debt", "Grant"])
                i_interest = st.multiselect("Interest Areas", ["Feed Production", "Women-led Farms", "Cold Chain"])
                i_min = st.number_input("Min Ticket Size", min_value=0)
                i_max = st.number_input("Max Ticket Size", min_value=0)
                i_email = st.text_input("Email")
                i_phone = st.text_input("Phone")
                i_submit = st.form_submit_button("Submit Investor")
                if i_submit:
                    with engine.connect() as conn:
                        conn.execute("""
                            INSERT INTO investor (name, investment_type, interest_area, min_ticket_size, max_ticket_size, contact_email, contact_phone)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                        """, (i_name, i_type, i_interest, i_min, i_max, i_email, i_phone))
                    st.success("Investor registered.")

# --- PAGE: MATCHMAKING ---
elif choice == "Matchmaking":
    tab1, tab2 = st.tabs(["Supplier Matchmaking", "Investor Matchmaking"])

    with tab1:
            st.subheader("Supplier Matching Recommendations")
            species_filter = st.selectbox("Select Fish Species", ["Tilapia", "Catfish"])
            region_filter = st.selectbox("Select Region", ["Greater Accra", "Ashanti", "Bono"])
            query = f"""
                SELECT * FROM supplier
                WHERE '{species_filter}' = ANY(products_supplied)
                AND region = '{region_filter}'
            """
            df = pd.read_sql_query(query, engine)
            st.write("Recommended Suppliers:", df)

    with tab2:
            st.subheader("🤝 Investor Matching Recommendations")
            businesses = pd.read_sql("SELECT * FROM aquaculture_business", engine)
            investors = pd.read_sql("SELECT * FROM investor", engine)

            selected_business = st.selectbox("Select a Business", businesses["business_name"])
            biz_row = businesses[businesses["business_name"] == selected_business].iloc[0]

            matches = investors[
                (investors["region"].str.lower().isin([biz_row["region"].lower(), "nationwide"])) &
                (investors["target_sector"].str.lower().str.contains(biz_row["main_activity"].lower())) &
                (investors["target_stage"].str.lower().str.contains(biz_row["business_stage"].lower()))
            ]

            if not matches.empty:
                st.success(f"Found {len(matches)} investor(s) for {selected_business}")
                st.dataframe(matches[["name", "region", "investment_type", "target_sector", "contact_email", "phone_number"]])


# --- PAGE: BUSINESS DIRECTORY ---
elif choice == "Business Directory":
    st.subheader("All Registered Businesses")
    df = pd.read_sql_query("SELECT * FROM aquaculture_business", engine)
    st.dataframe(df)

# --- PAGE: MEDIA UPLOAD/DOWNLOAD ---
elif choice == "Upload/Download File":
    tab1, tab2 = st.tabs(["Upload File", "Download File"])

    with tab1:
            st.subheader("Upload Business File")
            file = st.file_uploader("Choose a file", type=["pdf", "jpg", "png, docx, txt, mp3, mp4"])
            if file:
                result = upload_to_supabase(file)
            if result.status_code == 200:
                st.success(f"Uploaded {file.name} successfully!")  # Save to S3 in supabase
            else:
                st.error("Upload failed. Please try again.")


    with tab2:
            st.subheader("Download Business File")
            downloaded_file = st.download_button("Download Doument", file_name="certificate.pdf")
            if downloaded_file:
                st.success("Download successful!")  # Save to S3 in supabase
            else:
                st.error("Download failed. Please try again.")

# --- PAGE: VISUAL BOARD ---
elif choice == "Visual Board":
    st.subheader("Geospatial Distribution")
    df = pd.read_sql_query("SELECT business_name, gps_lat, gps_lon, region FROM aquaculture_business", engine)
    st.map(df, latitude="gps_lat", longitude="gps_lon", color="[0, 160, 200, 30]")



    st.subheader("Supplier Gaps")
    df_sup = pd.read_sql_query("SELECT region, COUNT(*) AS count FROM supplier GROUP BY region", engine)
    fig = px.bar(df_sup, x="region", y="supplier_count", color="supply_type", title="Supplier Distribution by Region")
    st.plotly_chart(fig)


# --- PAGE: ALERTS & NOTIFICATIONS ---
elif choice == "Business Alerts":
    st.title("🗞️ News Alerts & Notifications")

    st.markdown("""
    Stay updated with the latest aquaculture business news, alerts, and notifications in Ghana.
    """)

    news_df = pd.read_sql("SELECT * FROM business_notifications ORDER BY created_at DESC", engine)

    for _, row in news_df.iterrows():
        st.info(f"**{row['title']}**\n\n{row['message']}\n\n*Posted on {row['created_at']}*")

    with st.expander("📣 Add New Notification (Admin Only)"):
        title = st.text_input("Title")
        message = st.text_area("Message")
        if st.button("Post Notification"):
            with engine.connect() as conn:
                conn.execute(
                    "INSERT INTO business_notifications (title, message, created_at) VALUES (%s, %s, now())",
                    (title, message)
                )
                st.success("Notification posted successfully.")

# --- PAGE: ADMIN DASHBOARD ---
elif choice == "Admin Dashboard":
    st.title("📊 Admin Panel")

# Business registrations by region
df = pd.read_sql_query("SELECT region, COUNT(*) AS count FROM aquaculture_business GROUP BY region", engine)
st.subheader("Registrations by Region")
fig = px.bar(df, x="region", y="count", color="region", title="Business Count by Region")
st.plotly_chart(fig)

# Production capacity summary
df_cap = pd.read_sql_query("SELECT region, SUM(production_capacity) as total_production FROM aquaculture_business GROUP BY region", engine)
st.subheader("Production Capacity by Region")
st.dataframe(df_cap)        

# View full dataset
st.subheader("All Business Records")
df_all = pd.read_sql_query("SELECT * FROM aquaculture_business", engine)
st.dataframe(df_all)

# CSV Export
csv = df_all.to_csv(index=False).encode('utf-8')
st.download_button("Download as CSV", csv, "aquaculture_businesses.csv", "text/csv")
