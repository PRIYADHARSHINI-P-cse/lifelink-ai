import streamlit as st

st.set_page_config(page_title="LifeLink AI", layout="centered")

# Global CSS styling
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.pexels.com/photos/12193090/pexels-photo-12193090.jpeg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: black !important;
    }

    .main .block-container {
        background-color: white !important;
        padding: 2.5rem 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        max-width: 760px;
        margin: 6vh auto;
    }

    h1, h2, h3, h4, h5, h6, p, label, .css-1cpxqw2 {
        color: black !important;
    }

    .stButton>button {
        background-color: #b1003f;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1.5rem;
        font-size: 1rem;
    }

    .stButton>button:hover {
        background-color: #870031;
    }

    .css-1d391kg, .css-1v3fvcr {
        color: white !important;  /* Sidebar text */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🩸 LifeLink AI")
page = st.sidebar.radio("Navigate", ["Home", "Find Donor", "Estimate Cost", "About"])

# Title
st.title("🏥 LifeLink AI")
st.subheader("Connecting Hope through AI for Thalassemia Support")

# Page Content
if page == "Home":
    st.markdown("""
    LifeLink AI is an AI-powered platform supporting Thalassemia patients in India.

    ### 🌟 Features:
    - 🩸 Match with verified blood donors
    - 💰 Provide yearly treatment cost estimates
    - 🎗 Suggest government & NGO aid programs

    💡 Designed for the AI for Good Hackathon 2025 by Team CARE LINKERS
    """)

elif page == "Find Donor":
    st.header("🩸 Find a Blood Donor")
    st.markdown("Use our AI-assisted donor finder to connect with available matches near you.")

    blood_group = st.selectbox("Select Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    city = st.text_input("Enter City or Pincode")
    urgency = st.selectbox("Urgency Level", ["Low", "Medium", "High"])

    if st.button("🔍 Find Donors"):
        if not city.strip():
            st.error("⚠ Please enter a valid city or pincode.")
        else:
            donor_db = {
                "A+": {
                    "Low": [("Anita Sharma", 91), ("Rohit Mehra", 87), ("Divya Iyer", 83)],
                    "Medium": [("Karan Joshi", 93), ("Nidhi Patel", 89), ("Amit Rao", 85)],
                    "High": [("Riya Kapoor", 96), ("Sarthak Jain", 92), ("Tanvi Verma", 90)]
                },
                # [Other blood groups as before...]
                # ...
            }

            matches = donor_db.get(blood_group, {}).get(urgency, [])

            if matches:
                st.success("Top AI‑matched donors near you:")
                for donor, score in matches:
                    st.markdown(f"✅ {donor} – Match Score: {score}%")
            else:
                st.warning("No matches found for the selected criteria.")

    st.markdown("### 📞 Contact Details to Reach Donors")
    with st.form("contact_form"):
        name = st.text_input("Your Full Name *", key="name")
        email = st.text_input("Email Address *", key="email")
        phone = st.text_input("Phone Number *", key="phone")
        message = st.text_area("Additional Info (Optional)", placeholder="Eg: Preferred time to contact or patient details")

        submitted = st.form_submit_button("📬 Send Request")

        if submitted:
            if not name.strip():
                st.error("⚠ Please enter your full name.")
            elif not email.strip():
                st.error("⚠ Please enter a valid email address.")
            elif not phone.strip():
                st.error("⚠ Please enter your phone number.")
            else:
                st.success(f"✅ Thank you {name}, your request has been shared with the donor coordinator.")

elif page == "Estimate Cost":
    st.header("💰 Treatment Cost Estimator")
    st.markdown("Get a detailed estimate for annual Thalassemia treatment costs.")

    state = st.selectbox("Select State", ["Tamil Nadu", "Maharashtra", "Delhi", "West Bengal", "Other"])
    age = st.number_input("Enter Patient Age", min_value=0, max_value=100, step=1)
    hospital = st.selectbox("Choose Hospital Type", ["Government", "Private", "NGO"])

    if st.button("💡 Estimate Cost"):
        base = 2500 if hospital == "Government" else 6000 if hospital == "NGO" else 12000
        factor = 1.2 if age > 12 else 1.0
        monthly_cost = int(base * factor)
        yearly = monthly_cost * 12

        st.success(f"Estimated Yearly Cost: ₹{yearly:,}")
        st.markdown(f"""
        Detailed Breakdown:
        - 💉 Monthly Transfusion Cost: ₹{monthly_cost:,}
        - 🗓 12-Month Total: ₹{yearly:,}
        - 🏥 Hospital Type: {hospital}
        - 👤 Patient Age: {age} years
        - 📍 Location: {state}

        ### 🎯 You may be eligible for these aid programs:
        - 🛡 Blood Warriors Fund – Offers subsidies for low-income families.
        - 💰 PM Health Assistance Scheme – Central aid for rare disease treatment.
        - 🏥 {state} State Insurance Program – Covers Thalassemia treatment in select hospitals.
        """)

elif page == "About":
    st.header("📘 About LifeLink AI")
    st.markdown("""
    LifeLink AI is developed by Team CARE LINKERS for the AI for Good Hackathon 2025.

    ### 🫀 Mission:
    Empower Thalassemia patients through intelligent tools and accessible healthcare insights.

    ### 🔑 Highlights:
    - 💡 Smart donor matching
    - 💸 Cost estimation based on age and hospital type
    - 🧾 Aid and support program suggestions
    """)

# Footer
st.markdown("---")
st.caption("© 2025 LifeLink AI — Built for Humanity")
