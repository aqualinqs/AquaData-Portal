# 🌊 🇬🇭 AquaData Portal


![Portal Banner](https://media.giphy.com/media/fS99W61FK1QFu/giphy.gif)

> **Connecting Ghanaian-owned aquaculture businesses with the right markets, suppliers, and investors – one data point at a time.**

A Streamlit-based data platform that links Ghanaian-owned aquaculture businesses with suppliers, markets, investors and key service providers in the aquaculture industry.

---

### 🚀 Features

- ✅ **Business Registration** – Capture geolocated aquaculture business data
- 📈 **Admin Dashboard** – Visualize production by region and business stages
- 🧭 **Geospatial Clustering** – Map aquaculture businesses across Ghana
- 🤝 **Investor Matchmaking** – Match investors with verified businesses
- 📤 **Supabase Storage** – Upload & manage media documents (PDFs, images)
- 📬 **Email & SMS Alerts** – Notify investors using Twilio and Gmail
- 📊 **Interactive Charts** – Built with Plotly and PyDeck
- 🔐 **Authentication** – Secure access via Streamlit Authenticator

---

### 🎯 Project Goal

This portal is designed to support **Ghanaian aquaculture entrepreneurs** by:
- Providing visibility across the value chain
- Enabling easy access to quality and affordable inputs and profitable markets.
- Attracting investment and technical support
- Enabling data-driven interventions for **food security and economic growth**

---

### 📸 Screenshots

#### 💻 Admin Dashboard
![Admin Dashboard](https://media.giphy.com/media/UsmcxsoAyA0XYZghaa/giphy.gif)

#### 📍 Business Mapping
![Map](https://media.giphy.com/media/IlyjQ2fEMqbrMbzE2y/giphy.gif)

#### 🤖 Matchmaking + Alerts
![Matchmaking](https://media.giphy.com/media/qErLw8jIfk6S7rpMiP/giphy.gif)

---

### 🛠 Tech Stack

| Backend | Frontend | Storage & Auth | Notifications |
|--------|----------|----------------|----------------|
| PostgreSQL | Streamlit | Supabase | Twilio (SMS), Gmail SMTP |
| SQLAlchemy | PyDeck | Firebase (optional) | Plotly Charts |

---

### ⚙️ Deployment

```bash
git clone https://github.com/aqualinqs/AquaData-Portal.git
cd AquaData-Portal

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run AquaGhana_Portal.py

🔐 Create a .streamlit/secrets.toml file for your credentials.

---

### 🧪 Testing & Sample Data
Mock SQL seed scripts and test cases available in AquaGhana_data.sql.

---

### 🤝 Contributions Welcome!
We love contributions! If you'd like to:

Add more analytics

Connect to blockchain traceability

Expand to other African countries

Fork, branch, and send a PR 🚀

---

📩 Contact
Built by: @aqualinqs
📧 Email: aqualinqs22@gmail.com

This project is made with ❤️ for sustainable aquaculture and nutrition security in Ghana.
---
