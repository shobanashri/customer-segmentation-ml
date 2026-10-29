#### **Customer Segmentation Using K-Means \& DBSCAN**

**-------------------------------------------------------------------------------**



| Component      | Details                                          |

| -------------- | ------------------------------------------------ |

| Project name   | Customer Segmentation Using K-Means \& DBSCAN     |

| Domain         | Retail / E-commerce / Marketing                  |

| Learning type  | Unsupervised Machine Learning                    |

| Algorithm 1    | K-Means Clustering                               |

| Algorithm 2    | DBSCAN Clustering                                |

| Language       | Python                                           |

| Environment    | Jupyter Notebook                                 |

| Main libraries | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn |





##### **What problem are we solving?**

\------------------------------------

Imagine a shopping mall has thousands of customers. Every customer has different characteristics and spending habits.



The marketing team wants to understand:

\------------------------------------------

Who are the high-spending customers?

Which customers spend less?

Which customers have similar characteristics?

Can customers be grouped into meaningful segments?

How can marketing campaigns be tailored to different customer groups?



Instead of manually categorizing customers, we'll use clustering algorithms to discover groups of similar customers from the data.



Business objective

\--------------------

Identify meaningful customer segments based on available customer attributes and spending behaviour to help businesses develop more targeted marketing strategies.



ML objective

\----------------

Apply and compare K-Means and DBSCAN to discover customer clusters, then evaluate their quality and interpret their business relevance.





###### **Workflow**

\---------

| Step | Stage                     | What we'll do                                              |

| ---- | ------------------------- | ---------------------------------------------------------- |

| 1    | Project setup             | Organize folders and create the notebook                   |

| 2    | Data understanding        | Load the dataset and inspect its structure                 |

| 3    | Data quality              | Check missing values, duplicates, and data types           |

| 4    | Exploratory Data Analysis | Analyze customer characteristics and distributions         |

| 5    | Feature selection         | Identify appropriate clustering features                   |

| 6    | Feature scaling           | Prepare features for distance-based algorithms             |

| 7    | K-Means                   | Find clusters and determine a suitable number of clusters  |

| 8    | DBSCAN                    | Discover density-based clusters and potential noise points |

| 9    | Evaluation                | Compare cluster quality using suitable metrics             |

| 10   | Visualization             | Visualize the discovered customer segments                 |

| 11   | Business interpretation   | Explain what the clusters mean for marketing               |

| 12   | Documentation             | Prepare a professional README and publish to GitHub        |





Data understanding

\------------------



Use in clustering -> Annual Income(k$) , Spending Score(1-100)

CustomerID identifies a customer; it doesn't measure their behaviour.





Data quality

\-----------

Age -> avg - 38.85yrs , range - 18-70

Annual income -> avg - 60.56, range - 15k-137k

spending score -> avg - 50.20, range - 1-99



EDA

\----

Gender -> 112 females (56%) and 88 males (44%)

Age -> The distribution appears concentrated among young and middle-aged adults, with fewer customers at older ages.

Annual incomes -> Most customers appear concentrated in the middle-income range, with a smaller number of high-income customers.

Spending score ->  The distribution appears to have concentrations at lower, moderate, and higher spending levels.





Kmeans

\------

Why convert the centroids back? The model learned using standardized features, but the plot uses the original income and spending-score scales. inverse\_transform() converts the centers so both use the same units.





| Cluster | Customers | Avg. Income | Avg. Spending Score | Interpretation                   |

| ------- | --------: | ----------: | ------------------: | -------------------------------- |

| 0       |        81 |      55.30k |               49.52 | Average Income, Average Spending |

| 1       |        39 |      86.54k |               82.13 | High Income, High Spending       |

| 2       |        22 |      25.73k |               79.36 | Low Income, High Spending        |

| 3       |        35 |      88.20k |               17.11 | High Income, Low Spending        |

| 4       |        23 |      26.30k |               20.91 | Low Income, Low Spending         |


Evaluation results

\-------------------

| Metric             |   K-Means |     DBSCAN |

| ------------------ | --------: | ---------: |

| Silhouette Score   | \*\*0.555\*\* |      0.524 |

| Number of clusters |         5 |          7 |

| Noise points       |         0 | 35 (17.5%) |



Interpretation

\---------------

K-Means : The silhouette score - 0.555 indicates reasonably well separated clusters

DBSCAN : 0.524 - some cluster separation but it exclude 35 noise points.

Current result : k-means has high silhouette- produce 5 interpretable customer segment.

DBSCAN identify noise bt create 7 clusters with current param.





Business Interpretation

\--------------------------



K-Means identified five customer segments using annual income and spending score, with a silhouette score of 0.555.



Cluster 0 — Average Income, Average Spending: The largest segment, containing 81 customers (40.5%). Loyalty programs and personalized promotions may help encourage repeat purchases.

Cluster 1 — High Income, High Spending: Contains 39 customers (19.5%). Premium offers and exclusive loyalty benefits could help retain these customers.

Cluster 2 — Low Income, High Spending: Contains 22 customers (11%). Affordable premium products and rewards may be suitable strategies to test.

Cluster 3 — High Income, Low Spending: Contains 35 customers (17.5%). Further investigation is needed to understand their low spending and identify possible barriers to purchasing.

Cluster 4 — Low Income, Low Spending: Contains 23 customers (11.5%). Budget-friendly products and value-focused promotions may be appropriate.



Conclusion: The segments provide a structured way to understand customer income and spending patterns. The proposed marketing strategies should be tested using actual campaign results before implementation.





segmemt summay

\-------------

| Segment                          | Customers | What the owner learns                                    |

| -------------------------------- | --------: | -------------------------------------------------------- |

| High Income, High Spending       |        39 | Customers who may be suitable for premium offers         |

| High Income, Low Spending        |        35 | Customers whose purchase barriers may need investigation |

| Low Income, High Spending        |        22 | Customers who spend actively despite lower income        |

| Low Income, Low Spending         |        23 | Customers who may respond to value-focused offers        |

| Average Income, Average Spending |        81 | The largest group, suitable for retention initiatives    |





4\. How will the model work when new customers arrive?



This is where the project becomes more than a one-time analysis.



Suppose a retail owner receives a new customer record:



| Customer   | Annual Income | Spending Score |

| ---------- | ------------: | -------------: |

| Customer A |           85k |             90 |



Our application would:



Receive the customer's income and spending score.

Apply the same fitted scaler used during model training.

Pass the scaled features to the trained K-Means model.

Return the assigned cluster.

Display the segment's business interpretation.













Ui 

\---

python -m pip install streamlit



python -m streamlit --version



python -m streamlit run app.py



