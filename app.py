import pickle
import string
import streamlit as st
import webbrowser

# Load the model
LrdetectFile = open('model.pkl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

# Function to show the prediction results
def showResults(input_test):
    Model_Predict = Lrdetect_Model.predict([input_test])

    if Model_Predict[0] == 1:
        st.text("This Tweet is a Disaster")
    else:
        st.text("This Tweet is Not a Disaster")

# Check if the start button has been pressed
if 'start_button_clicked' not in st.session_state:
    st.session_state.start_button_clicked = False

# Home page layout
def home_page():
    st.title("Welcome to the Disaster Tweet Classifier")
    st.write("This application uses natural language processing to classify tweets related to disasters.")
    
    if st.button("Start"):
        st.session_state.start_button_clicked = True
    
    # Footer
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            }
        </style>
        <div class="footer">
            <p>Developed by Chamod Nadeeranga @2024</p>
        </div>
        """, unsafe_allow_html=True)

# Prediction page layout
def prediction_page():
    st.title("Natural Language Processing with Disaster Tweets")
    input_test = st.text_input("Provide your disaster tweet here", '')
    button_clicked = st.button("Predict Tweet")
    if button_clicked:
        showResults(input_test)

# Conditional rendering based on the start button
if not st.session_state.start_button_clicked:
    home_page()
else:
    prediction_page()