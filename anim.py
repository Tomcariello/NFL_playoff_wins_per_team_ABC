import matplotlib.pyplot as plt

# Create a new figure
fig = plt.figure()

# Add axes to the figure
ax = fig.add_axes([0,0,1,1])

# Indicate the labels
languages = ['JavaSCript', 'C++', 'Java', 'Python', 'PHP']

# Student values list 
people = [11,58,27,36,21]

# Specify the chart type (barh --> horizontal bar chart)
# Also specify which values to show on each axis
ax.barh(languages, people)

# Show the bar chart
plt.show()