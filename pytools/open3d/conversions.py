import numpy as np
import open3d as o3d


def numpy_array_to_point_cloud(array):
    """
    Converts a numpy array to an Open3D point cloud.
    """
    assert array.shape[1] == 3
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(array)
    return cloud


def point_cloud_to_numpy_array(cloud):
    """
    Converts an Open3D point cloud to a numpy array.
    """
    array = np.asarray(cloud.points)
    return array
