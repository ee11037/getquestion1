import matplotlib.pyplot as plt

# Function to read points from a file

def read_points_from_file(filename):

   points = []

   with open(filename, 'r') as file:

       for line in file:
           
           line = line[2:13]
           x, y = map(float, line.split(","))
           
           points.append((x, y))
           print(points)
   return points

# Read points from the file

filename = 'output_points.txt'

points = read_points_from_file(filename)

# Extract x and y coordinates

x_values = [point[0] for point in points]

y_values = [point[1] for point in points]

# Create the plot

plt.figure(figsize=(8, 6))

plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Line through points A, B, P')

# Annotate the points

for i, point in enumerate(points):
   if i==2:
   	plt.text(point[0], point[1], 'P', fontsize=12, verticalalignment='bottom')
   else:
        plt.text(point[0], point[1], f' {chr(65 + i)}', fontsize=12, verticalalignment='bottom')


# Set the title and labels

plt.title('Line Passing Through Points A, B, and P')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

# Add grid and legend

plt.grid()

plt.legend()

# Set limits for better visibility

plt.xlim(0, 6)

plt.ylim(-6, 3)

# Draw axes

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

plt.axvline(0, color='black', linewidth=0.5, linestyle='--')


# Show the plot
plt.show()
plt.savefig('Figure_1.png')
