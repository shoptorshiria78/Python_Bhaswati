# Polygon Area Calculator using Shoelace formula

def polygon_area(coords):
    n = len(coords)  # number of vertices
    area = 0
    
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]  # next vertex (wraps around to 0)
        area += (x1 * y2) - (x2 * y1)
    
    return abs(area) / 2


# Example: Polygon with vertices
# Square with points (0,0), (4,0), (4,4), (0,4)
points = [(0, 0), (4, 0), (4, 4), (0, 4)]

print("Area of polygon:", polygon_area(points))
