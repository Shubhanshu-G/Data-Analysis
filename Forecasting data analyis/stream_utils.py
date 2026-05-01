import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent

@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "combined_preprocessed_dataset.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    return df

def get_rp_table():
    years = list(range(2014, 2026))
    rp = [1.2, 1.4, 1.7, 2.1, 2.8, 3.6, 4.5, 5.0, 5.2, 6.3, 7.5, 9.0]
    ramp = [1800, 1850, 1900, 2000, 2200, 2400, 2600, 2700, 2800, 3000, 3300, 3600]
    std_dev = [9000, 9200, 9500, 9800, 10200, 10800, 11500, 12000, 12500, 13200, 14000, 15000]
    
    table = pd.DataFrame({
        "Year": years,
        "Renewable Penetration (%)": rp,
        "Mean Ramp (MW/hour)": ramp,
        "Net Load Std Dev (MW)": std_dev
    })
    return table

def plot_raw_generation(df):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(14, 5))
    # We plot downsampled data (daily) to make the dashboard load much faster without losing the trend
    df_daily = df[['load_mw', 'solar_mw', 'wind_mw']].resample('D').mean()
    
    ax.plot(df_daily.index, df_daily['load_mw'], label='Load', color='gray', alpha=0.7)
    ax.plot(df_daily.index, df_daily['solar_mw'], label='Solar', color='orange')
    ax.plot(df_daily.index, df_daily['wind_mw'], label='Wind', color='blue')
    
    ax.set_title("PJM RTO Daily Average Generation & Load (MW)")
    ax.set_xlabel("Time")
    ax.set_ylabel("MW")
    ax.legend()
    plt.tight_layout()
    return fig

def plot_net_load(df):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(14, 5))
    df_daily = df[['net_load_mw']].resample('D').mean()
    
    ax.plot(df_daily.index, df_daily['net_load_mw'], color='red')
    ax.set_title("PJM RTO Daily Average Net Load (MW)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Net Load (MW)")
    plt.tight_layout()
    return fig

def plot_hourly_profile(df):
    sns.set_style("whitegrid")
    hourly_profile = df.groupby('hour')[['load_mw','net_load_mw','solar_mw','wind_mw']].mean()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hourly_profile.index, hourly_profile['load_mw'], label='Load', color='black')
    ax.plot(hourly_profile.index, hourly_profile['net_load_mw'], label='Net Load', color='red', linestyle='--')
    ax.plot(hourly_profile.index, hourly_profile['solar_mw'], label='Solar', color='orange')
    ax.plot(hourly_profile.index, hourly_profile['wind_mw'], label='Wind', color='blue')
    
    ax.set_title("Average Hourly Profile")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("MW")
    ax.set_xticks(range(0, 24, 2))
    ax.legend()
    plt.tight_layout()
    return fig

def get_xgboost_rp_impact_table():
    rp_increase = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    rmse = [4034.85, 4040.07, 4070.34, 4098.99, 4170.65, 4163.07, 4199.91, 4249.15, 4264.76, 4335.46, 4370.56]
    nrmse = [4.69, 4.70, 4.73, 4.76, 4.85, 4.84, 4.88, 4.94, 4.96, 5.04, 5.08]
    
    table = pd.DataFrame({
        "Renewable Increase (%)": rp_increase,
        "RMSE": rmse,
        "NRMSE (%)": nrmse
    })
    return table

