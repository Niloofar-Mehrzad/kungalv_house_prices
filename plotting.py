import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("kungalv_house_prices.csv")

# Convert columns to numeric (if necessary)
df['Closing Price (kr)'] = pd.to_numeric(df['Closing Price (kr)'], errors='coerce')
df['Boarea (m2)'] = pd.to_numeric(df['Boarea (m2)'], errors='coerce')

# Example: Scatter plot of Closing Price vs. Boarea
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Boarea (m2)', y='Closing Price (kr)')
plt.title("Closing Price vs. Boarea")
plt.xlabel("Boarea (m²)")
plt.ylabel("Closing Price (kr)")
plt.grid()
plt.show()
