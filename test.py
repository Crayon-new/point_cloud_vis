import copy
import numpy as np
import open3d as o3d

if __name__ == "__main__":
    from open3d_vis import Visualizer
    print("Testing nus_vis in open3d ...")

    points = np.load('D:\\gitlib\\nuScenes_viz\\resource\\n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852875947629_points.npy')
    pred = np.load('D:\\gitlib\\nuScenes_viz\\resource\\pred1.npy')
    pred_labels = np.load('D:\\gitlib\\nuScenes_viz\\resource\\n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852874947918\\n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852874947918_pred_labels.npy')
    vars = np.load('./resource/vars.npy')
    

    # for p, v in zip(max_pred, vars):
    #     p[3] = p[3]+v[4]
    #     p[4] = p[4]+v[3]
    #     p[5] = p[5]+v[5]
    
    # for p, v in zip(min_pred, vars):
    #     p[3] = p[3]-v[4]
    #     p[4] = p[4]-v[3]
    #     p[5] = p[5]-v[5]

    vis = Visualizer(points)
    if pred_labels is None:
        palette = np.random.randint(
            0, 255, size=(pred_labels.max() + 1, 3)) / 256
        labelDict = {}
        for j in range(len(pred_labels)):
            i = int(pred_labels[j])
            if labelDict.get(i) is None:
                labelDict[i] = []
            labelDict[i].append(pred[j])
        for i in labelDict:
            vis.add_bboxes(
                bbox3d=np.array(labelDict[i]),
                bbox_color=palette[i],
                points_in_box_color=palette[i])
    else:
        vis.add_bboxes(pred)

    # vis.add_bboxes(min_pred, bbox_color=np.array((255,0,0)))
    # vis.add_bboxes(max_pred, bbox_color=np.array((255,0,0)))
    vis.show()
 
    # cords = o3d.geometry.TriangleMesh.create_coordinate_frame()
    # o3d.visualization.draw_geometries([mesh])