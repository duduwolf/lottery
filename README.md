### 基于Three.js的3D动态球体

#### 开发背景及过程
儿子的班级老师需要一个能在上课时随机抽选学生进行背诵课文，本来准备用python+pyqt5来实现，后面发现使用基于WebGL的浏览器来展示效果更好，最主要开发起来简单多了。

整整看了一个周末的Three.js，被三维空间的xyz坐标、相机、光源、旋转搞晕了，都怪高中和大学的数学全还给老师了，平移、弧线移动的三角函数算法基本忘光，更别说矩阵、椭圆、线性代数之类的了。。。

不过好在参考网上的例子，改来改去基本修改成功了，look index.html

#### 记下踩过的坑

- [TrackballControls](https://github.com/gtsop/threejs-trackball-controls)的效果的确非常棒，但修改起来难度就更大了，到现在我都无法实现TrackballControls里那种丝绸般顺滑的旋转动画。。。
- ThreeJS中的camera、scene、tween（补间动画）、control、render等概念基本理解了，但类似于Vector、三维空间的位置计算等等概念就干脆搞不懂了。