# API to Redshift Data Pipeline | End-to-End ETL Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AWS](https://img.shields.io/badge/AWS-S3%2C%20Redshift-orange)
![Pandas](https://img.shields.io/badge/Data_Processing-Pandas-brightgreen)

A production-ready data pipeline that extracts weather data from an API, processes it, and loads it into Redshift for analytics. Designed to showcase core data engineering skills.

---

## Key Features
- **API Integration**: Real-time data extraction from OpenWeatherMap API
- **Data Processing**: Cleaning, transformation, and feature engineering with pandas
- **Cloud Storage**: Raw/processed data partitioning in AWS S3 (data lake pattern)
- **Data Warehousing**: Optimized Redshift schema design and loading
- **Infrastructure**: AWS IAM roles and security best practices

---

## 📊 Pipeline Architecture
```mermaid
graph LR
    A[API Extraction] --> B(Raw S3 Zone)
    B --> C[Data Processing]
    C --> D(Processed S3 Zone)
    D --> E[Redshift Loading]
    E --> F[Analytics Dashboard]
