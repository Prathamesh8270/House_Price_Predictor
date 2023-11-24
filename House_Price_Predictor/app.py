import streamlit as st
import pickle as pk
import pandas as pd

model = pk.load(open(r"C:\Users\asus\OneDrive\Documents\Full Web Development and Python Bootcamp\Python Tutorial\Python ML and DL Projects\House_Price_Predictor\House_Price_Price_model.pkl","rb"))

st.header("Banglore House Predictor")

data = pd.read_csv(r"C:\Users\asus\OneDrive\Documents\Full Web Development and Python Bootcamp\Python Tutorial\Python ML and DL Projects\House_Price_Predictor\Cleaned_data.csv")
with st.form(key="my_form"):
        
    loc = st.selectbox("Choose the location",data["location"].unique())
    sqft = st.number_input("Enter the total sqft")
    beds = st.number_input("Enter the number of bedrooms")
    bath = st.number_input("Enter the number of bathrooms")
    balc = st.number_input("Enter the number of balcony")

    input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=["location","total_sqft","bath","balcony","bedroom"])


# if st.button("Predict Price"):
#     output = model.predict(input)
#     out_str = "Price of the House is " + str(output[0]*100000)

    # button_check = st.form_submit_button("Button to Click")
    submit_button = st.form_submit_button(label='Predict')
    # st.session_state["submitted"] = st.form_submit_button("Submit")
    if submit_button:
        output = model.predict(input)
        # out_str = "Price of the House is " + str(output[0]*100000)
        st.write(f"The predicted sales are: {abs(output[0])}.")
        