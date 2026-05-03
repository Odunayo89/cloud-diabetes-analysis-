# Cloud-Based Biomedical Data Analysis (AWS EC2 + S3 + Python)

## Overview
This project demonstrates an end-to-end cloud-based data workflow for processing and analyzing a biomedical dataset using AWS EC2 and S3.

## Objective
To simulate a real-world computational biology workflow involving data ingestion, cleaning, processing, and analysis in a cloud environment.

## Dataset
Pima Indians Diabetes Dataset (public biomedical dataset)

## Workflow
1. Data ingestion from external source (GitHub)
2. Data cleaning and formatting (added headers)
3. Data exploration using Linux tools (wc, grep)
4. Data subsetting (diabetic vs non-diabetic patients)
5. Statistical analysis using Python (pandas)
6. Cloud storage of results using AWS S3

## Tools & Technologies
- AWS EC2 (compute)
- AWS S3 (storage)
- Linux (bash)
- Python (pandas)

## Key Results
- Total samples: 768
- Diabetic patients: 268
- Non-diabetic patients: 500
- Generated summary statistics and dataset subsets

## Skills Demonstrated
- Cloud computing workflow (EC2 + S3)
- Linux command-line data processing
- Data cleaning and transformation
- Python-based data analysis
- Reproducible project structuring

## How to Run
```bash
python analyze_diabetes.py
