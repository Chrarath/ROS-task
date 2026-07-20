# 第二周任务
## 一、任务做的修改：
- 修改了发布的4个目标点坐标。
- 高度判断标准从 2.0m 改成了 1.5m。
- 话题名从 /target_point 改成了 /uav/target_point。
## 三、任务完成截图
-第一张截图：roslaunch 成功运行截图
<img width="724" height="498" alt="923444dd51f3a73dfc6e445f049988d1" src="https://github.com/user-attachments/assets/445e2d72-1fb4-45c5-bfa7-b34b29138a35" />
-第二张截图：rostopic list 看到 /target_point
<img width="724" height="498" alt="f34c2b0960fb6bc43c1f0a088ca710ca" src="https://github.com/user-attachments/assets/1ee9c046-9b42-44b8-a7d0-8b3e97af26ea" />
-第三张截图：rostopic echo /target_point 看到坐标
<img width="724" height="498" alt="192ccac5d4283f71248abb09a1f7dfb2" src="https://github.com/user-attachments/assets/5659a305-e8e1-4761-8157-0252ec23c6e1" />
## 二、target_pub -> /target_point -> target_sub 完整解释
- 各部分含义
target_pub：发布节点（Publisher）
负责持续生成目标点坐标数据，调用 ROS 发布 API，把消息发送到指定话题。
/target_point：话题（Topic，中间传输通道）
ROS 中节点异步通信的管道，斜杠开头代表全局话题名；所有发布、订阅该话题的节点都通过它中转数据。
target_sub：订阅节点（Subscriber）
监听 /target_point 话题，一旦收到 target_pub 发来的坐标消息，立刻执行自定义逻辑（计算高度、距离、方位并打印判断）。
- 整条链路逻辑
target_pub（生产者） → 把坐标消息丢进管道/target_point → target_sub（消费者）自动读取管道里的消息并处理
类比：广播电台（pub）→ 无线电频道（topic）→ 收音机（sub），频道一致才能收发通信。
## 三、运行过程遇到的报错及解决
### 报错1：订阅节点收不到目标点数据，rostopic echo /target_point无输出
原因：发布与订阅两端消息类型不匹配，或话题名拼写不一致。
解决：
- 使用`rostopic type /target_point`查看话题消息类型；
- 两端代码导入完全相同的消息文件；
- 执行catkin_make重新编译，source环境变量后重启roscore与两个节点。
### 报错 2：rostopic list 看不到 /target_point 话题
现象：运行完 target_pub，查询话题列表没有目标话题，订阅端完全接收不到信息。
原因：发布节点启动失败、代码内话题名写错，或节点中途异常退出。
解决：
- 查看发布节点终端日志，确认程序无崩溃报错；
- 核对代码中话题字符串，确保前后名称完全一致；
- 重新运行 target_pub，新开终端执行rostopic list验证话题是否出现。
