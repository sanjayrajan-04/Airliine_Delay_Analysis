import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Airline and Airport Data
AIRLINES = ["Emirates", "Etihad", "Qatar Airways", "FlyDubai", "Air India", "British Airways", 
            "Lufthansa", "Delta", "American Airlines", "Singapore Airlines"]
AIRPORTS = ["DXB", "AUH", "JFK", "LHR", "SIN", "DOH", "CDG", "BKK", "ORD", "KWI", "DEL", "BOM", 
            "FRA", "SYD", "PEK", "HND", "ICN", "SFO", "LAX", "DFW"]
CANCELLATION_REASONS = ["Weather", "Technical", "Air Traffic", "Security", "Staff Issue", ""]

def generate_flight_data(num_rows=1000):
    data = []
    for _ in range(num_rows):
        # Flight date (within last 1 year)
        flight_date = fake.date_between(start_date='-1y', end_date='today')
        
        # Random airline and airports
        airline = np.random.choice(AIRLINES)
        origin, dest = np.random.choice(AIRPORTS, 2, replace=False)
        
        # Scheduled departure/arrival (HHMM format)
        crs_dep_time = f"{np.random.randint(0, 23):02d}{np.random.randint(0, 59):02d}"
        crs_arr_time = f"{np.random.randint(0, 23):02d}{np.random.randint(0, 59):02d}"
        
        # Departure delay (0-120 mins, 10% chance of negative delay)
        dep_delay = np.random.randint(0, 120) if np.random.random() > 0.1 else np.random.randint(-20, 0)
        
        # Actual departure time
        dep_time = (datetime.strptime(crs_dep_time, "%H%M") + timedelta(minutes=dep_delay)).strftime("%H%M")
        
        # Cancellation (2% chance)
        cancelled = 1 if np.random.random() < 0.02 else 0
        cancellation_reason = np.random.choice(CANCELLATION_REASONS) if cancelled else ""
        
        # Arrival delay (based on departure delay + extra variance)
        arr_delay = dep_delay + np.random.randint(-10, 30)
        arr_time = (datetime.strptime(crs_arr_time, "%H%M") + timedelta(minutes=arr_delay)).strftime("%H%M")
        
        data.append({
            "FL_DATE": flight_date,
            "OP_CARRIER": airline,
            "ORIGIN": origin,
            "DEST": dest,
            "CRS_DEP_TIME": crs_dep_time,
            "DEP_TIME": dep_time,
            "DEP_DELAY": dep_delay,
            "CRS_ARR_TIME": crs_arr_time,
            "ARR_TIME": arr_time,
            "ARR_DELAY": arr_delay,
            "CANCELLED": cancelled,
            "CANCELLATION_CODE": cancellation_reason
        })
    
    df = pd.DataFrame(data)
    
    # Rename columns as per your requirement
    column_rename = {
        "FL_DATE": "Flight_Date",
        "OP_CARRIER": "Airline_Code",
        "ORIGIN": "Origin_Airport",
        "DEST": "Destination_Airport",
        "CRS_DEP_TIME": "Scheduled_Departure",
        "DEP_TIME": "Actual_Departure",
        "DEP_DELAY": "Departure_Delay",
        "CRS_ARR_TIME": "Scheduled_Arrival",
        "ARR_TIME": "Actual_Arrival",
        "ARR_DELAY": "Arrival_Delay",
        "CANCELLED": "Cancelled",
        "CANCELLATION_CODE": "Cancellation_Reason"
    }
    df = df.rename(columns=column_rename)
    
    return df

# Generate 10,000 records
flight_data = generate_flight_data(10000)

# Save to CSV
flight_data.to_csv("flight_details.csv", index=False)
print("CSV file generated: flight_details.csv")