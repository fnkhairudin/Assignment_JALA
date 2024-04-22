Assignment Test of JALA Data Scientist Job Role
=========

Table of Contents
-------------
* [Context](#context)
* [Problem Statement](#problem-statement)
* [Task](#task)
* [Goals](#goals)
* [Analytics Approach](#analytic-approach)
* [MLflow Tracking Experiment](#mlflow-tracking-experiment)
* [Project Organization](#project-organization)

**Context**:
------------
**Jala Tech** is an Indonesian startup company that tries to make significant strides in the shrimp industry. Jala serves as a digital ecosystem enabler for the shrimp industry value chain. Here’s what we do:
1. Comprehensive Solutions: Jala provides end-to-end solutions to streamline the shrimp farming process. These solutions aim to enhance productivity, efficiency, and sustainability throughout the entire shrimp cultivation cycle.
2. Revolutionizing Shrimp Farming: Jala’s offerings include advanced technology services such as data analysis and water quality monitoring. By leveraging these tools, they empower shrimp farmers to make informed decisions and optimize their operations.
3. Ecosystem Building: Jala builds an ecosystem within the shrimp industry, helping farmers create efficiency and gain wider and easier market access. Their goal is to increase sustainable productivity in shrimp farming.

The farm management system (JALA App) is one of the solutions that we provide for shrimp farmers. With the JALA App, farmers can manage their shrimp farms better. Farmers can record their data digitally, analyze the data that they have collected, and receive predictive analytics of their shrimp cultivation.

**Problem Statement**:
------------
Asumsi saat ini Petambak masih melakukan _monitoring_ kegiatan mulai dari awal menyebar benur udang hingga memanen udang masih dilakukan secara maunal, belum secara digitalisasi (Realtime) atau memanfaatkan teknologi, sehingga hasil **panen masih belum maksimal**.

**Task**:
------------
1. Evaluate the completeness of data
2. Calculate SR and average growth rate (ADG) of shrimp per cultivation cycle
3. Predictive modeling:
    
    a. Survival Rate (in percentage) forecast for the end of cultivation or at the
    pointed day of cultivation (You need to make sure that the model
    performs well when the cultivation cycle is still ongoing)

    b. Average Body Weight of Shrimp (in grams) forecast
    
    c. Biomass (in kilograms) forecast
    
    d. Revenue forecast that estimates the value of the shrimp when it is
    harvested.
4. Based on the predictive model that you’ve made, Infer what features/variables
that important to make predictions
5. Based on the data that you analyzed, make recommendations on how shrimp
farming should be done to achieve optimal results
6. Deployment that covers:
    
    a. Feature store of engineered features that you made during development
    
    b. Source code (Please upload it into GitHub, and include clear instructions
    on how to set the service and documentation of the API request)

**Goals**:
------------
Farmers can record their data digitally, analyze the data that they have collected, and receive predictive analytics of their shrimp cultivation.

**Analytic Approach**:
------------
With the value that we’re trying to give to farmers, we need to develop accurate robust **predictive analytics** that our farmers can rely on.

MLflow Tracking Experiment
------------
https://dagshub.com/fnkhairudin/Assignment_JALA.mlflow

Project Organization
------------
    ├── README.md          <- business understanding until conclusion and recommendation
    ├── data
    |   ├── processed      <- final data for analysis or modeling
    │   └── raw            <- original data
    │
    ├── model              <- final model
    │
    ├── notebooks          <- Jupyter notebooks
    │                         
    ├── reports            <- guidance of assignment test
    │
    └── src                <- get experiment id for MLflow tracking experiment
    └── requirements.txt   <- requirements file for reproducing the analysis environment, e.g.
                            generated with `pip freeze > requirements.txt`