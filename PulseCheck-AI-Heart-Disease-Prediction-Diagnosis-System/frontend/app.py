import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="PulseCheck AI", layout="wide")

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.main { background-color: #0d1b2a; color: white; }

.stButton > button {
    background: linear-gradient(90deg, #e63946, #c1121f);
    color: white;
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
    width: 100%;
}

.risk-high {
    background: #c1121f;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    color: white;
}

.risk-low {
    background: #2d6a4f;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("## ❤️ PulseCheck AI")
st.markdown("*AI-Powered Heart Disease Prediction System*")
st.markdown("---")

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.markdown("## About")
    st.info("Predicts heart disease risk using ML models")
    st.markdown("**Model:** Logistic Regression")
    st.markdown("**Accuracy:** ~85%")
    st.markdown("**Team:** Your Team")

# ---------------- INPUTS (3 COLUMNS) ---------------- #
st.markdown("### Enter Patient Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 20, 80, 40)
    gender_option = st.selectbox("Gender", ["Female", "Male"])
    gender = 0 if gender_option == "Female" else 1

    cp_option = st.selectbox("Chest Pain Type",
        ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "No Pain"])
    cp_map = {"Typical Angina":0,"Atypical Angina":1,"Non-anginal Pain":2,"No Pain":3}
    cp = cp_map[cp_option]

    trestbps = st.number_input("Resting BP", 80, 200, 120)

with col2:
    chol = st.number_input("Cholesterol", 100, 600, 200)

    fbs_option = st.selectbox("Fasting Blood Sugar", ["Normal", "High"])
    fbs = 0 if fbs_option == "Normal" else 1

    restecg_option = st.selectbox("Resting ECG",
        ["Normal", "ST-T Abnormality", "LV Hypertrophy"])
    restecg_map = {"Normal":0,"ST-T Abnormality":1,"LV Hypertrophy":2}
    restecg = restecg_map[restecg_option]

    thalach = st.slider("Max Heart Rate", 60, 220, 150)

with col3:
    exang_option = st.selectbox("Exercise Angina", ["No", "Yes"])
    exang = 0 if exang_option == "No" else 1

    oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)

    slope_option = st.selectbox("ST Slope",
        ["Upsloping", "Flat", "Downsloping"])
    slope_map = {"Upsloping":0,"Flat":1,"Downsloping":2}
    slope = slope_map[slope_option]

    ca = st.selectbox("Major Vessels", [0,1,2,3])

    thal_option = st.selectbox("Thalassemia",
        ["Normal","Fixed Defect","Reversible Defect","Severe"])
    thal_map = {"Normal":0,"Fixed Defect":1,"Reversible Defect":2,"Severe":3}
    thal = thal_map[thal_option]

# ---------------- PREDICT ---------------- #
if st.button("Analyze Heart Health"):

    payload = {
        "features":[age, gender, cp, trestbps, chol,
                    fbs, restecg, thalach,
                    exang, oldpeak, slope, ca, thal]
    }

    try:
        res = requests.post("http://127.0.0.1:5000/predict", json=payload)
        result = res.json()['prediction']

        colA, colB = st.columns(2)

        # -------- RESULT -------- #
        with colA:
            if result == "High Risk":
                st.markdown('<div class="risk-high">⚠️ HIGH RISK</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="risk-low">✅ LOW RISK</div>', unsafe_allow_html=True)

        # -------- GAUGE CHART -------- #
        with colB:
            # dummy confidence (you can upgrade backend later)
            confidence = 75 if result == "High Risk" else 30909

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=confidence,
                title={'text': "Confidence %"},
                gauge={'axis': {'range': [0, 100]}}
            ))

            st.plotly_chart(fig, use_container_width=True)

    except:
        st.error("Backend not running")