# Academic-Data-Drift-and-Copy-Behavior-Analyzer

Day 10 challenge of python 

### 📌 Overview

This project generates student data and analyzes how it changes after modification. It mainly focuses on data drift and the difference between shallow copy and deep copy.

### 🎯 Objective
- Generate random student data (10–15 records)
- Apply changes using roll number rule
- Compare original and modified data
- Detect drift and copy issues

### ⚙️ Features
- Shallow and Deep Copy
- Data modification using sqrt
- NumPy & Pandas analysis
- Manual median calculation
- Drift detection
- Data normalization
- Final classification :
            - Stable Data
            - Minor Drift
            - Critical Drift
            - Copy Failure Detected

### Key Concept
Shallow copy shares inner data, so changes may affect original data, causing copy failure. Deep copy avoids this problem.

### How to Run
- pip install numpy pandas
- python filename.py

### 📊 Output
- Original, Shallow, Deep DataFrames
- Drift value
- Tuple (mean, drift, std_dev)
- Normalized marks
- Final classification

