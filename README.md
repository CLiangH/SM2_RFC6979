项目目标
=

Implement sm2 with RFC6979

实现原理
=

![image](https://github.com/CLiangH/Picture/blob/main/SM21.png)

其中随机数k生成时我们使用伪随机（Hash）代替真随机。

代码解析
=

上述椭圆曲线加法数乘以及GCD等算法不在赘述，本题为实现方便，我们选择椭圆曲线为$y^2$=$x^3$+2x+2。
在函数开始时首先初始化Za=SM3(LENA||IDA||a||b||xG||yG||xA||yA).

__签名算法__
_______________

首先将Za与消息级联并使用SM3加密得到参数e.由于此处我们使用RFC6979，因此选取k时，我们首先将私钥、明文Hash和所用算法名称级联，之后过一遍SM3将其转化为数字，
从而代替随机选取。之后依次求取kG、r、s即可。

__验证算法__
________________

首先按上述步骤求出e，之后计算

`t=(r+s) mod n`

`S=sG+tP`

`R=(e+S[0]) mod n`

如果`R==r`，则验证成功，反之失败。

运行指导
=

代码可直接运行

运行截图
=

![image](https://github.com/CLiangH/Picture/blob/main/SM22.png)
