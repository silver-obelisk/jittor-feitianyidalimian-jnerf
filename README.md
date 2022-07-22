| 第二届计图挑战赛B榜可微分渲染赛道开源

# Jittor 可微分渲染比赛 

## 简介
| 简单介绍项目背景、项目特点

本项目包含了第二届计图挑战赛计图 - 可微分渲染比赛的代码实现。本项目的特点是：采用了JNeRF方法对数据集进行重建

## 安装 
| 介绍基本的硬件需求、运行环境、依赖安装方法

本项目可在 1张 V100 上运行，每个数据集的训练时间约为20分钟。

#### 运行环境
- ubuntu 20.04 LTS
- python >= 3.7
- jittor >= 1.3.0

#### 安装依赖
执行以下命令安装 python 依赖
```
pip install -r requirements.txt
```
## 数据集
｜ 介绍数据集下载的方法
数据集可以在https://www.educoder.net/competitions/index/Jittor-3评测数据一栏中下载，请将下载好的数据集放在data文件夹内

## 训练
｜ 介绍模型训练的方法

运行python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Coffee.py命令获取Coffee数据集的训练结果，同样将ngp_Coffee改成ngp_Easyship可以获得
Easyship的训练结果，以此类推。训练结果保存在logs文件夹内。注意确保数据集已经放在data文件夹内，否则运行会报错




## 致谢
| 对参考的论文、开源库予以致谢，可选

此项目基于JNeRF实现，代码参考了https://github.com/Jittor/JNeRF。

## 注意事项

点击项目的“设置”，在Description一栏中添加项目描述，需要包含“jittor”字样。同时在Topics中需要添加jittor。

![image-20220419164035639](https://s3.bmp.ovh/imgs/2022/04/19/6a3aa627eab5f159.png)
