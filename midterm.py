import matplotlib.pyplot as plt

# Example 1: Creating a scatter plot using one conditional statement
x_values = range(1, 21)
y_values = [x + 1 for x in x_values]

filtered_x = [x for x in x_values if x % 2 == 0]
filtered_y = [y for y in y_values if y % 2 != 0] 

plt.scatter(filtered_x, filtered_y, color='blue', label = 'Even x, Odd y')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('My Scatter Plot')
plt.legend()

plt.grid(True)
plt.show()

# Example 2: Merge two bar charts using a for loop
cat1 = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 9, 6]

cat2 = ['F', 'G', 'H', 'I', 'J']
values2 = [8, 4, 6, 2, 7]

bar_width = 0.35

fig, ax = plt.subplots()
for i in range(2):
    if i == 0:
        x = [j for j in range(len(cat1))]
        ax.bar(x, values1, bar_width, color = 'blue', label = 'Bar Chart 1')
    else:
        x = [j + bar_width for j in range(len(cat2))]
        ax.bar(x, values2, bar_width, color = 'red', label = 'Bar Chart 2')

ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Merged Bar Charts')
ax.legend()

plt.grid(True)
plt.show()

# Example 3: Set tick marks
x_values = [1, 2, 3, 4, 5]
y_values = [5, 7, 2, 8, 4]

plt.plot(x_values, y_values)

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 4, 6, 8, 10])

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Plot with Tick Marks')

plt.grid(True)
plt.show()
