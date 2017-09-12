### 1A  

和 API 欢快玩耍

搞定你的首个 MVP，现在你是不是内心特别欣喜，感觉自己潜力无限？

啊哈，请保持这样的自信，迎接本章新挑战 —— 用 API 获取真实、实时的天气数据，让你的程序与真实世界互通起来。

API ~ Application Programming Interface

完成本章任务，你的小小程序，将可以为你播报最新天气情况，想想就超酷 ;-) 你甚至会惊奇地发现，编程在这个世界上有如此多好玩的用法，还有无数 API 任意调用。

新的世界，在你眼前渐渐展开。欢迎来到新世界！

### 1B
如果 2wd1 11:42 前，你还未完成 ch0 挑战，建议你按下述建议行动，跳过其它无关行动：

先用 Python3 改写 7 个《Learn Python The Hard Way》小练习，熟悉 Python3 的使用
然后完成 ch1 基础任务，获得第 1 个 MVP 程序
最后挑战 ch2 任务（其实是 ch1 成果的升级版），跟上课程节奏
如果你看到周围还有学友死磕 ch0 所有行动（比如调试各种工具），而非开始挑战 ch1 和 ch2 任务，麻烦提醒一下 Ta 哟。

### 2A

ch2 目标：通过 API 获取真实、即时的数据

本章，你将学习通过 API 获取真实、即时的数据来完善天气程序。

你的程序从本章开始，将真正成为一个可以解决你实际问题的应用啦。

你将会体验到：

如何选择一个合适的 API
使用 requests 模块来对 API 发送请求、传递参数、接受返回的数据
处理 API 返回的数据，转换为 Python 中合适的数据结构

### 2B

从这一章开始，你的程序不再只和本地的数据进行交互，而是利用互联网上公开的 API 获取数据，进行交互。

本章基础任务较简单，学有余力，你可完成进阶任务，做更多探索。如果进阶任务也折腾完毕，还可以发邮件到 course@openmindclub.com ，申请任务加码;-)

经过 2 周玩耍，相信你已体会开智翻转课堂模式的特色 —— 什么是"课"? | [Zoom.Quiet Personal Static Wiki](hhttp://wiki.zoomquiet.io/IMHO/om-what-is-ke#_1) —— 开智课程提供的教练资源、同侪氛围似一片土壤，最终长出什么来你说了算


### 3A

ch2 [课程任务介绍video](http://c.openmindclub.com/course/packs/5f2b1c80-6ee0-11e7-b904-7bda389c7ba7/cards/c3320290-8572-11e7-a304-d92161331260?page=1)


### 3B

本章基础任务：完成一个在命令行界面下天气查询程序，实现以下功能：

输入城市名，返回该城市最新的天气数据；
输入指令，获取帮助信息（一般使用 h 或 help）；
输入指令，获取历史查询信息（一般使用 history）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
提交时需包含软件使用说明书 README.md， 能令其他同学根据说明书运行程序，使用所有功能。

完成基础任务后，你可查看后面的进阶任务卡领取进阶任务，解锁更多技能 ;-)

### 4A

#### 如何使用本章卡片？

至此，你已知晓本章任务，接下来的卡片将指引你完成任务，提示你需重点思考的问题、可参考的资料及可能踩的坑。

按阳志平老师在「编程与心智」视频中提到的分类，你可以选择更适合自己的学习方式：

如果你是新新手或新手，建议你先抽 15-20
分钟快速总览本卡包剩余卡片，心中有数，再对着任务卡明确本章任务重点（可查询实时天气的程序），开始输出。
如果你是专业余同学，你可开始自主探索，完成初版代码后，再对着本卡包查漏补缺。

### 4B

每周你将收到这以下卡包，使用建议如下：

当章任务卡包：周一 11:42 前上线，介绍本章任务内容和一些完成提示。此卡包使用建议参见本卡片正面。
当章任务提点卡包：周四 11:42 前上线，详细讲解本章任务思路。如果此时你依然对本章任务没有眉目，可翻看此卡包；如果对完成任务有把握，不看也无妨。
当章任务加油卡包：下周二 19:42 前上线，点评当章典型问题、优秀实践。一定别错过哦。

### 5A

想要获取最新天气数据，当然得找相应机构调取。那如何调取？这就涉及到 API 啦。

现在各大互联网公司和机构都有对外开放的 API ，供用户完成很多有意思的事情。

你可以带着这几个问题，先去探索一下 API ：

API 是什么，解决什么问题？
API 一般接收什么输入，返回什么数据？
互联网上有哪些类型的 API ？他们为什么要把 API 开放出来？
flip buttongradient

### 5B

参考资料：

- [What is an API? - Youtube](https://www.youtube.com/watch?v=s7wmiS2mSXY)
- [Application Programming Interface - Wikipedia](http://en.wikipedia.org/wiki/Application_Program_Interface)
[- API Providers - Apigee](https://apigee.com/providers)
- [API Store](http://apistore.baidu.com/)
- [What APIs Are And Why They’re Important](http://readwrite.com/2013/09/19/api-defined/)

如果探索国外的 API 有网络不稳定的情况，别忘了科学上网。


### 6A： 选择合适的API

了解什么是 API 后，是时候选择一个顺手的天气 API 来完成本章任务啦~

弱水三千，只取一瓢。互联网上有非常多的天气 API，那如何选择一个合适的 API ？

对于本任务，建议你在选择 API 时考虑以下问题：

是否有 Python 的 demo ？
使用上有哪些限制（比如要收费）？
数据源是否可靠？
...


### 6B

教练检索了一些 API 供你选择：

[心知天气 - 天气数据 API 和BI - 冷暖自心知](http://www.thinkpage.cn/)

[Weather API- OpenWeatherMap](http://openweathermap.org/api)

[彩云天气API](http://wiki.swarma.net/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94API/v2)

### 7A

#### 使用 requests 模块发送请求

选定了 API ，你就可以通过 Python 来和 API 进行交互啦。

requests 模块是你和 API 进行交互的主要工具。这是非常优秀的第三方网络模块，需要单独安装。安装好后，请你探索：

如何在程序中引入 requests 模块？
如何使用 requests 模块发送请求？
POST 和 GET 是什么意思？如何用 requests 模块发送 POST 或者 GET 请求？

### 7B

Python 和 API 进行交互使用的是 HTTP 协议。在Python 中，有很多模块 (Python 自带的 urllib 模块以及我们这里推荐的requests模块) 可以对请求和接收的数据进行封装，通过 HTTP 协议在互联网上传输。

#### 参考资料：

- [Requests: HTTP for Humans](http://www.python-requests.org/en/master/)
- [HTTP 方法：GET 对比 POST](http://www.w3school.com.cn/tags/html_ref_httpmethods.asp)
-

### 8A

处理 API 返回的数据

给 API 发送请求后，就要考虑如何处理 API 返回的数据啦：

如何获得 API 返回的数据？
如何在 Python 中处理 JSON 数据？
JSON 的来历是什么？ 为什么绝大多数 API 都选择以 JSON 的方式传递数据？

### 8B

JSON 是一种存储和交换文本信息的语法。它支持多种编程语言，也是目前最流行的数据交换方式。

想要了解更多关于 JSON 的信息，可以参考：

- [Introducing JSON](http://www.json.org/)
- [19.2. json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [JSON Response Content](http://docs.python-requests.org/en/master/user/quickstart/#json-response-content)

嗯哼，至此，本章基础任务就完成得差不多啦。

9A

#### 进阶任务：玩转 API（选做）

如果你已完成基础任务，还可以继续探索：

- 之前只在输入城市名时查询天气，有没有可能指定时间，让程序定时查询天气？
- 选一个国内 API 和国外 API 分别进行调用，了解不同的调用姿势。更进一步，如果你来设计 API ，你会怎么设计？
- 给程序增加温度单位转换功能


9B

不同国家、不同组织对实现同样功能的天气 API 实现方式各有不同，你可以了解 3-5 个，找到你任务更优雅的方式。未来你自己设计 API 时，就容易有思路了~

参考：

- Weather API - Free Weather API JSON and XML - Developer API Weather For Website - Apixu
- Weather API- OpenWeatherMap
- Dark Sky API
- Yahoo! Weather RSS feed
- 和风天气 | 更专业的天气数据服务

### 10A-10B BGM

### 11A  

#### 彩蛋-[大妈聊如何提问](http://c.openmindclub.com/course/packs/5f2b1c80-6ee0-11e7-b904-7bda389c7ba7/cards/c3320290-8572-11e7-a304-d92161331260?page=1)
[《如何提问》具体内容可以在《如何提问》页面下查看


11B

看完编程老司机 Zoom.Quiet 聊如何提问，你有无新思考？欢迎写在教程里，叫六个月前的自己更快掌握提问要义~

此外，还可重温：

- [How To Ask Questions The Smart Wa](http://www.catb.org/~esr/faqs/smart-questions.html)y by Eric Steven Raymond
- [提问的智慧](http://wiki.woodpecker.org.cn/moin/AskForHelp)
- [如何向开源社区提问题 · Issue #545 · seajs/seajs](https://github.com/seajs/seajs/issues/545)
-[ 珠的自白: 34 如何提问?才对世界有帮助!](http://blog.zhgdg.org/2014-10/dm34-how2ask/)
