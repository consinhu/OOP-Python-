import pandas as pd
import matplotlib.pyplot as plt

# Extraction
dataset = pd.read_csv("/Users/consinhu/Rutgers/Spring 2024/Object-Oriented Programming/Fruit Prices 2020.csv")

# Transformations
price_by_form = dataset.groupby('Form')['RetailPrice']
mean_price_by_form = price_by_form.mean().reset_index()
filtered_mean_price_by_form = mean_price_by_form[mean_price_by_form['RetailPrice'] > 2.00]

# Load 1 
filtered_mean_price_by_form.to_csv("/Users/consinhu/Rutgers/Spring 2024/Object-Oriented Programming/Fruit Prices 2020.csv")

# Load 2
plt.figure(figsize = (10, 8))
plt.pie(filtered_mean_price_by_form["RetailPrice"], labels = filtered_mean_price_by_form["Form"], autopct = '%1.1f%%', startangle = 90)
plt.title("Mean Prices of Fruits by Form")
plt.savefig('fruitpiechart.png')


