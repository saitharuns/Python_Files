import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Fetch names and scores from the database
cursor.execute('SELECT NAME, PERCENTAGE FROM STUDENTS')
data = cursor.fetchall()

# Separate data into names and scores arrays
names = np.array([row[0] for row in data])  # Extract names
scores = np.array([row[1] for row in data])  # Extract scores

# Plot the data as a bar graph

plt.bar(names, scores)
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Student Scores')

plt.show()

# Close the connection
conn.close()
