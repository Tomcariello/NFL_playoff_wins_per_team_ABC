import matplotlib.pyplot as plt

# Create a new figure
fig = plt.figure()

# Add axes to the figure [x0, y0, width, height]
# x0 = where to start the x-axis, relative to the left side of the window
# y0 = where to start the y-axis, relative to the bottom of the window
# width = the width this axes should occupy as a percentage of the window
# height = the height this axes should occupy as a percentage of the window
ax = fig.add_axes([.25,.25,.5,.5])

# Indicate the labels
languages = ['JavaSCript', 'C++', 'Java', 'Python', 'PHP']

# Student values list 
people = [11,58,27,36,21]

# Specify the chart type (barh --> horizontal bar chart)
# Also specify which values to show on each axis
ax.barh(languages, people)

# plt.axis("image")

# Show the bar chart
plt.show()