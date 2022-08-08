---
title: "處理價格資料"
summary: 利用 pandas.resample 處理常見 tick 資料集
subtitle: ""
date: 2021-04-01T02:57:29+08:00
lastmod: 2021-04-01T02:57:29+08:00
draft: true
author: ""
authorLink: ""
description: ""
license: ""
images: []

tags: ["data processing", "pandas"]
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
### 遇到的問題
`pandas.resample` 可以把時間序列彙整並且做相對應的運算，使用時要注意產生出的資料標籤是如何對齊。

例如台指期貨開盤時間為 `08:45`，如果使用 `label='right'` 那第一筆資料會這樣產生
```shell
2022-08-03 08:45:00 15000                           # (08:45 -> 08:50)的資料 #
2022-08-03 08:50:00 15100                           # (08:50 -> 08:55)的資料 #
```
如果使用 `label='left'` 那第一筆資料會這樣產生
```shell
2022-08-03 08:50:00 15000                           # (08:45 -> 08:50)的資料 #
2022-08-03 08:55:00 15100                           # (08:50 -> 08:55)的資料 #
```