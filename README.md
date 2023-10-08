# SeeleAssistant 崩坏3/崩坏三全自动托管项目
不会代码的舟游脚本up下岗再就业了,此脚本仍在测试阶段，维护更新正常进行，支持项目往下滑，模拟器兼容性测试拉到底  
此项目于2023.10.03创立，由于是个人项目发展进度较慢，一个人要熬秃头了（悲），大体路线主干稳定性测试（dev7完成）→做GUI→学OpenCV→Windows支持  
有问题会日更的，没问题就搓炸弹test_All搓出来的低质量炸弹代码已经快600行了（悲）  
从dev9开启添加浅层乐土支持（人物攻击逻辑），选关逻辑恕我没学OpenCV没法做，深层乐土还得搁置  
## 注意事项  
·此脚本基于Windows下python的多个子项目，此脚本暂时只对安卓模拟器生效，待稳定后向Windows原生窗口迁移，目前您仍然需要下载安装蓝叠国际蓝叠5（Bluestacks5）Pie-64或者Nougat-64，并在其中安装崩坏3以使用此脚本。  
·此脚本本人由于精力有限只对蓝叠国际（蓝叠5） Pie64版本做支持，其他模拟器的使用效果您可以发送邮件告知我，使用其他模拟器需要改/Android/config.py里的adb连接与模拟器启动位置  
## 脚本说明
安装脚本（克隆仓库）
```
git clone -b Dev-seele https://github.com/BronOfFireUnkn/SeeleAssistantCore.git
```
·此项目需要python≥3.10方可正常运行，此项目采用虚拟环境（venv）运行，缺点是占用空间较大，优点是卸载无任何残留，仅需删除整个项目文件夹即可完成卸载    
·安装完毕python后（安装时建议勾选ADD to PATH），启动安装依赖文件.bat，会自动创建python虚拟环境，然后在config.py配置文件中修改变量，运行start_android.bat即可,此脚本会自动git pull拉取更新，无需更新选择NO UPDATE即可，需要检查更新有个Update Only.bat  
·如果您想参与测试，请在AirtestIDE中（需要下载AirtestIDE）打开/test area/test_All.py即可运行
## 支持项目
### 最后更新时间 2023/10/07 13:43（请注意由于维护原因时效性可能滞后）
|支持项目|目前状态|备注|最后更新版本|第三方运行库|
|:----:|:----:|:----:|:----:|:----:|
|总流程|/|基本完成|dev7|airtest,opencv,pynput|
|作战任务|支持|完成|dev6|airtest|
|作战奖励|支持|/|dev7|airtest|
|邮件收取|支持|/|dev7|airtest|
|材料远征|支持|/|dev5|airtest|
|万象二|支持|通用|dev7|airtest|
|家园-收取金币体力|支持|完成|dev5|airtest|
|家园-远征|支持|完成|dev6|airtest|
|家园-打工|支持|完成|dev7|airtest|
|商店购买|支持|完成|dev3|airtest|
|接取任务|支持|不推荐用|dev3|airtest|
|战场扫荡|支持|/|dev7|airtest|
|舰团|支持|完成|dev7|airtest|
|戳戳舰娘|支持|完成|dev2|airtest|
|万象四|Next|专用|/|airtest|
|万象六|Next|专用|/|airtest|
|万象七|Next|专用|/|airtest|
|完成任务|Next|弯道超车|/|airtest,opencv,pynput|
|商城周期礼包|Will Be|/|/|airtest|
|往世乐土（浅层）|逐步支持|/|dev9|airtest|
|往世乐土（2.25）|搁置|等待队列|/|airtest,opencv,pynput|
## 联系作者
B站私信不看，有问题发邮件  
B站：[无铭_BronOfFire](https://space.bilibili.com/36254944)  
邮箱：bronoffire_unkn@petalmail.com  
## 模拟器兼容性报告
### [蓝叠国际 蓝叠5（Bluestacks5）](https://www.bluestacks.com/download.html)
|版本|状态|  
|:----:|:----:|
|Nougat-32(Android 7-32)|被淘汰,建议别用|  
|Nougat-64(Android 7-64)|兼容，可运行，正常识别|  
|Pie-64(Android 9-64)|兼容，可运行，正常识别|  
|Android 11-64|崩坏3闪退，无法运行|  
## 吐槽
其实你从功能上来看可以看成是HonKai Helper的重制版，只不过他好多写的不细，也好久没更新了，受不了一点，还是决定自己搓一个炸弹出来
