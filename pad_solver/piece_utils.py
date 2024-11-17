import math
import numpy as np

ROTATION_ANGLES = [0 ,math.pi/2, math.pi, 3*math.pi/2]

def rotation_matrix_for_angle(theta):
    return [[math.cos(theta), math.sin(theta)],[-math.sin(theta), math.cos(theta)]]

def rotate(points, angle):
    rotation_matrix = rotation_matrix_for_angle(angle)
    return [(int(x),int(y)) for x,y in [np.around(x) for x in np.matmul(points, rotation_matrix)]]

def traslate(points,to_position):
    x1,y1 = to_position
    return [(x+x1, y+y1) for x,y in points]

def reflect_x(points):
    return [(-x, y) for x,y in points]

def reflect_y(points):
    return [(x, -y) for x,y in points]

def get_rotation_variations(points):
        rotation_variations = [rotate(points,theta) for theta in ROTATION_ANGLES]
        return rotation_variations
   
def normalize(points):
    min_x = min(x for x, _ in points)
    min_y = min(y for _, y in points)
    normalized = sorted((x - min_x, y - min_y) for x, y in points)
    return tuple(normalized)

def get_all_variations(points):
    transformations = set()
    
    rotations = get_rotation_variations(points)
    for rot in rotations:
        transformations.add(normalize(rot))
    
    reflections = [
        reflect_x(points),
        reflect_y(points)
    ]
    
    for reflection in reflections:
        refl_rotations = get_rotation_variations(reflection)
        for reflection_rotation in refl_rotations:
            transformations.add(normalize(reflection_rotation))

    return transformations
