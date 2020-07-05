###学习笔记

###selenium-webdriver
1. 从[ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) 下载浏览器驱动包
2. 将驱动包放置到虚拟环境bin目录下
3. 通过selenium-webdriver可以调用浏览器，查看代码执行情况
4. 如果页面中的链接地址是写在前端JS代码中的那么也可以使用selenium-webdriver来模拟请求
5. WebDriver 文档：
   - https://www.w3.org/TR/webdriver/ 
   - https://www.selenium.dev/selenium/docs/api/py/ 

###识别图片验证码
- 先安装依赖库libpng, jpeg, libtiff, leptonica，tesseract
    - brew install leptonica
    - brew install  tesseract
- Python 需要调用C/C++封装好的包,来进行图片中字符和文字的提取
- [各种语言识别库](https://github.com/tesseract-ocr/tessdata)

###Scrapy下载中间件
- Scrapy 已经内置实现了很多[下载中间件](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-DOWNLOADER_MIDDLEWARES_BASE)
- 中间件执行顺序由map中的值来决定,第一个中间件(数值最小)是最靠近引擎的，最后一个中间件(数值最大)是最靠近下载器的。
- DOWNLOADER_MIDDLEWARES 设置会与Scrapy定义的 DOWNLOADER_MIDDLEWARES_BASE 设置合并,不是覆盖
- 如果不想执行某个中间件则将其值设置为：None；例如：'week02_01.middlewares.Week0201DownloaderMiddleware': None
- 自定义中间件需要在settings.py中的 DOWNLOADER_MIDDLEWARES 进行配置
- 自定义中间件建议通过继承方式来实现

###Scrapy自定义pipeline
- pipeline的应用场景
    - 清理HTML数据
    - 验证爬取的数据(检查item包含某些字段)
    - 查重(并丢弃)
    - 将爬取结果保存到数据库中
- 自定义Pipeline需要实现的函数
    - init
    - from_crawler
    - open_spider
    - close_spider
    - process_item
- 上述函数执行顺序
    1. from_crawler 
    2. __init__ 
    3. open_spider 
    4. process_item(每个item都会调用一次) 
    5. close_spider
 - 除process_item函数每个item都会调用一次外，其余函数只会执行一次
    
    