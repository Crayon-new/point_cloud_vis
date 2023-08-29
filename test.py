import copy
import numpy as np
import open3d as o3d
import json

def sustech_label_to_numpy(label):
    result = np.ones((len(label),7))
    for i in range(len(label)):
        result[i][0] = label[i]['psr']['position']['x']
        result[i][1] = label[i]['psr']['position']['y']
        result[i][2] = label[i]['psr']['position']['z']-label[i]['psr']['scale']['z']/2+0.05
        result[i][3] = label[i]['psr']['scale']['x']
        result[i][4] = label[i]['psr']['scale']['y']
        result[i][5] = label[i]['psr']['scale']['z']
        result[i][6] = -label[i]['psr']['rotation']['z']
    return result

def draw_2d(data_2d):
    import numpy as np
    import matplotlib.pyplot as plt

    # 创建二维数组
    # data_2d = np.random.rand(100, 3)  # 100个点的随机数据，每个点包含x、y、z坐标

    # 提取x和y坐标
    x_coords = data_2d[:, 0]
    y_coords = data_2d[:, 1]

    # 绘制投影
    plt.scatter(x_coords, y_coords,s = 0.1, c='b', marker='o')  # 使用散点图绘制x和y坐标
    plt.xlabel('X-coordinate')  # 设置x轴标签
    plt.ylabel('Y-coordinate')  # 设置y轴标签
    plt.title('Projection on XY-plane')  # 设置标题
    plt.axis('equal')  # 设置坐标轴刻度相等，保证图像比例正确
    plt.show()  # 显示图像

if __name__ == "__main__":
    from open3d_vis import Visualizer
    print("Testing nus_vis in open3d ...")

    # points = np.load('/home/hzj/github_respo/point_cloud_vis/resource/n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852875947629_points.npy')
    points = o3d.io.read_point_cloud("/home/hzj/github_respo/SUSTechPOINTS/data/scene1/pcd/1_54.pcd")
    points = np.asarray(points.points)
    label_file = "/home/hzj/github_respo/SUSTechPOINTS/data/scene1/label/1_54.json"
    with open(label_file,'r') as file:
        label = json.load(file)
    pred = sustech_label_to_numpy(label)
    draw_2d(points)
    # pred = np.load('/home/hzj/github_respo/point_cloud_vis/resource/pred1.npy')
    pred_labels = None
    vars = None
    # pred_labels = np.load('/home/hzj/github_respo/point_cloud_vis/resource/n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852874947918/n015-2018-09-25-13-17-43+0800__LIDAR_TOP__1537852874947918_pred_labels.npy')
    # vars = np.load('./resource/vars.npy')
    

    # for p, v in zip(max_pred, vars):
    #     p[3] = p[3]+v[4]
    #     p[4] = p[4]+v[3]
    #     p[5] = p[5]+v[5]
    
    # for p, v in zip(min_pred, vars):
    #     p[3] = p[3]-v[4]
    #     p[4] = p[4]-v[3]
    #     p[5] = p[5]-v[5]

    # vis = Visualizer(points)

    # if pred_labels:
    #     palette = np.random.randint(
    #         0, 255, size=(pred_labels.max() + 1, 3)) / 256
    #     labelDict = {}
    #     for j in range(len(pred_labels)):
    #         i = int(pred_labels[j])
    #         if labelDict.get(i) is None:
    #             labelDict[i] = []
    #         labelDict[i].append(pred[j])
    #     for i in labelDict:
    #         vis.add_bboxes(
    #             bbox3d=np.array(labelDict[i]),
    #             bbox_color=palette[i],
    #             points_in_box_color=palette[i])
    # else:
    #     for i in range(len(pred)):
    #         _color = (72/255,101/255,241/255)
    #         vis.add_bboxes(bbox3d=pred[i:i+1],
    #                        bbox_color=_color)

    # # vis.add_bboxes(min_pred, bbox_color=np.array((255,0,0)))
    # # vis.add_bboxes(max_pred, bbox_color=np.array((255,0,0)))

    # vis.show()
 
    # # cords = o3d.geometry.TriangleMesh.create_coordinate_frame()
    # # o3d.visualization.draw_geometries([mesh])