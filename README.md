# **SpaceX Falcon 9 First Stage Landing Prediction**

## **Background & Objective 🚀**:
This project harnesses the Falcon 9 launch data from SpaceX to predict the success of its first-stage landing.

## **Technologies Employed 💻**:
- **Languages & Libraries**: Python, Pandas, Scikit-Learn, Plotly, and Dash
- **Database**: PostgreSQL
- **Data Source**: The entire dataset is sourced directly from the SpaceX API, and the insights extracted are visualized interactively using Plotly.

## **Methodological Approach 📊**:
- **Data Preparation**: The dataset underwent preprocessing, cleaning, and feature engineering phases.
- **Model Training**: Leveraging Scikit-Learn, multiple predictive models were trained, namely Logistic Regression, Decision Trees, and SVM.

## **Key Insights from EDA 🔍**:
- Flight Number positively correlates with Landing Success.
- Heavy payloads yield higher chances of successful landings.
- The launch success rate has seen an upward trend since 2013.

## **Plotly Dashboard 🖥️**:
- Interactive dashboard built with Plotly and Dash.
- Featured a launch site dropdown for success rates and a payload mass slider for detailed visual insights.

## **Machine Learning Outcomes 🤖**:
Out of the tested models, the Decision Tree stood out in performance. However, while the model showcased promising accuracy, it's pivotal to consider extraneous factors that might influence real-world results.

## **Conclusion & Forward Path 🛣️**:
With its current performance, the Decision Tree model is recommended for future predictions. However, the dynamic nature of space missions emphasizes the need for continuous data assimilation and consequent model refinement.

## **Getting Started 🚀**:

1. Clone the repository.
2. Ensure you have the necessary Python libraries installed (`pandas`, `numpy`, `matplotlib`, `sklearn`, `seaborn`, `sqlalchemy`, `sqlite`, `plotly`, and `dash`).
3. Navigate to the Jupyter Notebook and Plotly file to view the complete analysis.

---

Feel free to contribute or suggest improvements!
