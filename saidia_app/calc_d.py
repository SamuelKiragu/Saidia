# class template for holding a point's coordinates 
class Point:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


# function takes two point objects and calculates distance between points
def distance(point1, point2):
    return abs(point2.lat - point1.lat) + abs(point2.lng - point1.lng)
