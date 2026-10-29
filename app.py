import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide"
)


# --------------------------------------------------
# 2. LOAD DATA AND PERFORM CLUSTERING
# --------------------------------------------------

@st.cache_data
def load_and_cluster_data():
    data = pd.read_csv("Mall_Customers.csv")

    features = [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]

    # Scale the selected features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[features])

    # K-Means clustering
    kmeans = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )
    data["KMeans_Cluster"] = kmeans.fit_predict(scaled_features)

    # DBSCAN clustering
    dbscan = DBSCAN(
        eps=0.3,
        min_samples=5
    )
    data["DBSCAN_Cluster"] = dbscan.fit_predict(scaled_features)

    return data


try:
    df = load_and_cluster_data()
except FileNotFoundError:
    st.error(
        "Mall_Customers.csv was not found. "
        "Please place it in the same folder as app.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Unable to load or process the dataset: {error}")
    st.stop()


# --------------------------------------------------
# 3. DASHBOARD HEADER
# --------------------------------------------------

st.title("🛍️ Customer Segmentation Dashboard")

st.markdown(
    """
    Explore customer groups using **K-Means and DBSCAN clustering**.
    This dashboard helps identify patterns in annual income and
    spending behaviour to support data-driven marketing decisions.
    """
)

st.divider()


# --------------------------------------------------
# 4. KEY PERFORMANCE INDICATORS
# --------------------------------------------------

total_customers = len(df)
total_kmeans_clusters = df["KMeans_Cluster"].nunique()
average_income = df["Annual Income (k$)"].mean()
average_spending = df["Spending Score (1-100)"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👥 Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "🎯 K-Means Segments",
    total_kmeans_clusters
)

col3.metric(
    "💰 Average Annual Income",
    f"${average_income:.2f}k"
)

col4.metric(
    "🛒 Average Spending Score",
    f"{average_spending:.2f}/100"
)


# --------------------------------------------------
# 5. K-MEANS CUSTOMER SEGMENTATION
# --------------------------------------------------

st.header("🎯 K-Means Customer Segmentation")

st.write(
    "Explore how customers are grouped according to annual income "
    "and spending score."
)

cluster_options = sorted(df["KMeans_Cluster"].unique().tolist())

selected_clusters = st.multiselect(
    "Select customer segments to display",
    options=cluster_options,
    default=cluster_options,
    format_func=lambda cluster: f"Segment {cluster}"
)

filtered_df = df[df["KMeans_Cluster"].isin(selected_clusters)]

if not filtered_df.empty:
    plot_df = filtered_df.copy()
    plot_df["KMeans_Cluster"] = plot_df["KMeans_Cluster"].astype(str)

    fig_kmeans = px.scatter(
        plot_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color="KMeans_Cluster",
        hover_data=["CustomerID", "Gender", "Age"],
        title="Customer Segments: Annual Income vs Spending Score",
        labels={
            "Annual Income (k$)": "Annual Income (thousands of dollars)",
            "Spending Score (1-100)": "Spending Score",
            "KMeans_Cluster": "Customer Segment"
        },
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig_kmeans.update_layout(
        legend_title_text="Customer Segment",
        height=550
    )

    st.plotly_chart(fig_kmeans, use_container_width=True)

else:
    st.info("Select at least one segment to display the chart.")


# --------------------------------------------------
# 6. K-MEANS CLUSTER PROFILES
# --------------------------------------------------

st.header("📋 Customer Segment Profiles")

cluster_profiles = (
    df.groupby("KMeans_Cluster")
    .agg(
        Customer_Count=("CustomerID", "count"),
        Average_Annual_Income=("Annual Income (k$)", "mean"),
        Average_Spending_Score=("Spending Score (1-100)", "mean")
    )
    .reset_index()
)

cluster_profiles["Customer_Percentage"] = (
    cluster_profiles["Customer_Count"] / total_customers * 100
)

cluster_profiles["Segment_Interpretation"] = (
    cluster_profiles["KMeans_Cluster"].map({
        0: "Average Income, Average Spending",
        1: "High Income, High Spending",
        2: "Low Income, High Spending",
        3: "High Income, Low Spending",
        4: "Low Income, Low Spending"
    })
)

cluster_profiles = cluster_profiles.rename(
    columns={"KMeans_Cluster": "Segment"}
)

st.dataframe(
    cluster_profiles.round(2),
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# 7. CLUSTER SIZE VISUALIZATION
# --------------------------------------------------

st.subheader("Customer Count by Segment")

fig_counts = px.bar(
    cluster_profiles,
    x="Segment",
    y="Customer_Count",
    color="Segment",
    text="Customer_Count",
    title="Number of Customers in Each K-Means Segment",
    labels={
        "Segment": "Customer Segment",
        "Customer_Count": "Number of Customers"
    }
)

fig_counts.update_layout(height=400)

st.plotly_chart(fig_counts, use_container_width=True)


# --------------------------------------------------
# 8. BUSINESS INSIGHTS
# --------------------------------------------------

st.header("💼 Business Insights")

business_insights = {
    0: (
        "Average Income, Average Spending",
        "Consider testing loyalty rewards and personalized promotions."
    ),
    1: (
        "High Income, High Spending",
        "Consider testing premium offers and exclusive loyalty benefits."
    ),
    2: (
        "Low Income, High Spending",
        "Consider testing value bundles, rewards, and affordable offers."
    ),
    3: (
        "High Income, Low Spending",
        "Investigate possible purchase barriers and test targeted offers."
    ),
    4: (
        "Low Income, Low Spending",
        "Consider testing budget-friendly products and value promotions."
    )
}

for _, row in cluster_profiles.iterrows():
    segment = int(row["Segment"])
    interpretation, recommendation = business_insights[segment]

    with st.expander(f"Segment {segment}: {interpretation}"):
        st.write(f"**Customers:** {int(row['Customer_Count'])}")
        st.write(
            f"**Average annual income:** "
            f"${row['Average_Annual_Income']:.2f}k"
        )
        st.write(
            f"**Average spending score:** "
            f"{row['Average_Spending_Score']:.2f}/100"
        )
        st.write(f"**Suggested action:** {recommendation}")


# --------------------------------------------------
# 9. DBSCAN CLUSTERING
# --------------------------------------------------

st.header("🤖 DBSCAN Clustering")

st.write(
    "DBSCAN groups nearby observations and identifies observations "
    "that do not belong to a sufficiently dense region."
)

dbscan_counts = (
    df["DBSCAN_Cluster"]
    .value_counts()
    .sort_index()
    .rename_axis("DBSCAN_Cluster")
    .reset_index(name="Customer_Count")
)

dbscan_counts["Cluster_Type"] = dbscan_counts["DBSCAN_Cluster"].apply(
    lambda cluster: "Noise" if cluster == -1 else "Cluster"
)

fig_dbscan = px.bar(
    dbscan_counts,
    x="DBSCAN_Cluster",
    y="Customer_Count",
    color="Cluster_Type",
    text="Customer_Count",
    title="DBSCAN Cluster Distribution",
    labels={
        "DBSCAN_Cluster": "DBSCAN Cluster (-1 = Noise)",
        "Customer_Count": "Number of Customers",
        "Cluster_Type": "Type"
    }
)

fig_dbscan.update_layout(height=400)

st.plotly_chart(fig_dbscan, use_container_width=True)

# DBSCAN scatter plot: visualize clusters and noise points

st.subheader("DBSCAN Customer Segmentation Map")

dbscan_plot_df = df.copy()

# Give noise points a readable label
dbscan_plot_df["DBSCAN_Label"] = dbscan_plot_df[
    "DBSCAN_Cluster"
].apply(
    lambda cluster: "Noise (-1)"
    if cluster == -1
    else f"Cluster {cluster}"
)

fig_dbscan_scatter = px.scatter(
    dbscan_plot_df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    color="DBSCAN_Label",
    hover_data=["CustomerID", "Gender", "Age"],
    title="DBSCAN: Annual Income vs Spending Score",
    labels={
        "Annual Income (k$)": "Annual Income (thousands of dollars)",
        "Spending Score (1-100)": "Spending Score",
        "DBSCAN_Label": "DBSCAN Group"
    }
)

fig_dbscan_scatter.update_layout(height=550)

st.plotly_chart(
    fig_dbscan_scatter,
    use_container_width=True
)

noise_count = int((df["DBSCAN_Cluster"] == -1).sum())

col1, col2 = st.columns(2)

col1.metric(
    "DBSCAN Clusters (excluding noise)",
    df.loc[df["DBSCAN_Cluster"] != -1, "DBSCAN_Cluster"].nunique()
)

col2.metric(
    "Noise Points",
    f"{noise_count} ({noise_count / total_customers * 100:.1f}%)"
)

st.caption(
    "DBSCAN labels observations as noise when they do not belong "
    "to a discovered density-based cluster. Results depend on eps "
    "and min_samples."
)


# --------------------------------------------------
# 10. MODEL EVALUATION
# --------------------------------------------------

st.header("📈 Clustering Evaluation")

scaled_features = StandardScaler().fit_transform(
    df[["Annual Income (k$)", "Spending Score (1-100)"]]
)

kmeans_silhouette = silhouette_score(
    scaled_features,
    df["KMeans_Cluster"]
)

st.metric(
    "K-Means Silhouette Score",
    f"{kmeans_silhouette:.3f}"
)

st.write(
    "The silhouette score measures how well observations fit within "
    "their assigned clusters compared with other clusters. Values "
    "closer to 1 generally indicate better-separated clusters."
)

dbscan_labels = df["DBSCAN_Cluster"]
non_noise_mask = dbscan_labels != -1
non_noise_labels = dbscan_labels[non_noise_mask]

if (
    non_noise_labels.nunique() >= 2
    and non_noise_labels.nunique() < len(non_noise_labels)
):
    dbscan_silhouette = silhouette_score(
        scaled_features[non_noise_mask],
        non_noise_labels
    )

    st.metric(
        "DBSCAN Silhouette Score (excluding noise)",
        f"{dbscan_silhouette:.3f}"
    )

    st.caption(
        "This DBSCAN score excludes noise points, so compare it with "
        "the K-Means score cautiously."
    )
else:
    st.info(
        "A DBSCAN silhouette score cannot be calculated for the "
        "current clustering because at least two valid clusters "
        "are required."
    )


# --------------------------------------------------
# 11. CUSTOMER DATA EXPLORER
# --------------------------------------------------

st.header("🔎 Customer Data Explorer")

show_data = st.checkbox("Show customer records")

if show_data:
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# --------------------------------------------------
# 12. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Customer Segmentation Using K-Means & DBSCAN | "
    "Machine Learning Portfolio Project"
)