#Q1
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        # √((x2 - x1)^2 + (y2 - y1)^2)
        return math.hypot(other.x - self.x, other.y - self.y)

    def midpoint(self, other):
        # Midpoint: ((x1 + x2)/2, (y1 + y2)/2)
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def line_equation(self, other):
        # Slope m = (y2 - y1)/(x2 - x1), Intercept c = y - mx
        if self.x == other.x:
            return "Vertical line: x = {}".format(self.x)
        m = (other.y - self.y) / (other.x - self.x)
        c = self.y - m * self.x
        return f"y = {m:.2f}x + {c:.2f}"

    def reflect_over_line(self, A, B):
        # Reflect point over line AB using vector projection
        dx = B.x - A.x
        dy = B.y - A.y
        a = dx * dx - dy * dy
        b = 2 * dx * dy
        d = dx * dx + dy * dy
        x = ((a * (self.x - A.x) + b * (self.y - A.y)) / d) + A.x
        y = ((b * (self.x - A.x) - a * (self.y - A.y)) / d) + A.y
        return Point(x, y)

A = Point(1, 2)
B = Point(4, 6)
C = Point(3, 5)

print("Distance A-B:", A.distance_to(B))
print("Midpoint A-B:", vars(A.midpoint(B)))
print("Line Equation A-B:", A.line_equation(B))
print("Reflection of C over AB:", vars(C.reflect_over_line(A, B)))


#Q2
import numpy as np

A = np.array([2, 3])
B = np.array([4, -1])
C = np.array([-1, 2])

# 1. Vector Addition
R = A + B + C
print("Resultant Vector R:", R)

# 2. Magnitudes
print("Magnitude of A:", np.linalg.norm(A))
print("Magnitude of B:", np.linalg.norm(B))
print("Magnitude of C:", np.linalg.norm(C))

# 3. Dot Products
print("A·B:", np.dot(A, B))
print("A·C:", np.dot(A, C))
print("B·C:", np.dot(B, C))

# 4. Angles Between Vectors
def angle_between(u, v):
    cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return np.degrees(np.arccos(np.clip(cos_theta, -1.0, 1.0)))

print("Angle A-B:", angle_between(A, B))
print("Angle A-C:", angle_between(A, C))
print("Angle B-C:", angle_between(B, C))

# 5. Projection of A onto B
proj = (np.dot(A, B) / np.dot(B, B)) * B
print("Projection of A onto B:", proj)


#Q3
def closest_point_on_segment(S, E, P):
    # Vector projection of SP onto SE
    SE = E - S
    SP = P - S
    t = np.dot(SP, SE) / np.dot(SE, SE)
    t = max(0, min(1, t)) 
    return S + t * SE

S = np.array([0, 0])
E = np.array([4, 4])
P = np.array([2, 0])

# 1. Segment Length
length = np.linalg.norm(E - S)
print("Length of Segment SE:", length)

# 2. Closest Point on Segment
closest = closest_point_on_segment(S, E, P)
print("Closest Point on SE to P:", closest)

# 3. Distance from P to Segment
distance = np.linalg.norm(P - closest)
print("Distance from P to Segment:", distance)


#Q4
def line_intersection(a1, b1, c1, a2, b2, c2):
    # Solve system: a1x + b1y = c1 and a2x + b2y = c2
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    try:
        solution = np.linalg.solve(A, B)
        return f"Intersection Point: ({solution[0]:.2f}, {solution[1]:.2f})"
    except np.linalg.LinAlgError:
        return "Lines are parallel or coincident."

print(line_intersection(1, -1, 0, 2, -2, 4))