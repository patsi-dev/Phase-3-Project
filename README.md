# Predicting H1N1 Vaccine Uptake

# ✨ Overview of the Project 

This project created a data-driven strategy to increase H1N1 vaccination rates by using a reliable binary classification model. The model predicted whether a person was likely to get vaccinated based on a survey of their `opinions`, `behaviors`, and `demographics.` The insights from this model can be used to help public health agencies design more `effective`, targeted vaccination campaigns.

# 🧑‍⚕️ Business and Data Understanding 

## Introduction

Vaccination is one of the most effective public health measures for preventing the spread of infectious diseases. In recent years, there has been the development of vaccines for other pandemics such as COVID-19. Vaccination not only helps individuals who have been immunised but also the community from the wider spread of the virus.

For this study, we are using data from a survey conducted in 2009 during the H1N1 influenza pandemic, also known as the "swine flu". This led to an estimated death toll worldwide in its first year of between 151,000 and 575,000. To reduce this, a vaccine was introduced in late 2009 alongside the seasonal flu that was already available.

The survey was used to understand the uptake of both vaccines. These included respondents sharing information on their health conditions, demographics, risk perception, and behaviours. By analyzing this dataset, we can better understand which factors influenced vaccine uptake. These insights can help healthcare professionals design more effective, targeted campaigns to improve vaccine acceptance and coverage in future pandemics.

**Stakeholder Audience:** The primary stakeholder for this project was a public healthcare organization.

## Problem Statement

* Public health agencies face the challenge of running vaccination campaigns with limited resources. A general, untargeted approach is inefficient and does not effectively address the unique factors that influence vaccination in different groups of people.
  
* The key challenge is the lack of a proactive approach to identifying individuals who are least likely to get vaccinated, and understanding the specific reasons behind their choices. This results in lower vaccination rates and poses a greater risk to public health.

## Dataset Choice 

The dataset used for this project was from the National 2009 H1N1 Flu Survey (NHFS), conducted by the Centers for Disease Control and Prevention (CDC). This dataset was suitable because it contained various predictors that displayed the factors influencing a person's decision to get vaccinated, such as `opinions`, `behaviors`, `demographics`, and `external influences` like a `doctor's recommendation`.

# 🧹 Data Cleaning 

The initial data exploration revealed that many columns had missing values, with some columns having extreme numbers of nulls. For example, `employment_industry`, `employment_occupation`, and `health_insurance` were missing over 12,000 entries each. To avoid losing a lot of useful data, a strategic approach to handling these missing values was necessary instead of simply dropping the rows.

# ⚙️ Modeling Approach 

The project aimed to build a binary classification model to predict whether a person would receive the H1N1 vaccine. The goal was to compare the performance of different machine learning models, such as Logistic regression and Random forest to determine the most effective technique for vaccine uptake prediction. The success of the model was measured by its ability to achieve a recall above **0.70** while maintaining a good balance between **precision** and **recall**.

# 📈 Evaluation 

The evaluation of the model focused on:

* **Model Performance:** The model was considered successful if it achieved a recall score above `0.70`.

* **Actionable Insights:** Success also included providing clear insights into the factors that were the strongest predictors of vaccine acceptance and hesitancy, which could be explained to stakeholders.

# 🎯 Conclusion 

Machine learning models were applied to predict H1N1 and seasonal flu vaccine uptake using demographic, health, and behavioral data.

- Key predictors included `doctor recommendations,` `risk perception,` and `knowledge levels`.

- The models achieved reasonable accuracy, showing potential to identify groups unlikely to vaccinate.

- Insights can guide `targeted public health campaigns,` `better resource allocation,` and `improved pandemic preparedness.`

- Results are limited to the 2009 H1N1 context and require cautious, ethical application to avoid bias or stigmatization.

Overall, predictive modeling is a valuable decision-support tool for enhancing vaccination strategies and strengthening public health resilience.

