E-commerce Sales Analysis Project

Project Overview
This project is a comprehensive analysis of an e-commerce dataset, aimed at uncovering insights that can drive business decisions. From cleaning and preparing the data to building predictive models, this project explores multiple facets of the business, including sales distribution, product popularity, and customer behavior.

Key Objectives
1. Data Cleaning and Preparation
- Cleaned and structured the dataset by handling missing values, correcting data types, and removing erroneous records.
- Utilized Python for data cleaning and feature engineering, ensuring a robust dataset for analysis.
2. Sales Distribution Analysis
- Analyzed and visualized sales across different countries to identify key markets and their contributions to overall revenue.
- Used Tableau to create interactive visualizations of sales trends, although challenges with Tableau Public prevented full online publication.
3. Product Popularity Analysis
- Identified top-performing products by total sales and quantity sold, providing insights into what drives the business.
4. Customer Segmentation
- Segmented customers based on their purchasing behavior, categorizing them into Low-Value, Mid-Value, and High-Value groups using RFM (Recency, Frequency, Monetary) analysis.
5. Time Series Analysis
- Explored sales trends over time, identifying patterns, seasonality, and growth trends that can inform strategic planning.
- Implemented ARIMA models in Python to forecast future sales trends.
6. Feature Engineering
- Created new features, such as Customer Lifetime Value (CLV) and RFM metrics, to enhance predictive modeling and customer segmentation.
7. Predictive Modeling
- Built models for sales forecasting using time series analysis, focusing on providing actionable insights for business strategy.
8. Visualization and Dashboard Creation
- Developed interactive dashboards in Tableau Public that present key findings in a clear and accessible way.
- Captured images of key visualizations for inclusion in the portfolio due to challenges with Tableau Public's web version.

Challenges and Solutions
1. Data Integrity
- Addressed issues like mixed data types and missing values to ensure the dataset was reliable for analysis.
2. Technical Hurdles
- Overcame challenges with installing and configuring necessary Python packages in Visual Studio 2022.
- Managed limitations with Tableau Public by saving images of the dashboards and visualizations, ensuring the work could still be showcased.
3. Filter Selection
- Initially started with a StockCode filter, but realized that a date range filter would be more insightful.
- Solution: Switched to using the InvoiceDate field for filtering and adjusted the dashboard to make the analysis more meaningful.
4. Python Errors
- Faced issues with the Recency calculation and model fitting in Python.
- Solution: Correctly defined the current_date for Recency and adjusted the parameters for the forecasting models to ensure they ran smoothly.
5. Dashboard Layout and Design
- Ensuring that the dashboard was both visually appealing and easy to navigate required careful consideration of layout and filter placement.
- Solution: Used containers and alignment tools in Tableau Public to organize everything in a clean, logical way.

Expected Outcomes
1. Business Insights
- Gain a deep understanding of sales performance, product trends, and customer behavior, providing actionable insights for the business.
2. Predictive Power
- Developed models that can accurately forecast sales, predict customer behavior, and recommend products, helping to shape business strategy.
3. Comprehensive Reporting
-Delivered a full set of visualizations, models, and reports that can be used to present findings to stakeholders or included in a professional portfolio.

How to Use This Project
1. Clone the Repository
git clone https://github.com/yourusername/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis

2. Set Up the Environment
Install the required Python packages using:
pip install -r requirements.txt

3. Run the Analysis
- Follow the code and instructions provided to replicate the analysis, explore the data, and generate insights.

5. Explore the Results
- Review the visualizations and models created to understand the business insights derived from the data.
- Note that images of the key visualizations are included due to the inability to publish the full dashboard online.

Conclusion
This project showcases the entire process of analyzing e-commerce data, from initial cleaning to advanced modeling and visualization. It serves as a valuable resource for understanding how data-driven decisions can be made in a business context. The inclusion of both Python code and Tableau visualizations highlights the integration of data manipulation and visual storytelling, even in the face of technical challenges.
