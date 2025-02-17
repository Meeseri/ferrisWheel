import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
RADIUS = 96  # Radius of the wheel in feet
CENTER = 96  # Vertical shift (center of the wheel)
PERIOD = 600  # Time for one full rotation in seconds (10 minutes)
PHASE_SHIFT = -math.pi / 2  # Phase shift to start at 0

# Function to calculate height at time t
def height_over_time(t):
    return RADIUS * math.sin((2 * math.pi / PERIOD) * t + PHASE_SHIFT) + CENTER

# Generate time values from 0 to 600 seconds (10 minutes)
time_seconds = np.linspace(0, 600, 3600)  # 1000 points for smooth graph
time_minutes = time_seconds / 60  # Convert seconds to minutes
heights = [height_over_time(t) for t in time_seconds]


# Key points (in seconds)
key_times = [0, 150, 300, 450, 600]  # 0, 2.5, 5.0, 7.5, 10.0 minutes
key_heights = [height_over_time(t) for t in key_times]

# Print results
for t, h in zip(key_times, key_heights):
    print(f"Time: {t / 60:.1f} minutes, Height: {h:.1f} feet")

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(time_minutes, heights, label="Height of Passenger Over Time")
plt.title("Centennial Wheel Height Over Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Height (feet)")
plt.axhline(y=CENTER, color="r", linestyle="--", label="Center of Wheel")
plt.axhline(y=0, color="g", linestyle="--", label="Ground Level")
plt.legend()
plt.grid(True)
plt.show()