## 学习笔记
###学习笔记

####Scrapy核心组件
	1. 引擎（Engine）
		a. “大脑”，指挥其他组件协同工作
	2. 调度器（Scheduler）
		a. 调度器接收引擎发过来的请求，按照先后顺序，压入队列中，同时去除重复的请求
	3. 下载器（Downloader）
		a. 下载器用于下载网页内容，并返回给爬虫
	4. 爬虫 （Spiders）
		a. 用于从特定的网页中提取需要的信息，即所谓的实体（item）
		b. 用户也可以从中提取出链接，让scrapy继续抓取下一个页面
	5. 项目管道（item Pipelines）
		a. 负责处理爬虫从网页中抽取的实体
		b. 主要负责数据持久化，验证实体有效性，清除不需要的信息
	6. 下载器中间件 （Downloader Middleware）
	7. 爬虫中间件（Spider Middleware）

####Scrapy执行流程
	1. Spiders 发起请求给engine
	2. engine将引擎发送给调度器
	3. scheduler依次执行爬取请求
	4. engine负责将队列中请求发送给downloader
	5. downloader访问网页并返回response对象给engine
	6. engine将response对象发送给spiders
	7. spiders解析response提取出items/requests，并返回给engine
	8. engine将ietms发送给pipelines，requests发送给scheduler

####Scrapy开发环境搭建
    1. 为初始化操作，一个scrapy项目里可以包含多个spider
        scrapy startproject spiders
    2. 进入spiders目录，目录，注意由于project名称为spiders，因此终端提示需要修改为cd spiders/spiders
        /Users/risheng/OneDrive/DMiner/geekTime/geekbangtrain/spiders/spiders 
    3. 创建spider，需要两个参数，
        参数1: spider名称，后续用于启动spider；
        参数2: 爬取网站所对应的域名
        scrapy genspider 参数1 参数2
        scrapy genspider movies douban.com 

###Scrapy爬虫&管道开发
    1. 开发中一般只需要专注与一下几个脚本:
        settings.py 配置请求头、管道对象等参数
        pipelines.py 管道开发，在这个脚本中将数据持久化，需要注意：Don't forget to add your pipeline to the ITEM_PIPELINES setting
        spiders目录下/spider名称.py 爬虫器脚本，用于解析网页提取item返回给pipelines，或者再次生成request
    1. 首先重写start_requests()方法，指定爬虫第一次请求链接，并且在callback中指定解析函数
    2. 注意：yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        如果dont_filter=True，是用来解除去重功能。
        Scrapy 自带 url 去重功能，第二次请求之前会将已发送的请求自动进行过滤处理。
        所以将 dont_filter 设置为 True 起到的作用是解除去重功能，

####Xpath入门
    1. XPath分为绝对路径和相对路径两种
    2. 相对路径-选取节点
        /	从根节点选取。
        //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
        .	选取当前节点。
        ..	选取当前节点的父节点。
        @	选取属性。

####yield
    1. 返回的值必须是对象
    2. 在一段逻辑处理中，可以单独返回一个值，不需要考虑数据类型
    3. next函数提取一个值，list函数提取所有值；
    4。 当提取完全部值后，如果再调用next将会抛出异常,调用list返回一个空列表

####推导式
    1. 生成新的列表、字典和元组
    2. 生成元组类型需要显示指定,通过tuple()函数生成; 如果不指定,只使用()将会返回一个生成器
    3. 生成列表：
            [i ** 2 for i in range(1, 11) if i > 5]
            [ 生成值语句 for循环语句 condition语句] 
            三部分组成
    4. 生成字典：
            {i: i*i for i in (5,6,7)}
    5. 生成元组：
            tuple(i for i in range(0, 11))
            