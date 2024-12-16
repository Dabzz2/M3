# streamlit_app.py
import streamlit as st
import requests

# Streamlit app title
st.title("Multi-Agent Economic Discussion App")

# Instructions
st.markdown("""
Enter two economic variables to initiate the discussion between the Economist and Financial Analyst.
""")

# Input fields
var1 = st.text_input("Enter economic variable 1 (e.g., inflation rate):")
var2 = st.text_input("Enter economic variable 2 (e.g., government spending):")

# Button to run the agents
if st.button("Run Discussion"):
    if var1 and var2:
        with st.spinner("Running agents..."):
            try:
                # Call the FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/run_agents",
                    json={"var1": var1, "var2": var2}
                )
                if response.status_code == 200:
                    result = response.json()
                    st.success("Agents have completed their discussion!")
                    st.text_area("Discussion Output", result, height=300)
                else:
                    st.error(f"Error running agents: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter both variables.")