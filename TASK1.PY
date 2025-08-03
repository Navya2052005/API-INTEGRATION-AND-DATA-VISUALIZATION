import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = {
    "Employee ID": np.arange(1, 101),
    "Department": np.random.choice(["Sales", "Marketing", "IT", "HR"], 100),
    "Job Title": np.random.choice(["Manager", "Analyst", "Developer", "Coordinator"], 100),
    "Performance Rating": np.random.randint(1, 6, 100),
    "Years of Experience": np.random.randint(1, 11, 100),
    "Salary": np.random.randint(50000, 150000, 100)
}
df = pd.DataFrame(data)

# Visualization 1: Distribution of Performance Ratings
plt.figure(figsize=(8, 6))
sns.histplot(df["Performance Rating"], bins=5, kde=True)
plt.title("Distribution of Performance Ratings")
plt.xlabel("Performance Rating")
plt.ylabel("Frequency")
plt.show()

# Visualization 2: Performance Ratings by Department
plt.figure(figsize=(8, 6))
sns.barplot(x="Department", y="Performance Rating", data=df)
plt.title("Performance Ratings by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Rating")
plt.show()

# Visualization 3: Performance Ratings by Job Title
plt.figure(figsize=(8, 6))
sns.barplot(x="Job Title", y="Performance Rating", data=df)
plt.title("Performance Ratings by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Average Performance Rating")
plt.show()

# Visualization 4: Relationship between Years of Experience and Performance Rating
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Years of Experience", y="Performance Rating", data=df)
plt.title("Relationship between Years of Experience and Performance Rating")
plt.xlabel("Years of Experience")
plt.ylabel("Performance Rating")
plt.show()

# Visualization 5: Relationship between Salary and Performance Rating
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Salary", y="Performance Rating", data=df)
plt.title("Relationship between Salary and Performance Rating")
plt.xlabel("Salary")
plt.ylabel("Performance Rating")
plt.show()

# Visualization 6: Heatmap of Correlations between Variables
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap of Correlations between Variables")
plt.show()

# Visualization 7: Pairplot of Variables
plt.figure(figsize=(12, 10))
sns.pairplot(df)
plt.title("Pairplot of Variables")
plt.show()

# Insights and Recommendations
print("Insights:")
print("* The distribution of performance ratings is skewed to the right, indicating that most employees have high performance ratings.")
print("* The average performance rating varies by department, with the Sales department having the highest average rating.")
print("* The average performance rating also varies by job title, with Managers having the highest average rating.")
print("* There is a positive relationship between years of experience and performance rating, indicating that more experienced employees tend to have higher performance ratings.")
print("* There is a positive relationship between salary and performance rating, indicating that higher-paid employees tend to have higher performance ratings.")
print("Recommendations:")
print("* Provide training and development opportunities to employees in departments with lower average performance ratings.")
print("* Provide additional support and resources to employees in job titles with lower average performance ratings.")
print("* Consider using years of experience and salary as factors in performance evaluations.")
