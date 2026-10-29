# Customer Segmentation Using K-Means and DBSCAN

## 1. Project Overview

This project applies unsupervised machine learning to segment mall customers based on their annual income and spending score.

The objective is to identify groups of customers with similar spending patterns and explore how these segments could support targeted marketing strategies.

Two clustering algorithms are investigated:

* K-Means
* DBSCAN

The project includes exploratory data analysis, cluster evaluation, business interpretation, and an interactive Streamlit dashboard for exploring the resulting customer segments.

## 2. Business Problem

Retail businesses serve customers with different income levels and spending behaviors. Treating every customer identically may limit the effectiveness of marketing campaigns.

Customer segmentation can help businesses understand these differences and develop more targeted marketing strategies.

This project explores how unsupervised learning can identify customer groups using annual income and spending score.

## 3. Dataset

The Mall Customers dataset contains 200 customer records and five columns.

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| CustomerID             | Unique customer identifier            |
| Gender                 | Customer gender                       |
| Age                    | Customer age                          |
| Annual Income (k$)     | Annual income in thousands of dollars |
| Spending Score (1-100) | Spending score on a scale of 1 to 100 |

The initial data-quality checks found no missing values or duplicate rows.

### Selected Features

The clustering models use:

* `Annual Income (k$)`
* `Spending Score (1-100)`

`CustomerID` is excluded because it is an identifier rather than a meaningful behavioral feature. Gender and age are not included in the initial clustering models.

## 4. Methodology

The project follows these steps:

1. Data understanding and quality checks
2. Exploratory data analysis
3. Feature selection
4. Feature standardization using `StandardScaler`
5. K-Means clustering and selection of K using the Elbow Method
6. DBSCAN clustering
7. Cluster visualization and evaluation
8. Business interpretation
9. Interactive dashboard development using Streamlit and Plotly

## 5. Model Results

### K-Means

The Elbow Method was used to select five clusters.

* Number of clusters: 5
* Silhouette Score: 0.555
* Customers segmented: 200

K-Means produced five interpretable customer groups based on annual income and spending score.

### DBSCAN

An initial DBSCAN configuration was evaluated.

* `eps`: 0.3
* `min_samples`: 5
* Number of clusters: 7, excluding noise
* Noise points: 35 (17.5%)
* Silhouette Score excluding noise points: approximately 0.524

DBSCAN identified seven density-based clusters and left 35 customers unassigned to a cluster under the selected parameters. These points are labelled as noise; this does not automatically mean that they are abnormal customers.

The silhouette scores are not directly comparable because the DBSCAN score excludes noise points.

Based on the current results, K-Means is the leading candidate for the primary segmentation because it provides five interpretable groups and a higher reported silhouette score. Further evaluation should also consider cluster structure, stability, and business usefulness.

## 6. K-Means Customer Segments

| Cluster | Customers | Average Annual Income (k$) | Average Spending Score | Interpretation                   |
| ------- | --------: | -------------------------: | ---------------------: | -------------------------------- |
| 0       |        81 |                      55.30 |                  49.52 | Average Income, Average Spending |
| 1       |        39 |                      86.54 |                  82.13 | High Income, High Spending       |
| 2       |        22 |                      25.73 |                  79.36 | Low Income, High Spending        |
| 3       |        35 |                      88.20 |                  17.11 | High Income, Low Spending        |
| 4       |        23 |                      26.30 |                  20.91 | Low Income, Low Spending         |

These interpretations describe the observed cluster profiles. They are useful summaries of the data, not independently verified customer categories.

## 7. Potential Business Applications

The identified segments suggest several marketing strategies that could be tested.

* **Cluster 0 — Average Income, Average Spending:** Explore loyalty programs and personalized promotions.
* **Cluster 1 — High Income, High Spending:** Test premium offers and exclusive loyalty benefits.
* **Cluster 2 — Low Income, High Spending:** Consider rewards and affordable offers that encourage continued engagement.
* **Cluster 3 — High Income, Low Spending:** Investigate potential purchasing barriers and test relevant offers.
* **Cluster 4 — Low Income, Low Spending:** Explore budget-friendly products and value-focused promotions.

These are potential strategies based on observed patterns. Their effectiveness must be validated through actual campaign results.

## 8. Interactive Dashboard

The project includes a Streamlit dashboard built with Plotly.

The dashboard provides:

* Key dataset statistics
* Interactive K-Means customer segmentation scatter plot
* K-Means cluster profiles and visualizations
* Potential business insights for each K-Means segment
* DBSCAN cluster visualization and cluster counts
* Noise-point information
* Silhouette score comparison
* An option to inspect the customer data

The dashboard helps users explore the segmentation results visually. The displayed clusters and business recommendations should be interpreted in the context of the dataset and the limitations of unsupervised learning.

## 9. Limitations

* The dataset contains only 200 customers.
* The selected features do not capture all aspects of customer behavior.
* The clusters are algorithm-generated groups, not independently verified customer categories.
* The silhouette score alone does not establish business usefulness.
* The K-Means and DBSCAN silhouette scores are calculated on different sets of observations, so the comparison requires caution.
* Marketing outcomes have not been tested using campaign data.

## 10. Future Improvements

* Support segment assignment for new customers using the fitted scaler and K-Means model.
* Explore DBSCAN parameter sensitivity and clustering stability.
* Evaluate marketing outcomes when suitable business data becomes available.
* Investigate additional customer features if reliable data becomes available.
* Improve the dashboard with additional filtering and customer-level exploration where useful.

## 11. Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Plotly

## 12. Conclusion

This project explores customer segmentation using K-Means and DBSCAN. K-Means produced five interpretable customer groups and achieved a silhouette score of 0.555. DBSCAN identified seven density-based clusters and 35 noise points using the selected parameters.

An interactive Streamlit dashboard makes the segmentation results, cluster profiles, and evaluation metrics easier to explore.

The findings provide an initial understanding of customer income and spending patterns. Further validation, stability analysis, and real-world campaign testing are needed before using these segments to guide business decisions.
