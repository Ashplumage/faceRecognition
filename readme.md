<html>
<head></head>
<body>
<h1>readme</h1>
<h2>代码用途</h2>
<p>人脸识别sample代码，通过利用opencv内置分类器寻找人脸，并通过截取和写入本地磁盘，实现训练和测试集数据的采集，并利用tensorflow训练搭建CNN神经网络，训练人脸识别分类器。
将训练好的分类器模型写入本地.h5的文件中，读取分类器再次调用opencv对人脸进行识别，若成功识别，则用opnecv文字框做出说明
</p>
<h2>代码结构</h2>
<ul>
<li><p codes/>
	<ul>
	<li>open_camera.py</li>
	<li>faceDetectWithOpencv.py</li>
	<li>getTrainData.py</li>
	<li>loadData.py</li>
	<li>trainByKeras.py</li>
	<li>face_recognize.py</li>

</ul>

<li>

<li>testdata<li>

<li>traindata<li>
</ul>
</body>
</html>
