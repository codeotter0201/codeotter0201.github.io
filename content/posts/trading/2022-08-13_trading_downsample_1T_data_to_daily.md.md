---
title: "將分鐘資料集降頻為每日資料集，並保有原始分鐘的index"
summary: "使用資料：台指期 08:45 -> 13:45"
subtitle: ""
date: 2022-08-13T02:20:52+08:00
lastmod: 2022-08-13T02:20:52+08:00
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

### 原始資料

|datetime|open|high|low|close|volume|
|:-:|:-:|:-:|:-:|:-:|:-:|
|2022-07-02 04:58:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|
|2022-07-02 04:59:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|
|2022-07-02 05:00:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|

---
### 降頻語法
```python
# 先選取日盤時間
ohlcv = ohlcv.between_time('08:45', '13:45')
# 再用 index.date 進行聚合
ohlcv.groupby(ohlcv.index.date).agg({
    'open':'first',
    'high':'max',
    'low':'min',
    'close':'last',
    'volume':'sum',
}).reindex(ohlcv.index).ffill().tail()
```

#### 降頻後資料

|datetime|open|high|low|close|volume|
|:-:|:-:|:-:|:-:|:-:|:-:|
|2022-06-29	|15020	|15114	|14980	|15019	|100639|
|2022-06-30	|14931	|14945	|14610	|14622	|131969|
|2022-07-01	|14656	|14702	|14128	|14175	|183609|

--- 

### 還原 index 語法
```python
ohlcv.reindex(ohlcv.index).ffill()
```

#### 還原後資料
|datetime|open|high|low|close|volume|
|:-:|:-:|:-:|:-:|:-:|:-:|
|2022-07-02 04:58:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|
|2022-07-02 04:59:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|
|2022-07-02 05:00:00	|14656.0	|14702.0	|14128.0	|14175.0	|183609.0|

---