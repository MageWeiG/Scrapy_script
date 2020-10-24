# Scrapy_script

## software
这个文件夹下面是一个scrapy爬虫的框架，使用conda来配置的虚拟环境

爬虫的功能是，爬取联想应用商店的各种类型的软件中，下载量在5万以上的软件的信息。

环境的配置在`scrapy_py3.yaml`文件里面，使用`conda env create -f scrapy_py3.yaml`命令导入环境。

运行爬虫的命令是`scrapy crawl downs -o softt.csv`结果将输出到同目录下的`softt.csv`文件中。

