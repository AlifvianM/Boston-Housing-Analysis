import streamlit as st
import requests


st.title("House Price Prediction")
st.image("assets/modern house plan - carbondale__05776.original.jpg")

st.divider()

with st.form('house-price-form'):

    square_feet= st.number_input('Square Feet', min_value=0, help='square')
    bedrooms= st.number_input('Bedrooms', min_value=0, help='count of bedrooms')
    bathrooms= st.number_input('Bathrooms', min_value=0, help='count of bedrooms')
    year_built= st.number_input('YearBuilt', min_value=0, help='when house was built')
    neighborhood_rural= st.checkbox('Rural Neighborhood')
    neighborhood_suburb= st.checkbox('Suburb Neighborhood')
    neighborhood_urban= st.checkbox('Urban Neighborhood')

    submit = st.form_submit_button('predict')

    if submit:
        neighborhood_rural = 1 if neighborhood_rural == True else 0
        neighborhood_suburb = 1 if neighborhood_suburb == True else 0
        neighborhood_urban = 1 if neighborhood_urban == True else 0

        print(neighborhood_rural, neighborhood_suburb, neighborhood_urban)

        with st.spinner("Predicting....."):
            result = requests.post('http://api_service:8000/predict/', json={
                "SquareFeet" : square_feet, 
                "Bedrooms" : bedrooms,
                "Bathrooms" : bathrooms,
                "YearBuilt" : year_built,
                "Neighborhood_Rural": neighborhood_rural, 
                "Neighborhood_Suburb" : neighborhood_suburb,
                "Neighborhood_Urban" : neighborhood_urban
            }).json()

        st.info(f'Your House Price is {result["predicted_price"]}')