---
title: 利用 Shioaji subscribe 取得最新1分k價格資料
summary: ""
subtitle: ""
date: 2023-06-30T02:20:52+08:00
lastmod: 2023-06-30T02:20:52+08:00
draft: false
author: ""
authorLink: ""
description: ""
license: ""
images: []
tags: ["shioaji"]
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

## 處理即時資料有那些地方要注意

- 由於即時資料更新很快，取得即時資料最好只拿當下最需要的，例如避免取得過去1天之內的資料，如果每次都拿過多沒有必要的資料，無論是對 server 或是對 local 都是很大的負擔
- 即時資料的起點是從訂閱的當下開始，如果啟動後遇到狀況要重開，就必須回補全部的資料
- 由於1分K是1分鐘之內的所有價格統計，為了避免即時資料起點在分鐘之內，可以將前N筆資料捨棄

## 需求整理
- 要有處理 quote 的方式，收到資料後存入預先設計好的 dictionary，官網範例是 {code:quote}
- 要有回補1k區間資料的方式，這可以使用 shioaji kbar 達成
- 取得商品資料的功能，取資料時，優先找 quote 資料，如果找不到相關商品、資料不正確，就下載伺服器資料，並且重新載入 quote
	- 驗證 quote 資料正確
	- 重新載入 quote 資料
	- quote 組合成為 1K data，注意將前1分鐘資料捨棄
- 合併資料AB，頭尾相連
	- A資料的尾部與B資料的頭部必須重疊，重疊部分以A資料為優先
	- B資料的尾部要超過A資料的尾部
	- 注意kbar 是 left 還是 right
- resample kbar 透過 1k data 轉換成想要的最終資料，例如 15k