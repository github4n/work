文档是后来补写，可能有遗忘或者写错
版本:num_ocr[1.0.0.0]
1.开发和自测环境
	win7
	python3.6.5
2.安装依赖
	tesseract，版本4.0（3.05版本试过也可）
	ffmpeg
3.python主要安装依赖包 （可根据提示pip install）
	yaml(PyYAML):logging日志的yaml配置解析
	
	pytesseract：用于识别
	
	cv2(opencv-conrib-python):图片处理，裁剪、降噪、灰度
	
	PIL(Pillow):格式转换，用于识别的图片格式
	
	requests:http库
4.配置
	.conf配置:程序的基本配置，包括地址、超时时间、路径等
	.yml配置：程序的logging日志配置
5.命令行,
	可命令行指定.conf(-c)和.yml(-log)的路径
6.num_my.traineddata文件
	自制简单的数字训练集,放在tesseract安装目录的tessdata目录下使用

