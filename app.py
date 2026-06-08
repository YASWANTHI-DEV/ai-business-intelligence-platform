import streamlit as st
import pandas as pd

from auth import register_user
from auth import login_user
from database import create_users_table

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI-Powered Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
}

.feature-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# DATABASE
# -------------------------

create_users_table()

# -------------------------
# SESSION STATE
# -------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "data" not in st.session_state:
    st.session_state.data = None


# -------------------------
# LOGOUT FUNCTION
# -------------------------

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.data = None


# -------------------------
# LOGIN / REGISTER
# -------------------------

if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    st.markdown(
        '<p class="main-title">📊 AI-Powered Business Intelligence Platform</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">Sales Analytics | Forecasting | Business Insights</p>',
        unsafe_allow_html=True
    )

    if menu == "Register":

        st.subheader("📝 Create Account")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            if register_user(
                username,
                password
            ):
                st.success(
                    "Registration Successful!"
                )

            else:
                st.error(
                    "Username already exists."
                )

    else:

        st.subheader("🔐 Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login_user(
                username,
                password
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

# -------------------------
# HOME PAGE
# -------------------------

else:

    st.sidebar.success(
        f"Welcome, {st.session_state.username}"
    )

    # Upload Dataset Once

    uploaded_file = st.sidebar.file_uploader(
        "📂 Upload Sales Dataset",
        type=["csv"]
    )

    if uploaded_file is not None:

        st.session_state.data = pd.read_csv(
            uploaded_file
        )

    if st.sidebar.button("🚪 Logout"):

        logout()

        st.rerun()

    # Main Page

    st.markdown(
        '<p class="main-title">🚀 AI-Powered Business Intelligence Platform</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">Executive Dashboard for Sales Analytics & Forecasting</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    if st.session_state.data is not None:

        df = st.session_state.data

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "📦 Records",
            len(df)
        )

        col2.metric(
            "📋 Columns",
            len(df.columns)
        )

        col3.metric(
            "👤 User",
            st.session_state.username
        )

        st.success(
            f"Dataset Loaded Successfully ({len(df)} rows)"
        )

        st.subheader(
            "Dataset Preview"
        )

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    else:

        st.info(
            "Upload a dataset from the sidebar to begin analytics."
        )

    st.markdown("---")

    st.markdown("""
<div class="feature-box">

### Features Included

✅ Secure Login & Registration

✅ Dataset Upload

✅ Executive Dashboard

✅ Product Analytics

✅ Customer Analytics

✅ Revenue Trends

✅ Sales Forecasting

✅ AI Business Insights

✅ Download Reports

</div>
""", unsafe_allow_html=True)