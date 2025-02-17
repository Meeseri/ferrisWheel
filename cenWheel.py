import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# This is a program for precalculus, and it shows the sin graph of
# the Cenntenial Wheel. This includes a table with the 5 key
# points of the graph.

# Made by Oliver Hernandez

# Constants, pretty reusable!
# to model a diff wheel, change radius and center accordingly
# period changes speed of rotation
# phase shift changes starting location of cabin
RADIUS = 96  # Radius of the wheel in feet
CENTER = 96  # Vertical shift, and shows you the center of wheel
PERIOD = 600  # Time full rotation in secs, in this case 10 minutes
PHASE_SHIFT = -math.pi / 2  # Phase shift to start at 0

# Function to calculate height at time t, set 2 postive (counterclock) or negative(clockwise)
def height_over_time(t):
    return RADIUS * math.sin((-2 * math.pi / PERIOD) * t + PHASE_SHIFT) + CENTER

# Generate time values from 0 to 600 seconds (10 minutes)
time_seconds = np.linspace(0, 600, 800)  # np.linspace is the number of spaces between 0 and 600secs, changes smoothness of graph

time_minutes = time_seconds / 60  # this converts secs to min and stores it

heights = [height_over_time(t) for t in time_seconds] #Calculates height for each time point using height_over_time function (change the range in time_seconds above to show longer or shorter ride)

# Key points (in seconds)
key_times = [0, 150, 300, 450, 600]  # 0, 2.5, 5.0, 7.5, 10.0 minutes
key_heights = [height_over_time(t) for t in key_times]

# Create the plot
fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 1, height_ratios=[3, 1])  # Split into 2 rows: plot and table

# Plot the sinusoidal function
ax1 = plt.subplot(gs[0]) 
ax1.plot(time_minutes, heights, label="Height of Passenger Over Time") # x-axis, changed to minutes to read smoothly

#Labels are self explanatory!
ax1.set_title("Centennial Wheel Height Over Time") 
ax1.set_xlabel("Time (minutes)")
ax1.set_ylabel("Height (feet)")
ax1.axhline(y=CENTER, color="r", linestyle="--", label="Center of Wheel")
ax1.axhline(y=0, color="g", linestyle="--", label="Ground Level")
ax1.legend()

#Adds grid so you can trace the graph better
ax1.grid(True)

# Add placeholder text in the top-left corner
placeholder_text = "Name: Oliver Hernandez\nDate: 2/17/2025\nCourse: Precalculus\nInstructor: Dr. Nathanson"
ax1.text(0.02, 0.98, placeholder_text, fontsize=12, ha="left", va="top", transform=ax1.transAxes,
         bbox=dict(facecolor="white", alpha=0.8, edgecolor="black", boxstyle="round"))

# Add the function equation above the plot (was pain tbh)
equation_text = r"$h(t) = 96 \cdot \sin\left(\frac{2\pi}{600} \cdot t - \frac{\pi}{2}\right) + 96$"
ax1.text(0.5, 1.1, equation_text, fontsize=12, ha="center", va="center", transform=ax1.transAxes)

# Create a table for the key points
ax2 = plt.subplot(gs[1])
ax2.axis("off")  # Hide axes for the table
table_data = [
    ["Time (minutes)", "Time (seconds)", "Height (feet)"],
    [0.0, 0, 0.0],
    [2.5, 150, 96.0],
    [5.0, 300, 192.0],
    [7.5, 450, 96.0],
    [10.0, 600, 0.0],
]
table = ax2.table(cellText=table_data, loc="center", colLabels=None, cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Adjust layout and display
plt.tight_layout()
plt.show()