import numpy as np
from scipy.optimize import minimize

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points on Earth using Haversine formula"""
    R = 6371  # Earth's radius in kilometers
    
    # Convert latitude/longitude to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return R * c

def objective_function(point, locations, distances):
    """Calculate sum of squared errors between calculated and known distances"""
    lat, lon = point
    error = 0
    
    for (loc_lat, loc_lon), dist in zip(locations, distances):
        calculated_dist = haversine_distance(lat, lon, loc_lat, loc_lon)
        error += (calculated_dist - dist)**2
    
    return error

def find_meeting_point(locations, distances):
    """Find the meeting point using trilateration"""
    # Use the center point of all locations as initial guess
    initial_guess = np.mean(locations, axis=0)
    
    # Minimize the objective function
    result = minimize(
        objective_function,
        initial_guess,
        args=(locations, distances),
        method='Nelder-Mead'
    )
    
    return result.x

def main():
    # Known locations (latitude, longitude)
    # You would need to replace these with actual coordinates
    meeting_location = (-00.0000, -00.000) 
    
    # Example locations (these need to be replaced with actual coordinates)
    locations = [
        (-00.0000, -00.000),  # Initial Place #1
        (-00.0000, -00.000),  # Initial Place #2
        (-00.0000, -00.000)   # Initial Place #3
    ]
    
    # Distances in kilometers
    distances = [3.24, 2.35, 2.83]
    
    # Find the meeting point
    meeting_point = find_meeting_point(locations, distances)
    
    print(f"The meeting point was likely at coordinates:")
    print(f"Latitude: {meeting_point[0]:.6f}")
    print(f"Longitude: {meeting_point[1]:.6f}")

if __name__ == "__main__":
    main()
