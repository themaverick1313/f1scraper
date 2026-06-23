import math
from pprint import pprint


class colors:

    class fg:
        white = "\033[0m"
        green = "\033[32m"
        orange = "\033[33m"
        red = "\033[31m"
        pink = "\033[95m"
        lightgreen = "\033[92m"


gravity = 9.81
ggCoef = 2
max_accel = ggCoef * gravity  # Total available grip for acceleration/braking

# Track layout arrays
nextDistanceStep = [
    0,
    50,
    50,
    50,
    50,
    50,
    50,
    34,
    0,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    50,
    0,
    50,
    50,
    47,
    0,
    50,
    50,
    50,
    50,
    50,
    0,
    50,
    50,
    50,
    50,
    50,
]
trackRadius = [
    0,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    50,
    50,
    50,
    50,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

accelerationTable = []
decelerationTable = []

# --- 1. ACCELERATION (FORWARD PASS) ---
# Start at the apex speed of the initial configuration
initial_radius = trackRadius[0] if trackRadius[0] > 0 else 100
current_v = math.sqrt(initial_radius * gravity * ggCoef)
accelerationTable.append(current_v)

for distance, radius in zip(nextDistanceStep[1:], trackRadius[1:]):
    if radius > 0:
        # If in a turn, velocity is limited by lateral grip (Apex Velocity)
        v_turn = math.sqrt(radius * gravity * ggCoef)
        current_v = min(
            v_turn, math.sqrt(current_v**2 + 2 * max_accel * distance)
        )
    else:
        # On a straightaway, accelerate forward
        current_v = math.sqrt(current_v**2 + 2 * max_accel * distance)
    accelerationTable.append(current_v)

# --- 2. DECELERATION (BACKWARD PASS) ---
# Start from the end of the track and calculate grip limits backward
reversed_distances = list(reversed(nextDistanceStep))
reversed_radii = list(reversed(trackRadius))

end_radius = reversed_radii[0] if reversed_radii[0] > 0 else 50
current_v = math.sqrt(end_radius * gravity * ggCoef)
rev_decel_table = [current_v]

for distance, radius in zip(reversed_distances[1:], reversed_radii[1:]):
    if radius > 0:
        v_turn = math.sqrt(radius * gravity * ggCoef)
        current_v = min(
            v_turn, math.sqrt(current_v**2 + 2 * max_accel * distance)
        )
    else:
        # Working backward, "accelerating" means maximum allowable entry speed to slow down in time
        current_v = math.sqrt(current_v**2 + 2 * max_accel * distance)
    rev_decel_table.append(current_v)

# Flip it back to forward orientation
decelerationTable = list(reversed(rev_decel_table))

# --- 3. MERGE TABLES (THE REAL LAP PROFILE) ---
# The car can never exceed the lowest profile dictated by accel limits vs braking limits
finalTable = [
    min(acc, dec) for acc, dec in zip(accelerationTable, decelerationTable)
]

# --- 4. CALCULATE TRUE LAP TIME ---
total_lap_time = 0.0
print(
    f"{colors.fg.white}{'Dist':<6} | {'Final V':<10} | {'Accel V':<10} | {'Decel V':<10}"
)
print("-" * 50)

for i in range(len(nextDistanceStep)):
    dist = nextDistanceStep[i]
    v_final = finalTable[i]

    # Calculate segment travel time based on average speed across the distance step
    if i == 0 or dist == 0:
        segment_time = 0.0
    else:
        v_prev = finalTable[i - 1]
        v_avg = (v_prev + v_final) / 2
        segment_time = dist / v_avg if v_avg > 0 else 0.0

    total_lap_time += segment_time

    # Display profile comparison
    print(
        f"{colors.fg.green}{dist:<6} | {v_final:<10.2f} | {colors.fg.red}{accelerationTable[i]:<10.2f} | {colors.fg.orange}{decelerationTable[i]:<10.2f}"
    )

print(colors.fg.white + "-" * 50)
print(f"{colors.fg.pink}Total Calculated Lap Time: {total_lap_time:.3f} seconds")
