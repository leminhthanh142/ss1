from math import radians, sin, cos, asin, sqrt

earth_radius = 6371  # kilometers


def haversine(point_a, point_b):
    (lat1, lon1) = point_a
    (lat2, lon2) = point_b

    # convert to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # longitudes distance
    lon_distance = lon2 - lon1

    # latitudes distance
    lat_distance = lat2 - lat1

    temp = (pow(sin(lat_distance / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(lon_distance / 2), 2))
    final = 2 * earth_radius * asin(sqrt(temp))

    return round(final, 2)


if __name__ == '__main__':
    distance = haversine((35.28831667, -120.6529), (46.60005, -112.0388333))
    print(f"distance between two point: {distance}km")
