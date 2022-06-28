import matplotlib.pyplot as plt

# Create a new figure
fig = plt.figure()

# Add axes to the figure
ax = fig.add_axes([0,0,1,1])

# Indicate the labels
langs = ['C', 'C++', 'Java', 'Python', 'PHP']

# Student values list 
students = [23,17,35,29,12]

# Specify the chart type (barh --> horizontal bar chart)
# Also specify which values to show on each axis
ax.barh(langs,students)

# Show the bar chart
plt.show()