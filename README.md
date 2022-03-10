# 文件结构

- code：代码文件夹，内层嵌套文件夹`  ./code/core  `放置核心代码、`  ./code/visualize  `放置可视化代码
- display：报告中插图所在文件夹
- report：报告文件夹，`.md`版本和`.pdf`版本
- result：存放八皇后N=1至N=11每个输入下合理局面的情况，每个`.txt`第一行为合理局面总数`num`，其余为`num`个序列，每个序列唯一确定一种合理局面，表示第1行至第N行每行皇后所放置的列数（也是从1至N）
- video：可视化展示视频，分别演示了N=8输入下单步展示部分合理局面以及N=5输入下连续展示共10种合理局面的功能，其中连续执行时会循环播放。
- README：说明文档

