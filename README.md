# Predicting H1N1 Vaccine Uptake

# ✨ **Business Understanding**

## Introduction

Vaccination is one of the most effective public health measures for preventing the spread of infectious diseases. In recent years, there has been the development of vaccines for other pandemics such as COVID-19. Vaccination not only helps individuals who have been immunised but also the community from the wider spread of the virus.

For this study, we are using data from a survey conducted in 2009 during the H1N1 influenza pandemic, also known as the "swine flu". This led to an estimated death toll worldwide in its first year of between 151,000 and 575,000. To reduce this, a vaccine was introduced in late 2009 alongside the seasonal flu that was already available.

The survey was used to understand the uptake of both vaccines. These included respondents sharing information on their health conditions, demographics, risk perception, and behaviours. By analyzing this dataset, we can better understand which factors influenced vaccine uptake. These insights can help healthcare professionals design more effective, targeted campaigns to improve vaccine acceptance and coverage in future pandemics.

## Problem Statement

* Public health agencies face the challenge of running vaccination campaigns with limited resources. A general, untargeted approach is inefficient and does not effectively address the unique factors that influence vaccination in different groups of people.
  
* The key challenge is the lack of a proactive approach to identifying individuals who are least likely to get vaccinated, and understanding the specific reasons behind their choices. This results in lower vaccination rates and poses a greater risk to public health.

## Objectives

* **Predict Vaccine Acceptance:** Create a classification model to predict whether a person will receive the H1N1 vaccine based on their past behavior.

* **Identify At-Risk Populations:** Accurately segment the population to predict which individuals are highly likely to remain unvaccinated for H1N1.

* **Understand Key Drivers:** Determine the most influential factors, such as opinions, behaviors, and demographics, that predict vaccine hesitancy and acceptance.

* **Compare Model Performance:** Evaluate and compare different machine learning models to find the most effective technique for vaccine uptake prediction.

# 📊 Dataset

The dataset is from the National 2009 H1N1 Flu Survey (NHFS), publicly available from the Centers for Disease Control and Prevention (CDC). It contains survey responses from 26,707 individuals in the U.S., with each row detailing a person's attitudes, beliefs, and behaviors toward the H1N1 and seasonal flu vaccines. The data includes:

* `Opinions & Knowledge:` Perceived risk, effectiveness, and side effects.

* `Behaviors:` Such as face mask use, hand washing, and avoidance of large gatherings.

* `Demographics:` Including age, income, race, health insurance, and geographic region.

* `External Influence:` Doctor's recommendations and employment in healthcare.

# 💻 Methodology

This project follows a standard data science methodology:

**Data Loading and Merging:** The features and target datasets were loaded and merged based on respondent_id. The resulting dataset has 26,707 rows and 38 columns.

**Exploratory Data Analysis (EDA):** The data was inspected for types, non-null counts, and missing values. It was noted that several columns, including employment_industry, employment_occupation, and health_insurance, have a high percentage of missing values, which will require a smart imputation strategy.

**Data Preprocessing and Modeling:**

* Missing values will be handled using an imputation method.

* The data will be split into training and testing sets.

* Categorical features will be one-hot encoded, and numerical features will be scaled.

* Classification models, such as Logistic Regression and Random Forest Classifier, will be trained and evaluated.

**Model Evaluation and Interpretation:** The models will be evaluated based on a recall score greater than 0.70 while maintaining a good balance with precision. The goal is to provide actionable insights by identifying the most influential features.

# 📈 Visualizations

<img width="684" height="395" alt="image" src="https://github.com/user-attachments/assets/3bcc5924-fcc3-4509-8c05-98c309064f10" />

<img width="688" height="332" alt="image" src="https://github.com/user-attachments/assets/e89b4eb2-4f8b-4221-9b84-3cb2e471092b" />

<img width="540" height="494" alt="image" src="https://github.com/user-attachments/assets/16d90913-b902-4530-9524-6c696691bc54" />

<img width="395" height="315" alt="image" src="https://github.com/user-attachments/assets/c0a9e07a-cb1a-400c-bc36-ebd359128cb0" />



# 🏁 Conclusion


* Key predictors included doctor recommendations, risk perception, and knowledge levels.

* The models achieved reasonable accuracy, showing potential to identify groups unlikely to vaccinate.

* Insights can guide targeted public health campaigns, better resource allocation, and improved pandemic preparedness.

* Results are limited to the 2009 H1N1 context and require cautious, ethical application to avoid bias or stigmatization.

  

# 💡 Business Recommendations

Based on the model's insights, the public healthcare organization can:

* Target outreach programs to demographic groups identified as at-risk or vaccine-hesitant.

* Focus on key influential factors, such as increasing public knowledge about vaccine effectiveness and promoting doctor recommendations, to improve vaccination rates.

* Allocate resources more efficiently by concentrating on the segments of the population most likely to remain unvaccinated.

# ➡️ Next Steps

* Explore more advanced feature engineering techniques to improve model performance.

* Investigate different machine learning models and ensemble methods (e.g., Gradient Boosting) to see if they can achieve better recall and precision scores.


# 🔧 Technologies Implemented

* Python

* Pandas

* NumPy

* Matplotlib

* Seaborn

* Scikit-learn
