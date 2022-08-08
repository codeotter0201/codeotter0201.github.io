---
title: "Markdown 常用語法"
summary: "紀錄寫文時使用的技巧"
subtitle: ""
date: 2022-08-01T00:00:00+08:00
lastmod: 2022-08-01T00:00:00+08:00
draft: false
author: ""
authorLink: ""
description: ""
license: ""
images: []

tags: ["markdown"]
categories: ["coding"]  # trading coding database crawler strategy autotrading

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: false
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true
code:
  copy: true
  maxShownLines: 50
math:
  enable: false
  # ...
mapbox:
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
library:
  css:
    # someCSS = "some.css"
    # 位于 "assets/"
    # 或者
    # someCSS = "https://cdn.example.com/some.css"
  js:
    # someJS = "some.js"
    # 位于 "assets/"
    # 或者
    # someJS = "https://cdn.example.com/some.js"
seo:
  images: []
  # ...

---
### 超連結
[Upstage](https://github.com/upstage/ "Visit Upstage!")

---
### 提示字
[CJK]^(中文/日语/韩语)

---
### 分數顯示
[浅色]/[深色]

[88]/[99]

---
### 列表
- [ ] **test**
- [x] *test*
* test
- test

---
### 引用
> test
>> test2

---
### Code
    line 1 of code
    line 2 of code
    line 3 of code

---
### 表格
`:` 控制文字內容對齊方向，置中 `:-:`，靠右 `-:`
|test1|test2|
|:-:|-:|
|test1|test2test2test2test2|
|test1|test2test2test2test2|

---
### 圖片
![Alt text](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

---
### 註腳
这是一个数字脚注[^1].
这是一个带标签的脚注[^label]

[^1]: 这是一个数字脚注
[^label]: 这是一个带标签的脚注
