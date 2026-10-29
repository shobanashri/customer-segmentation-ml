# Customer Segmentation Using K-Means and DBSCAN

## 1. Project Overview

This project applies unsupervised machine learning to segment mall customers based on their annual income and spending score.

The objective is to identify groups of customers with similar spending patterns and explore how these segments could support targeted marketing strategies.

Two clustering algorithms are investigated:

* K-Means
* DBSCAN

## 2. Business Problem

Retail businesses serve customers with different income levels and spending behaviors. Treating every customer identically may limit the effectiveness of marketing campaigns.

Customer segmentation can help businesses understand these differences and develop more targeted marketing strategies.

## 3. Dataset

The Mall Customers dataset contains 200 customer records and five columns:

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| CustomerID             | Unique customer identifier            |
| Gender                 | Customer gender                       |
| Age                    | Customer age                          |
| Annual Income (k$)     | Annual income in thousands of dollars |
| Spending Score (1-100) | Spending score on a scale of 1 to 100 |

The initial data-quality checks found no missing values or duplicate rows.

## 4. Methodology

1. Data understanding and quality checks
2. Exploratory data analysis
3. Feature selection
4. Feature standardization using `StandardScaler`
5. K-Means clustering and selection of K using the Elbow Method
6. DBSCAN clustering
7. Cluster visualization and evaluation
8. Business interpretation

### Selected Features

The clustering models use:

* `Annual Income (k$)`
* `Spending Score (1-100)`

CustomerID is excluded because it is an identifier rather than a meaningful behavioral feature.

## 5. Model Results

### K-Means

The Elbow Method was used to select five clusters.

* Number of clusters: 5
* Silhouette Score: 0.555
* Customers segmented: 200

### DBSCAN

An initial DBSCAN configuration was evaluated.

* `eps`: 0.3
* `min_samples`: 5
* Number of clusters: 7
* Noise points: 35 (17.5%)
* Silhouette Score excluding noise points: approximately 0.524

The silhouette scores are not directly comparable because the DBSCAN score excludes noise points.

Based on the current results, K-Means is the leading candidate for the primary segmentation.

## 6. K-Means Customer Segments

| Cluster | Customers | Average Annual Income (k$) | Average Spending Score | Interpretation                   |
| ------- | --------: | -------------------------: | ---------------------: | -------------------------------- |
| 0       |        81 |                      55.30 |                  49.52 | Average Income, Average Spending |
| 1       |        39 |                      86.54 |                  82.13 | High Income, High Spending       |
| 2       |        22 |                      25.73 |                  79.36 | Low Income, High Spending        |
| 3       |        35 |                      88.20 |                  17.11 | High Income, Low Spending        |
| 4       |        23 |                      26.30 |                  20.91 | Low Income, Low Spending         |

## 7. Potential Business Applications

* **Cluster 0:** Explore loyalty programs and personalized promotions.
* **Cluster 1:** Test premium offers and exclusive loyalty benefits.
* **Cluster 2:** Consider rewards and value-focused premium options.
* **Cluster 3:** Investigate barriers to purchasing and test relevant offers.
* **Cluster 4:** Explore budget-friendly products and value-focused promotions.

These are potential strategies based on the observed patterns. Their effectiveness must be validated through actual campaign results.

## 8. Limitations

* The dataset contains only 200 customers.
* The selected features do not capture all aspects of customer behavior.
* The clusters are algorithm-generated groups, not independently verified customer categories.
* The Silhouette Score alone does not establish business usefulness.
* Marketing outcomes have not been tested using campaign data.

## 9. Future Improvements

* Develop an interactive Streamlit dashboard.
* Allow users to explore customer segments and cluster profiles.
* Support segment assignment for new customers using the fitted scaler and model.
* Evaluate marketing outcomes when suitable business data becomes available.

## 10. Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## 11. Conclusion

This project explores customer segmentation using K-Means and DBSCAN. K-Means produced five interpretable groups and achieved a Silhouette Score of 0.555.

The results provide an initial understanding of customer income and spending patterns. Further validation and an interactive dashboard could help make these insights more accessible for business use.
