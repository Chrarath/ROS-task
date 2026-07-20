# 第二周任务二：ROS 目标点发布与订阅小实验

这个仓库是第二周任务二的示范代码。任务目标是让大家理解 ROS 里 `node`、`topic`、`msg`、`launch` 的基本关系：一个节点发布目标点，一个节点订阅目标点并输出判断结果。

## 一、任务要做什么

本任务需要完成三件事：

1. **跑通示范代码**

   能看到发布端输出目标点，订阅端输出方向、高度和距离。

2. **提交三张截图**

   - `roslaunch` 成功运行截图。
   - `rostopic list` 看到 `/target_point` 截图。
   - `rostopic echo /target_point` 看到坐标截图。

3. **自己改一点点代码**

   至少改一个地方，比如：

   - 修改发布的 4 个目标点坐标。
   - 把高度判断标准从 `2.0m` 改成 `1.5m`。
   - 把话题名从 `/target_point` 改成 `/uav/target_point`。
   - 在自己的 README 里解释 `target_pub -> /target_point -> target_sub` 是什么意思。

## 二、代码结构

```text
week2_ros_practice/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── week2_target.launch
└── scripts/
    ├── target_pub.py
    └── target_sub.py
```

每个文件的作用：

- `target_pub.py`：发布目标点，话题名是 `/target_point`，消息类型是 `geometry_msgs/Point`。
- `target_sub.py`：订阅 `/target_point`，收到坐标后输出方向、高度状态和距离。
- `week2_target.launch`：一条命令同时启动发布节点和订阅节点。
- `package.xml`：声明这个 ROS 包依赖 `rospy` 和 `geometry_msgs`。
- `CMakeLists.txt`：告诉 catkin 这个包需要安装哪些 Python 节点。

## 三、安装和运行指令

下面的指令在 Ubuntu 终端里输入。建议环境是 Ubuntu 20.04 + ROS Noetic。

### 1. 创建 catkin 工作空间

如果你已经有 `~/catkin_ws`，可以跳过这一步。

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### 2. 克隆这个仓库

注意：请在 `~/catkin_ws/src` 目录下克隆。

```bash
cd ~/catkin_ws/src
git clone https://github.com/kkkkkai-pro/SECOND.git week2_ros_practice
```

如果你的电脑访问 GitHub 很慢，也可以在 Windows 下载 zip，再复制到 Ubuntu 的 `~/catkin_ws/src/week2_ros_practice`。

### 3. 编译工作空间

```bash
cd ~/catkin_ws
chmod +x src/week2_ros_practice/scripts/*.py
catkin_make
source devel/setup.bash
```

### 4. 启动发布和订阅节点

```bash
roslaunch week2_ros_practice week2_target.launch
```

正常情况下，终端会持续输出类似内容：

```text
[INFO] 发布目标点: x=1.00, y=2.00, z=1.50
[INFO] 收到目标点: x=1.00, y=2.00, z=1.50 | 方向=正前方/左侧 | 高度正常 | 距离=2.69m
```

这张就是你要提交的第一张截图：`roslaunch` 成功运行截图。

### 5. 检查话题列表

重新打开一个 Ubuntu 终端，输入：

```bash
source ~/catkin_ws/devel/setup.bash
rostopic list
```

正常情况下，应该能看到：

```text
/rosout
/rosout_agg
/target_point
```

这张就是你要提交的第二张截图：`rostopic list` 看到 `/target_point`。

### 6. 查看目标点坐标

还是在第二个终端里输入：

```bash
rostopic echo /target_point
```

正常情况下，应该能看到类似：

```text
x: 1.0
y: 2.0
z: 1.5
---
x: 2.0
y: -1.0
z: 1.2
---
```

这张就是你要提交的第三张截图：`rostopic echo /target_point` 看到坐标。

## 四、你需要理解的内容

这个示范的数据流是：

```text
target_pub -> /target_point -> target_sub
```

含义是：

- `target_pub` 是发布节点，负责产生目标点坐标。
- `/target_point` 是话题，负责传递目标点坐标。
- `target_sub` 是订阅节点，负责接收目标点并进行判断。

在真实无人机任务里，类似的数据流可能会变成：

```text
视觉识别节点 -> 目标点话题 -> 规划/控制节点
```

所以这个任务虽然很小，但它是后面做视觉、规划、仿真的基础。

## 五、作业提交要求

每位同学提交一个文件夹，建议命名为：

```text
姓名_week2_ros_practice
```

里面至少包含：

- 修改后的代码。
- `roslaunch` 成功运行截图。
- `rostopic list` 看到 `/target_point` 截图。
- `rostopic echo /target_point` 看到坐标截图。
- 一个简单 README，说明你改了哪里、遇到了什么报错、怎么解决的。

## 六、常见报错

### 1. 找不到包

如果出现类似 `week2_ros_practice not found`，一般是没有 source：

```bash
source ~/catkin_ws/devel/setup.bash
```

也可能是仓库没有放在 `~/catkin_ws/src` 下面。

### 2. Permission denied

如果 Python 文件没有执行权限，输入：

```bash
chmod +x ~/catkin_ws/src/week2_ros_practice/scripts/*.py
```

### 3. No module named rospy

一般是 ROS 环境没有生效：

```bash
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
```

### 4. 只有发布，没有订阅输出

可以检查节点和话题：

```bash
rosnode list
rostopic info /target_point
```

如果 `target_sub` 没启动，检查 `launch/week2_target.launch` 有没有写错。

## 七、评分参考

- 60 分：能跑通示范代码。
- 75 分：能提交三张截图。
- 85 分：能自己改一个地方，并说明改了什么。
- 95 分：能解释 `target_pub -> /target_point -> target_sub`，并记录至少 2 个报错和解决方法。
