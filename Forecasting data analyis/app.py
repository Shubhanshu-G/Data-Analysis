import streamlit as st
import pandas as pd
from stream_utils import load_data, get_rp_table

# ----------------------------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="Net Load Forecasting Dashboard",
    layout="wide"
)

# ----------------------------------------------------
# 2. HEADER
# ----------------------------------------------------
st.title("Net Load Forecasting & Renewable Penetration")
st.markdown("A simple dashboard for exploring power grid net load dynamics under increasing renewable energy integration.")

# Load Data
with st.spinner("Loading dataset..."):
    try:
        df = load_data()
        data_loaded = True
    except Exception as e:
        st.error(f"Error loading data: {e}")
        data_loaded = False

if data_loaded:
    # ----------------------------------------------------
    # 3. KPI METRICS
    # ----------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)
    
    avg_load = df['load_mw'].mean()
    avg_net_load = df['net_load_mw'].mean()
    avg_rp = df['renewable_penetration'].mean() * 100
    peak_net_load = df['net_load_mw'].max()
    
    col1.metric("Average System Load", f"{avg_load:,.0f} MW")
    col2.metric("Average Net Load", f"{avg_net_load:,.0f} MW")
    col3.metric("Avg Renewable Penetration", f"{avg_rp:.1f} %")
    col4.metric("Peak Net Load", f"{peak_net_load:,.0f} MW")
    
    st.markdown("---")
    
    # ----------------------------------------------------
    # 4. TABS FOR VISUALIZATIONS
    # ----------------------------------------------------
    tab1, tab2, tab3, tab4 = st.tabs([
        "Exploratory Data Analysis", 
        "Renewable Trends", 
        "Forecasting Insights",
        "Dataset"
    ])
    
    with tab1:
        from stream_utils import plot_raw_generation, plot_net_load, plot_hourly_profile
        
        st.subheader("System Generation and Load Dynamics")
        st.pyplot(plot_raw_generation(df), use_container_width=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.pyplot(plot_net_load(df), use_container_width=True)
        with col_b:
            st.pyplot(plot_hourly_profile(df), use_container_width=True)
            
        st.markdown("### Representative Shift (2014 vs 2025)")
        st.image("Plots/fig_Y_final.png", caption="Representative Daily Net Load Profiles (2014 vs 2025)", use_container_width=True)
            
    with tab2:
        st.subheader("Renewable Penetration (RP) Impact")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.image("Plots/fig_RP_trend.png", caption="Annual Average Renewable Penetration in PJM (2014–2025)", use_container_width=True)
        with col_b:
            st.image("Plots/fig6_final.png", caption="Renewable Penetration Regime Segmentation", use_container_width=True)
        
        st.markdown("### Projected Renewable Penetration Scenarios (2014-2025)")
        rp_table = get_rp_table()
        st.dataframe(rp_table, use_container_width=True)
        
    with tab3:
        st.subheader("Forecasting Model Performance")
        
        from stream_utils import get_xgboost_rp_impact_table
        st.markdown("### XGBoost Performance under increasing RP")
        xgb_table = get_xgboost_rp_impact_table()
        st.dataframe(xgb_table, use_container_width=True)
        
        st.image("Plots/fig7_final.png", caption="Actual vs Predicted Net Load (1-Hour Ahead)", use_container_width=True)
        
        col_c, col_d = st.columns(2)
        with col_c:
            st.image("Plots/fig11_feature_importance_final.png", caption="XGBoost Feature Importance", use_container_width=True)
        with col_d:
            st.image("Plots/fig9_final.png", caption="NRMSE vs Forecast Horizon", use_container_width=True)
            
        col_e, col_f = st.columns(2)
        with col_e:
            st.image("Plots/fig10_boxplot.png", caption="Forecast Error Distribution by RP Regime", use_container_width=True)
        with col_f:
            st.image("Plots/fig8_final_with_legend.png", caption="Diebold–Mariano Loss Differential Distribution", use_container_width=True)
        
    with tab4:
        st.subheader("Final Combined Dataset")
        st.markdown("Preview of the final preprocessed data used for the forecasting models.")
        
        # Show first 1000 rows to keep it fast
        st.dataframe(df.head(1000), use_container_width=True)
        
        # Download button
        with open("combined_preprocessed_dataset.csv", "rb") as file:
            btn = st.download_button(
                label="Download Full Dataset",
                data=file,
                file_name="combined_preprocessed_dataset.csv",
                mime="text/csv"
            )
            
    # ----------------------------------------------------
    # 5. CONCLUSIONS
    # ----------------------------------------------------
    st.markdown("---")
    st.markdown("### Important Conclusions")
    st.markdown("""
    - **Duck Curve Deepening:** The average hourly profile clearly demonstrates the "duck curve" effect. Mid-day net load drops significantly due to peak solar generation, followed by steep ramping requirements in the early evening.
    - **Volatility Increases with RP:** As seen in the scenario tables, higher Renewable Penetration (RP) directly correlates with increased Net Load Standard Deviation and much higher ramping requirements.
    - **Forecasting Challenges:** High RP regimes inherently increase the prediction error. Traditional models (like SARIMA) struggle with this volatility, whereas machine learning models (XGBoost) capture complex, non-linear weather and temporal patterns much better.
    - **Crucial Features:** Short-term historical lags (Lag 1) and 24-hour cycles (Lag 24) are the strongest predictors for short-term forecasting, confirming that power grid behavior is highly autoregressive.
    """)
    
else:
    st.warning("Please ensure 'combined_preprocessed_dataset.csv' is in the same directory.")
