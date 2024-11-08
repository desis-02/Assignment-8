import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

petal_df = pd.read_csv('C:/Users/desir/Downloads/Petal_Data')
sepal_df = pd.read_csv('C:/Users/desir/Downloads/Sepal_Data')

iris_df = pd.merge(sepal_df, petal_df, on='species')

print(iris_df.head())

plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species', palette='viridis')
plt.title('Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

sns.pairplot(iris_df, hue='species', palette='viridis')
plt.suptitle('Pairplot of Iris Features by Species', y=1.02)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=iris_df, x='species', y='petal_length', palette='viridis')
plt.title('Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

loan_df = pd.read_csv('C:/Users/desir/Downloads/LoanDataset') 

plt.figure(figsize=(8, 6))
sns.histplot(loan_df['loan_amnt'].dropna(), kde=True)
plt.title('Loan Amount Distribution')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(data=loan_df, x='home_ownership', hue='loan_intent', palette='viridis')
plt.title('Loan Intent by Home Ownership')
plt.xlabel('Home Ownership')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=loan_df, x='customer_income', y='loan_amnt', hue='Current_loan_status', palette='viridis')
plt.title('Customer Income vs Loan Amount by Current Loan Status')
plt.xlabel('Customer Income')
plt.ylabel('Loan Amount')
plt.show()


