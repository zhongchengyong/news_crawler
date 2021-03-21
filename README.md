# 给苹果的使用说明
## 前置步骤
1. 安装anaconda，检查是否安装成功，可以控制台(cmd)中输入python --version，如果输出版本号，说明安装成功了。 
2. 安装依赖包，大部分应该已经装好了。在cmd中执行：
> conda install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat requests

到此，软件安装完成。

## 使用
### 数据爬取
执行 
> scrapy crawl chinadaily

会在工程目录下生成一个covid-19.html，里面包含了title和content。数据量比较大，执行的时候会一直console刷新消息，等待即可。

### 数据可视化
执行
> python scrapy.py

可以生成词云图片

## 代码修改
主要修改 crawler下的chinadaily.py文件，
