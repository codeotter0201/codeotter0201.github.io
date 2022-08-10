---
title: "永豐 API 使用注意事項"
summary: "一些認真看回測後才發現搞錯的地方"
subtitle: ""
date: 2022-08-10T03:20:52+08:00
lastmod: 2022-08-10T03:20:52+08:00
draft: false
author: ""
authorLink: ""
description: ""
license: ""
images: []

tags: ["shioaji api"]
categories: ["trading"]

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

#### 下載跨日期貨合約 tick 資料的注意事項
平常用 TSE 加權指數日期當索引下載資料，會漏掉夜盤

但如果只是用`pandas.daterange`遍例所有的日期(包含假日)，則會下載到重覆的資料

---
#### 使用 api.kbars 搭配期貨合約的注意事項
永豐有近月、遠月合約，例如`TXFR1`、`TXFR2`，這兩種合約就是俗稱的連續月合約

這種連續月資料是提供下載資料使用，因為期貨合約固定時間會換，更換的之後就是不一樣的商品編號

但是永豐 API 下單時，不能使用連續月合約，必須指定想要交易的合約

如果下單時使用連續月合約`會顯示無法下單`

而下載資料時，如果使用指定合約，會下載到`合約還是遠月時的資料`，這就會影響價格的呈現，因為雖然是同一個商品，但是不是熱門月是會有價差的

---

[永豐 API](https://sinotrade.github.io/tutor/market_data/historical/)