# Tellco-Data-Analysis

**Table of content**

 [Tellco-Data-Analysis](#Tellco-Data-Analysis)
  - [Overview](#overview)
  - [Data Source](#data-source)
  - [Installation Guide](#installation-guide)
  - [Project Structure](#project-structure)
    - [notebooks](#notebooks)
    - [data](#data)
    - [dashboard](#dashboard)
    - [models](#models)
    - [scripts](#scripts)
    - [tests](#tests)


## Overview

<p>
An investor is interested in purchasing TellCo (a telecommunication company), an existing mobile service provider in the Republic of Pefkakia.  TellCo’s current owners have been willing to share their financial information but have never employed anyone to look at their data that is generated automatically by their systems.
This project aims to provide a report to analyse opportunities for growth and make a recommendation on whether TellCo is worth buying or selling.  We will do this by analysing a telecommunication dataset that contains useful information about the customers & their activities on the network. We will deliver insights that we managed to extract to the employer through an easy to use web based dashboard and a written report. 
</p>

## Data Source
<p>
Data source For this Project was given by the employer. (It can be found in data folder)  
</p>

## Installation Guide

To install and run this project
        
            git clone https://github.com/tesfayealex/Tellco-Data-Analysis.git

            cd Tellco-Data-Analysis

            pip install -r requirements.txt
        
  
## Project Structure

### notebooks 
This folder holds the nooteboks used to process and visualize the data 
- Preprocessing and EDA - holds Data Exploratory features and visualizations
- User Engagement Analysis - holds User engagement features and visualizations
- User Experience Analytics - holds User experience features and visualizations
- User Overview Analysis - holds User overview features and visualization
- User Satisfaction Analysis - holds User satisfaction features and visualization
### data
This folder holds the data of the project (data is store on google drive using DVC)
  - Week1_challenge_data_source(CSV)
  - Others cleaned data's 
### dashboard 
This folder holds streamlit dashboard codes
### models
This folder holds models created for the project
### scripts
This folder holds script python files that modularize the codebase
### tests
This folder holds unit test files



