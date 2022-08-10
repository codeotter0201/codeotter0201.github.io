---
title: "處理價格資料"
summary: 利用 pandas.resample 處理常見 tick 資料集
subtitle: ""
date: 2021-04-01T02:57:29+08:00
lastmod: 2022-08-10T17:57:29+08:00
draft: false
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

> 降頻OHLCV從`1T`到`27T`
---
### 用一些奇怪頻率的原因
因為大多數程式交易常用的頻率就那樣，尤其是`5`、`15`、`30`這些倍數時間，常常會有滑價的情況發生

所以有些策略用一點不一樣的頻率，可以稍微減輕實際交易的滑價，大部分會希望早一點點行動

台灣期貨每天開盤時間為 `08:45:00`，預想中處理完的資料第一根K應該是`09:12:00`

但實際上`pd.resample`出來的資料，如果遇到分鐘頻率無法整除 60 ，是無法對齊的，這使得每天第一根K的時間點都不太一樣

---

### resample 對齊的方式
#### label, closed 參數設定
`pandas.resample` 可以把時間序列彙整並且做相對應的運算，但使用時要注意產生出的資料標籤是如何對齊

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

根據上面，現在使用的是`label=left`，沒什麼原因，就只是覺得比較符合直覺

另外關於`closed`預設是`right`也就是資料會向最後一筆對齊，覺得說明有點困難，實際操作試試會比較有感覺

---
### 嘗試過的解法
#### 透過 resample 參數調整
- origin 設定起始時間，但只有設定起始，當資料漸漸往下還是會有偏差
- base 看不太懂，運算失敗
- offset 設定一個參數例如`5T`時間標籤會按照參數做修正，依然沒有解決無法對齊的問題

#### for loop
先自訂開盤收盤時間，然後針對整個資料集，一天一天計算...
取而代之的就是算很慢，光是算`3天`的`1T`OHLCV就要花`2.2s`

#### 使用可以整除 60 的頻率
```python
n = [i for i in range(1, 60) if 60 % i == 0]
[1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
```
這樣可以直接避免`pandas.resample`之後時間無法對齊的問題

---
### 結論
目前找不到除了 for loop 之外比較快且正確的算法，`2.2s`的延遲，感覺也違背了一開始避免滑價的初衷

收盤時間的部分，台灣期貨日盤收盤時間是`13:45`所以可以也需要可以整除45，不然就是要把收盤的最後一個index做修改
如果要用只整除 60 的頻率例如 20 要記得把`14:00:00`改為`13:45:00`

> 所以決定暫時還是先使用可以同時整除 60、45 的頻率


另外，如果是用 `4H` 這種頻率，時間標籤會是正確的，但卻會把開盤收盤之間的資料混在一起

例如`12:00:00`之後下一根`16:00:00`，其中`16:00:00`的資料包含了 12 - 16 點的所有資料，如果對於收盤價比較敏感的策略需要特別注意



---
[pandas resample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)

<!-- cost time : 2022-08-10 15 -> 18 (3hrs) -->