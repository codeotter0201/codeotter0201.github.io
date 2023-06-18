---
title: "真的有必要停損嗎"
summary: 思考為何要停損，怎樣停損才是合理的
subtitle: ""
date: 2021-01-15T02:23:50+08:00
lastmod: 2022-08-08T00:00:00+08:00

author: ""
authorLink: ""
description: ""
license: ""
images: []

tags: ["stoploss"] # trading coding database crawler strategy autotrading
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
---

> **本文預設趨勢存在，而關於趨勢是否存在，參考下方補充資料**

#### 為何停損有效果
停損就是在持有的倉位方向相反，且趨勢出現時的***應對手段***

常常看到專職交易者說，在交易時，處理的部位，常常都是停損。獲利的部位則少管它，讓獲利的單子隨著趨勢一起結束出場

如果趨勢上漲存在，自然也存在趨勢下跌

策略方向錯了，停損有利；策略方向對了，停利吃虧

這時紀律的重要性出現了，也因為人性讓紀律很有用

    * 帳面已經虧損，再多虧一點也是虧，不如賭一把看它會不會回來 (整段趨勢滿滿的虧損)
    * 帳面已經獲利，如果賺的錢不見怎麼辦？不如趁現在有賺收手 (賺不到趨勢的錢)

最後經過市場的波動洗刷後，大部分的人得到***大賠小賺***的結局 💸

所以從趨勢的角度來看，停損是有用的，避免總資金被連續且方向一致的波動掃出市場。停利也因為趨勢的存在，貿然使用停利不見得是個好決策

但是何謂趨勢？什麼情形叫做趨勢，又什麼情形不能稱作趨勢，如果分辨不出來，即使紀律操作，下場不就是紀律的爆倉？

---
#### 設計停損的方法
如何設定停損是一個問題，趨勢甚麼時候發生，其實無法很精確的判斷，能看到趨勢存在，都是事後往回看的結果

所以每一筆交易***進場之後***，進場成本就不會是個重要因素，重要的是進場之後發生了甚麼事情，如果價格已經同向發展到一定的程度，是不是可以判斷趨勢產生？

根據上面的想法，評估每一筆交易的波動，這個參考值可以拿來觀察趨勢的產生

而評估交易波動的分析方法，推薦看看`MAE&MFE` 分析法，跟趨勢搭上關係的關鍵字還有`波動叢聚`、`厚尾`...等等


#### 實際操作遇到的情形
如果是手動操作者用這套方法，應該會發現常常停損在最低點，這是由於設計的停損點，一般來說都是依照過去比較糟的的交易狀況，進而決定出的較佳停損點

只是大部分的市場波動都是隨機的，真正的趨勢其實沒有想像中的多，如果市場波動沒有太大的變化，可以簡單的推論未來的狀況

假設過去有`10`筆輸最慘的交易，平均來說`-10%`，據此停損設定`-15%`，這最後會怎麼呈現？

未來輸的交易可能是 `-10%`、`-17%`、`-12%`、`-18%`

沒有觸發停損的交易，極可能最後也是輸的，只不過可能輸得比較少一點點

停損掉的交易，事後看可能會發現只離最糟的情況差距很小，有停損和沒停損差不多，可能不要停損還有機會賺錢

如果手動操作的話，遇到這種狀況不用兩三次，大概就開始修改自己的策略停損點，或更甚者修改策略的邏輯，賺的策略改成輸的策略

    而這一切可能就只是市場隨機波動產生的正常現象而已 😂

但這不代表停損沒有用，假如市場波動開始放大，後面多出了幾筆交易，損益呈現 `-22%`、`-32%`、`-48%`，這時停損就可以避免資金受到過大的影響

---
目前為止討論的是固定的停損，實際上如果市場波動大，停損與停利的機會都會變多，為了讓策略在獲利之前活下來，適當的把停損調大是有意義的

因應調整，也要考慮到，市場波動漸漸變小，可能會出不了場，將停損隨著波動調低也可以思考的選擇，但通常不會是手動調整，而是直接使用跟波動性有相關的指標，例如`ATR`、`RSI`、`KD`、`BBand`...等等

---
#### 參考資料
[MAE MFE](https://www.youtube.com/playlist?list=PLzXn-LCCq3wr2QbmFdiD7qrko8AcwZ-zW)

[隨機波動](https://www.youtube.com/playlist?list=PLzXn-LCCq3woqDBYXroqzgssAAquvKpzA)

