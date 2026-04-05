# 🏙️ NYC Rental Price ML Pipeline

![Weights & Biases](https://wandb.ai/rental_price/nyc_airbnb?nw=nwusermahrts)


This is a simple end-to-end **MLOps pipeline** for predicting short-term rental prices in NYC.  
Built with a focus on **reproducibility, and automation**.

---

## 🚀 Overview

This project simulates a real-world ML system where new rental data arrives weekly.  
The pipeline automatically:

- 📥 Load new data
- 🧹 Cleans and validates datasets (both deterministic and non-deterministic tests)
- 🔀 Splits data into train/validation/test sets
- 🌲 Trains a Random Forest model
- ⚙️ Performs hyperparameter tuning
- 📊 Tracks experiments with Weights & Biases
- 🏆 Selects and promotes the best model
- 🧪 Tests model performance before deployment

---

## 👨‍💻 My Contributions

- ✅ Fix dependencies and chained **modular, reusable ML pipeline** from the /src folder fo main.py
- ✅ Updated **data cleaning component** with configurable thresholds
- ✅ Integrated **experiment tracking (W&B)**
- ✅ Developed **Random Forest training pipeline**
- ✅ Performed manual **hyperparameter tuning via Hydra sweap and w&b**
- ✅ Ensured that pipeline runs smoothly for **continuous retraining**

---

## 🧱 Included Pipeline Architecture
```bash
Raw Data → Cleaning → Validation → Train / Val / Test Split → Model Training (Random Forest) → Hyperparameter Tuning → Model Selection → Testing → Production Model
```


---

## 🛠️ Tools

- **ML Pipeline**: MLflow  
- **Experiment Tracking**: Weights & Biases  
- **Configuration**: Hydra  
- **Model**: Scikit-learn (Random Forest)  
- **Environment**: Conda + Python 3.13  

---

## ⚙️ Setup

```bash
# Clone repository
git clone https://github.com/<your-username>/build-ml-pipeline-for-short-term-rental-prices.git
cd build-ml-pipeline-for-short-term-rental-prices

# Create environment
conda env create -f environment.yml
conda activate nyc_airbnb_dev

# Login to Weights & Biases
wandb login
```
