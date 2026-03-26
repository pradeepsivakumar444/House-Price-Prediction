import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"C:/Users/SHAARUKESHAAN/Downloads/house_prices.csv")

# Prepare features & target
X = df[["area", "bedrooms", "bathrooms", "stories", "parking"]]
y = df["price"]

# Model training
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("🏠 House Price Prediction App")
st.write("Enter the house details to predict the price:")

area = st.number_input("Area (sqft):", min_value=500, max_value=5000, value=1500)
bedrooms = st.slider("Bedrooms:", 1, 7, 3)
bathrooms = st.slider("Bathrooms:", 1, 6, 2)
stories = st.slider("Stories:", 1, 4, 1)
parking = st.slider("Parking Spaces:", 0, 3, 1)

if st.button("Predict Price"):
    new_data = [[area, bedrooms, bathrooms, stories, parking]]
    predicted_price = model.predict(new_data)[0]
    st.success(f"Estimated House Price: ₹ {predicted_price:,.2f}")
