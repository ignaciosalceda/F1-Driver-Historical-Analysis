import streamlit as st
import pandas as pd
import plotly.express as px

# Load preprocessed driver-level data
df = pd.read_csv("driver_cluster_data.csv")

# Define enriched cluster labels and visual definitions
cluster_definitions = {
    0: ("🏆 Winners", "<span style='color:#4CAF50; font-weight:bold'>These are the clutch performers</span> — drivers who <em>consistently outpaced</em> their teammates, often shining in <strong>less competitive machinery</strong>. Gritty, fearless, and technically gifted."),
    1: ("🚀 Overperformers", "<span style='color:#9b59b6; font-weight:bold'>These are the hidden stars</span> — drivers who <em>outdrove their machinery</em> and teammates, even if the scoreboard didn’t reflect it. Talent held back by circumstance."),
    2: ("🟢 Decent", "<span style='color:#2ecc71; font-weight:bold'>Steady, reliable, and consistent</span>. These drivers regularly brought points to their teams, showing <em>balanced performance</em> both in racecraft and qualifying."),
    3: ("⚠️ Underperformers", "<span style='color:#e74c3c; font-weight:bold'>These drivers often struggled to beat their teammates</span> despite occasionally scoring points. Whether due to <em>inconsistency</em> or playing a support role, they couldn’t consistently deliver results."),
    4: ("👑 Elite", "<span style='color:#f39c12; font-weight:bold'>F1 royalty</span>. These drivers <strong>dominated</strong> both the championship and their teammates. Hall-of-fame material with the complete package: <em>speed, precision, and consistency</em>."),
    5: ("⬇️ Poor", "<span style='color:#95a5a6; font-weight:bold'>The strugglers</span>. Rarely scored points and often beaten by teammates. Sometimes unlucky, sometimes out of depth, but always under the spotlight.")
}

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Driver Explorer", "📖 Project Overview"])

if page == "📖 Project Overview":
    st.title("📊 F1 Driver Performance Profiling")
    st.markdown("""
    ## 🧠 What is this project?
    This project aims to analyze and classify Formula 1 drivers across history using a data-driven, standardized methodology. Given how varied F1 has been across decades — from race lengths, car performance, to points systems — this app helps answer: **Who truly are the greatest drivers?**

    ## ⚙️ How it works
    We calculate two core metrics for each driver:
    - **Points per Race (normalized):** How efficiently a driver scores over their career.
    - **Teammate Win Ratio:** How often a driver finishes ahead of their teammate(s) — the only fair comparison, as they share the same car.

    These metrics are combined and fed into a **K-Means clustering algorithm**, which categorizes drivers into performance tiers:

    - 👑 **Elite**: Dominant and consistent, outperforming teammates and scoring heavily.
    - 🏆 **Winners**: Drivers who stood out against teammates, often without a top-tier car.
    - 🚀 **Overperformers**: Consistently beat teammates, even with limited race points.
    - 🟢 **Decent**: Balanced drivers who scored regularly and competed well.
    - ⚠️ **Underperformers**: Inconsistent or support drivers outpaced by teammates.
    - ⬇️ **Poor**: Rarely scored or outshined by their teammates.

    ## 🛠️ Technologies used
    - **Python** for data processing
    - **pandas**, **scikit-learn**, and **Plotly** for analytics and visualization
    - **Streamlit** for web app interactivity

    ## 🔍 Why this matters
    In F1, raw statistics like total wins or points can be misleading. This approach provides context-aware, fairer evaluation across eras. Whether you're a stats geek or casual fan — explore how your favorite driver ranks!
    """)

else:
    # Driver Explorer Page
    st.title("🏎️ F1 Driver Cluster Explorer")

    # UI: Select a driver
    driver_selected = st.selectbox("Select a driver to analyze:", df['driver'].sort_values())

    # Get selected driver data
    d_selected = df[df['driver'] == driver_selected].iloc[0]
    cluster_id = d_selected['cluster']
    cluster_name, cluster_desc = cluster_definitions.get(cluster_id, ("Unknown", "No definition available."))

    # Rank drivers by metric
    df['rank'] = df['metric'].rank(ascending=False, method='min')
    df_sorted = df.sort_values('rank').reset_index(drop=True)
    df_sorted['rank'] = df_sorted['rank'].astype(int)
    selected_index = df_sorted[df_sorted['driver'] == driver_selected].index[0]

    # Highlight selected row in custom table
    def highlight_selected_subtable(s):
        return ['background-color: #FFD700' if s['driver'] == driver_selected else '' for _ in s]

    # Plot with highlighted point
    fig = px.scatter(
        df,
        x='ratio_points_per_race',
        y='win_ratio',
        color='performance_tier',
        hover_name='driver',
        title='F1 Driver Performance Clusters',
        labels={
            'ratio_points_per_race': 'Points per Race (Ratio)',
            'win_ratio': 'Teammate Win Ratio',
            'performance_tier': 'Performance Tier'
        }
    )
    fig.add_scatter(
        x=[d_selected['ratio_points_per_race']],
        y=[d_selected['win_ratio']],
        mode='markers+text',
        marker=dict(size=14, color='white', line=dict(width=2, color='black')),
        text=[driver_selected],
        textposition='top center',
        name='Selected Driver'
    )

    # Show outputs
    st.plotly_chart(fig)

    st.markdown(f"### {driver_selected}")
    st.markdown(f"**Cluster:** {cluster_name}", unsafe_allow_html=True)
    st.markdown(cluster_desc, unsafe_allow_html=True)

    # Display custom 9-row ranking window centered on selected driver
    start = max(0, selected_index - 4)
    end = min(len(df_sorted), selected_index + 5)
    window_df = df_sorted.iloc[start:end][['rank', 'driver', 'ratio_points_per_race', 'win_ratio']]

    st.markdown("### Ranking Neighborhood")
    st.dataframe(window_df.style.apply(highlight_selected_subtable, axis=1), use_container_width=True)