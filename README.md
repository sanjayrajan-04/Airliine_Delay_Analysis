Airline Delay Analysis Project  

## 📌 Overview  
Flight delays are one of the most common challenges in the aviation industry, impacting both passengers and airlines. This project explores airline flight data to identify trends, patterns, and insights related to delays. Using Python for data cleaning, exploratory data analysis (EDA), and visualization, we uncover how different factors such as airlines, time of travel, and routes contribute to delays.  

The final outcomes include:  
* Cleaned datasets for reproducible analysis  
* Visual EDA results (saved as plots)  
* An interactive dashboard for business insights  


## Tools Used
* Excel (Data Cleaning)
* SQL (Data Transformation)
* Python (Exploratory Analysis)
* Power BI (Dashboard & Reporting)


## Datasets Used  
1. Raw Flight Details Dataset ("flight_details.csv")
   - Original dataset containing flight information such as airline, departure, arrival, delays, and cancellations.  

2. Cleaned Dataset ("flight_details_cleaned.csv")  
   - Preprocessed version of the raw dataset.  
   - Cleaning steps included: handling missing values, removing duplicates, standardizing airline names, formatting dates/times, and creating new derived columns such as Delay_Category.  

3. Final Analysis Dataset ("final_flight_data.csv")
   - Processed dataset after performing EDA.  
   - Used for dashboard building and sharing results.  



# Exploratory Data Analysis (EDA)  
EDA was performed in Jupyter Notebook using libraries such as Pandas, Matplotlib, and Seaborn Key analyses include:  

* Average departure delays by airline  
* Distribution of on-time vs delayed flights  
* Monthly delay trends and seasonality  
* Route-wise delay patterns  
* Export of final cleaned dataset  

All plots were saved in:  EDA_Analysis_ipynb/EDA_screenshots/

# Dashboard: Airline Analysis Dashboard  

An interactive dashboard was built using the final dataset.  
* Provides visual summaries of delay patterns.  
* Helps airlines and analysts quickly understand operational bottlenecks.  
* Useful for decision-making and improving service quality.  

The dashboard is Airline Analysis Dashboard.  



## Project Structure  

Airline_Delay_Analysis
1) Datasets
* flight_details.csv                # Raw dataset
* flight_details_cleaned.csv        # Cleaned dataset used in analysis
* final_flight_data.csv             # Final dataset for dashboard

2) EDA_Analysis_ipynb/
* flight_analysis_fixed.ipynb       # Jupyter Notebook (EDA + cleaning)
* EDA_screenshots                   # Saved plots from EDA

3) Dashboards
* Airline_Analysis_Dashboard        # Final dashboard
*  README.md                         # Project documentation


##  How to Run the Project  
1. Clone the repository or download the project folder.

2. Install required Python libraries and requirements 
   
3. Open the Jupyter Notebook:  Open jupyter notebook flight_analysis_fixed.ipynb

4. Run all cells to reproduce the EDA and generate plots.  


## Key Insights 

- Certain airlines experience consistently higher delays.  
- Delays tend to peak in specific months/seasons, showing seasonality in flight disruptions.  
- Majority of flights are on-time, but even a small percentage of delays has a significant impact on passengers.  
- The dashboard provides a business-friendly interface for monitoring and exploring these trends.  


## 🚀 Conclusion 

This project demonstrates how data analysis in Python can be used to derive meaningful insights from real-world flight data. The methodology covers the complete pipeline:  
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Visual storytelling with plots and dashboards  
The outcomes are valuable for airlines, regulators, and passengers to understand and minimize delays, ultimately improving the air travel experience.  

