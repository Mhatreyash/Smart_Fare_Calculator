import streamlit as st
import plotly.graph_objects as go

def round_to_nearest_half(number):
    """Rounds a number to the nearest 0.5."""
    return round(number * 2) / 2

def calculate_fare(base_fare, cost_per_km, cost_per_minute, surge_multiplier, distance, time, minimum_fare):
    """Calculates the final taxi or rickshaw fare."""
    calculated_fare = base_fare + (distance * cost_per_km) + (time * cost_per_minute)
    surge_adjusted_fare = calculated_fare * surge_multiplier
    rounded_fare = round_to_nearest_half(surge_adjusted_fare)
    final_fare = max(rounded_fare, minimum_fare)
    return final_fare, base_fare, (distance * cost_per_km), (time * cost_per_minute), (surge_multiplier - 1) * calculated_fare if surge_multiplier > 1 else 0

# Streamlit app
st.title("Smart Fare Calculator")

st.markdown("""
Enter the details below to calculate the fare for a taxi or rickshaw ride.
The fare will be rounded to the nearest ₹0.50 and will not be below the minimum fare.
""")

# Input form
with st.form("fare_form"):
    base_fare = st.number_input("Base Fare (₹)", min_value=0.0, step=0.01, format="%.2f")
    cost_per_km = st.number_input("Cost per km (₹)", min_value=0.0, step=0.01, format="%.2f")
    cost_per_minute = st.number_input("Cost per minute (₹)", min_value=0.0, step=0.01, format="%.2f")
    surge_multiplier = st.number_input("Surge Multiplier (e.g., 1.0 for no surge)", min_value=1.0, step=0.01, format="%.2f")
    distance = st.number_input("Distance (km)", min_value=0.0, step=0.01, format="%.2f")
    time = st.number_input("Time (minutes)", min_value=0.0, step=0.01, format="%.2f")
    minimum_fare = st.number_input("Minimum Fare (₹)", min_value=0.0, step=0.01, format="%.2f")
    submit_button = st.form_submit_button("Calculate Fare")

# Process form submission
if submit_button:
    try:
        final_fare, base, distance_cost, time_cost, surge_cost = calculate_fare(
            base_fare, cost_per_km, cost_per_minute, surge_multiplier, distance, time, minimum_fare
        )

        # Fare breakdown table
        st.subheader("Fare Breakdown")
        breakdown = [
            {"Component": "Base Fare", "Amount (₹)": f"{base:.2f}"},
            {"Component": "Distance Charge", "Amount (₹)": f"{distance_cost:.2f}"},
            {"Component": "Time Charge", "Amount (₹)": f"{time_cost:.2f}"}
        ]
        if surge_cost > 0:
            breakdown.append({"Component": "Surge Charge", "Amount (₹)": f"{surge_cost:.2f}"})
        breakdown.append({"Component": "Total Fare", "Amount (₹)": f"{final_fare:.2f}"})

        st.table(breakdown)

        # Visualization (Pie Chart)
        st.subheader("Fare Breakdown Visualization")
        labels = [item["Component"] for item in breakdown[:-1]]  # Exclude Total Fare for chart
        values = [float(item["Amount (₹)"]) for item in breakdown[:-1]]
        fig = go.Figure(data=[
            go.Pie(labels=labels, values=values, textinfo='label+percent',
                   marker=dict(colors=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']))
        ])
        fig.update_layout(title_text="Fare Component Distribution")
        st.plotly_chart(fig)

    except ValueError:
        st.error("Invalid input. Please enter numeric values.")
