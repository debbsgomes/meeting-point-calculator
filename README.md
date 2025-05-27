# Trilateration Meeting Point Finder

A Python script that uses trilateration to estimate the coordinates of a meeting point based on known locations and their distances to the meeting point.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Functions](#functions)
- [Input Format](#input-format)
- [Example Output](#example-output)
- [Use Cases](#use-cases)
- [Accuracy Considerations](#accuracy-considerations)
- [Limitations](#limitations)
- [Mathematical Background](#mathematical-background)

---

## Overview

This script implements a trilateration algorithm to determine the geographical coordinates of an unknown location (meeting point) when you know:

- The coordinates of **three or more reference locations**
- The distances from each reference location to the unknown meeting point

The algorithm uses mathematical optimization to minimize the error between calculated and known distances.

---

## How It Works

1. **Haversine Distance Calculation:** Computes the great-circle distance between two points on Earth's surface.
2. **Objective Function:** Calculates the sum of squared errors between known distances and calculated distances.
3. **Optimization:** Uses the Nelder-Mead method to find coordinates that minimize the error.
4. **Result:** Returns the most likely coordinates of the meeting point.

---

## Prerequisites

- Python 3.6+

---

## Installation

Install the required packages:

```bash
pip install numpy scipy
```

---

## Usage

Replace the placeholder coordinates in the `main()` function with actual GPS coordinates:

```python
# Known locations (latitude, longitude)
locations = [
    (-23.5505, -46.6333),  # São Paulo, Brazil
    (-22.9068, -43.1729),  # Rio de Janeiro, Brazil
    (-19.9167, -43.9345)   # Belo Horizonte, Brazil
]

# Distances in kilometers from each location to the meeting point
distances = [3.24, 2.35, 2.83]
```

Run the script:

```bash
python trilateration.py
```

---

## Example

```python
def main():
    # Example: Finding a meeting point in São Paulo area
    locations = [
        (-23.5505, -46.6333),  # Downtown São Paulo
        (-23.5475, -46.6361),  # Liberdade district
        (-23.5558, -46.6396)   # Vila Madalena
    ]
    
    # Distances in kilometers
    distances = [2.1, 1.8, 2.5]
    
    meeting_point = find_meeting_point(locations, distances)
    
    print(f"Meeting point coordinates:")
    print(f"Latitude: {meeting_point[0]:.6f}")
    print(f"Longitude: {meeting_point[1]:.6f}")
```

---

## Functions

### `haversine_distance(lat1, lon1, lat2, lon2)`

Calculates the great-circle distance between two points on Earth using the Haversine formula.

- **Parameters:**
  - `lat1, lon1`: Latitude and longitude of first point (in degrees)
  - `lat2, lon2`: Latitude and longitude of second point (in degrees)
- **Returns:** Distance in kilometers

### `objective_function(point, locations, distances)`

Calculates the sum of squared errors between calculated and known distances.

- **Parameters:**
  - `point`: Candidate coordinates `[latitude, longitude]`
  - `locations`: List of known location coordinates
  - `distances`: List of known distances to the meeting point
- **Returns:** Sum of squared errors

### `find_meeting_point(locations, distances)`

Main trilateration function that finds the optimal meeting point coordinates.

- **Parameters:**
  - `locations`: Array of known coordinates `[[lat1, lon1], [lat2, lon2], ...]`
  - `distances`: Array of distances from each location to the meeting point
- **Returns:** Optimized coordinates `[latitude, longitude]`

---

## Input Format

### Coordinates

- **Format:** Decimal degrees
- **Latitude:** Positive for North, negative for South
- **Longitude:** Positive for East, negative for West
- **Example:** São Paulo = `(-23.5505, -46.6333)`

### Distances

- **Unit:** Kilometers
- **Format:** List of numbers corresponding to each location
- **Example:** `[3.24, 2.35, 2.83]`

---

## Example Output

```
Meeting point coordinates:
Latitude: -23.548234
Longitude: -46.635891
```

---

## Use Cases

- Location forensics: Finding where someone was based on distance measurements
- GPS triangulation: Determining position from multiple reference points
- Archaeological surveys: Locating sites based on distance references
- Emergency services: Pinpointing locations from multiple distance reports
- Research applications: Any scenario requiring position determination from distance data

---

## Accuracy Considerations

- Minimum **3 locations** required for trilateration
- More locations generally improve accuracy
- Distance accuracy directly affects result precision
- Earth's curvature is accounted for using the Haversine formula
- Elevation differences are **not** considered (assumes flat Earth locally)

---

## Limitations

- Assumes distances are measured on Earth's surface
- Does **not** account for elevation differences
- Accuracy depends on the precision of input distances
- May not converge if distances are inconsistent or impossible

---

## Mathematical Background

The script uses:

- **Haversine formula** for great-circle distance calculation
- **Nelder-Mead optimization** for finding the best-fit coordinates
- **Least squares minimization** to reduce distance errors

This approach is commonly used in GPS systems, surveying, and location-based services.
