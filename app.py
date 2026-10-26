import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Page configuration
st.set_page_config(
    page_title="AI Cybersecurity Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-Powered Cybersecurity Threat Detection")
st.write("Detect unusual network activity using Machine Learning.")

# Generate sample normal network traffic for demonstration
np.random.seed(42)

normal_data = pd.DataFrame({
    "packets": np.random.randint(10, 100, 1000),
    "failed_logins": np.random.randint(0, 3, 1000),
    "bytes_sent": np.random.randint(500, 10000, 1000),
    "connections": np.random.randint(1, 20, 1000)
})

# Train the anomaly detection model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(normal_data)

st.subheader("Enter Network Activity")

packets = st.number_input(
    "Number of packets",
    min_value=0,
    value=30
)

failed_logins = st.number_input(
    "Failed login attempts",
    min_value=0,
    value=0
)

bytes_sent = st.number_input(
    "Bytes sent",
    min_value=0,
    value=3000
)

connections = st.number_input(
    "Number of connections",
    min_value=0,
    value=5
)

# Analyze network activity
if st.button("Analyze Threat"):

    input_data = pd.DataFrame([{
        "packets": packets,
        "failed_logins": failed_logins,
        "bytes_sent": bytes_sent,
        "connections": connections
    }])

    prediction = model.predict(input_data)[0]

    if prediction == -1:
        st.error("⚠️ Suspicious Network Activity Detected!")
        st.write("The activity differs from the sample normal traffic.")
    else:
        st.success("✅ Network Activity Appears Normal")
        st.write("No anomaly was detected by the model.")

    # Display submitted information
    st.subheader("Network Activity Report")

    st.dataframe(input_data, use_container_width=True)

    # Display basic statistics
    st.metric("Packets", packets)
    st.metric("Failed Logins", failed_logins)
    st.metric("Bytes Sent", bytes_sent)
    st.metric("Connections", connections)

st.caption(
    "Educational prototype. Uses synthetic training data; "
    "not suitable for real-world security monitoring."
)