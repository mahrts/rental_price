# 🏙️ NYC Rental Price ML Pipeline

This is a simple end-to-end **MLOps pipeline** for predicting short-term rental prices in NYC.  
Built with a focus on **reproducibility, and automation**

The w&b experiments tracking can be found at:
[w&b experiments tracking](https://wandb.ai/rental_price/nyc_airbnb?nw=nwusermahrts)

---

## 🚀 Overview

This project simulates a real-world ML system where new rental data arrives weekly.  
The pipeline automatically:

- 🧹 Download, Cleans and validates datasets (both deterministic and non-deterministic tests)
- 🔀 Splits data into train/validation/test sets
- 🌲 Trains a Random Forest model
- ⚙️ Performs hyperparameter tuning
- 📊 Tracks experiments with Weights & Biases
- 🏆 Selects and promotes the best model
- 🧪 Tests model performance before deployment

### 🧱 Included Pipeline Architecture
```bash
Download  → Simple Cleaning → Validation → Train / Val / Test Split → Model Training (Random Forest) → Hyperparameter Tuning → Model Selection → Testing → Production Model
```

---

## 👨‍💻 Contributions

- ✅ Fix dependencies and chained **modular, reusable ML pipeline** from the /src folder fo main.py
- ✅ Updated **data cleaning component** with configurable thresholds
- ✅ Integrated **experiment tracking (W&B)**
- ✅ Implemented **Random Forest pipeline** on sklearn
- ✅ Performed manual **hyperparameter tuning via Hydra sweap and w&b**
- ✅ Ensured that pipeline runs smoothly for **continuous retraining and reproducibility**
- ✅ Enforcing some pep8 coding style


---

## 🛠️ Tools

- **ML Pipeline**: MLflow  
- **Experiment Tracking**: Weights & Biases 
- **Config configuration**: Hydra  
- **Model**: Scikit-learn (Random Forest)  
- **Environment**: Conda + Python 3.13 

---

## ⚙️ Example setup
Running the code requires w&b login.
```bash
wandb login --relogin [YOUR_WANDB_API_KEY]
```
### Example for retraining
Assume an new data artifact [NEW_TRAINING_DATA.csv] arrived on w&b, then the model with version [my_version] (e.g. 1.0.3) can be retrained with:

```bash
mlflow run https://github.com/mahrts/rental_price.git -v [my_version] -P hydra_options="etl.sample='[NEW_TRAINING_DATA.csv]'"
```
