import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

# Setup Page Configuration
st.set_page_config(
    page_title="Prompt Evaluation Dashboard",
    # page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for light tone
st.markdown("""
    <style>
    .main {
        background-color: Gray98;
    }
    h1, h2, h3 {
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(" Prompt Evaluation Dashboard")
st.markdown("Explore the results of our Prompt Evaluation dataset. This dashboard provides a professional, light-toned overview of quality scores, hallucination risks, and their relationship with prompt characteristics.")

# Load Data
@st.cache_data
def load_data():
    # Attempt to load the cleaned dataset
    try:
        return pd.read_csv("Cleaned_dataset.csv")
    except FileNotFoundError:
        st.error("Could not find 'Cleaned_dataset.csv' in the current directory.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    # Sidebar Filters
    st.sidebar.header("Filters")
    
    # Task Type Filter
    task_types = df['task_type'].unique().tolist()
    selected_tasks = st.sidebar.multiselect("Select Task Type(s)", options=task_types, default=task_types)
    
    # Grade Filter
    grades = ['A', 'B', 'C', 'D', 'F']
    selected_grades = st.sidebar.multiselect("Select Grade(s)", options=grades, default=grades)
    
    # Apply Filters
    filtered_df = df[
        (df['task_type'].isin(selected_tasks)) & 
        (df['custom_grade'].isin(selected_grades))
    ]
    
    # KPIs
    st.markdown("### Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Prompts", f"{len(filtered_df):,}")
    col2.metric("Avg Quality Score", f"{filtered_df['quality_score'].mean():.2f}" if not filtered_df.empty else "0")
    col3.metric("Avg Custom Score", f"{filtered_df['custom_score_100'].mean():.2f}" if not filtered_df.empty else "0")
    col4.metric("Avg Hallucination Risk", f"{filtered_df['hallucination_risk'].mean():.2f}" if not filtered_df.empty else "0")
    
    st.markdown("---")
    
    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Quality Score Distribution")
        fig_hist = px.histogram(
            filtered_df, 
            x="quality_score", 
            nbins=30,
            color_discrete_sequence=['#87CEEB'],
            template="plotly_white"
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col_chart2:
        st.markdown("#### Hallucination Risk by Grade")
        fig_violin = px.violin(
            filtered_df, 
            x="custom_grade", 
            y="hallucination_risk", 
            color="custom_grade",
            category_orders={"custom_grade": ["A", "B", "C", "D", "F"]},
            box=True,
            template="plotly_white"
        )
        st.plotly_chart(fig_violin, use_container_width=True)
        
    col_chart3, col_chart4 = st.columns(2)
    
    with col_chart3:
        st.markdown("#### Task Type Distribution")
        task_counts = filtered_df['task_type'].value_counts().reset_index()
        fig_pie = px.pie(
            task_counts, 
            names='task_type', 
            values='count', 
            hole=0.4,
            template="plotly_white"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_chart4:
        st.markdown("#### Quality Score by Task Type")
        fig_box = px.box(
            filtered_df, 
            x="task_type", 
            y="quality_score", 
            color="task_type",
            template="plotly_white"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("---")
    st.markdown("### Filtered Dataset")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Export to Excel functionality
    def convert_df_to_excel(dataframe):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False, sheet_name='Filtered Data')
        return output.getvalue()

    excel_data = convert_df_to_excel(filtered_df)
    
    st.download_button(
        label="Download Data as Excel (.xlsx)",
        data=excel_data,
        file_name='filtered_prompt_evaluation_data.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
