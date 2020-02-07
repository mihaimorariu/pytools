import numpy as np

def rotation3d(theta, axis):
    """
    Returns a rotation matrix based on a given rotation axis and angle.
    :param theta: rotation angle (in radians)
    :param axis: rotation axis
    :return:
    """
    rotation = dict()
    rotation['x'] = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    rotation['y'] = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    rotation['z'] = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

    if not (axis in ['x', 'y', 'z']):
        raise ValueError('Invalid value provided for the axes argument (expected: "x", "y" or "z").')

    return rotation[axis]
