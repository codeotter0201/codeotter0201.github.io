---
title: "停損"
summary: 停損的意義與方法
subtitle: ""
date: 2021-01-15T02:23:50+08:00
lastmod: 2021-01-15T02:23:50+08:00
draft: false
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

**本篇文章預設趨勢存在，而關於趨勢是否存在的資料，放在參考資料補充。**

#### 為何停損有效果
停損就是在持有的倉位方向相反，且趨勢出現時的應對手段。

常常看到專職交易者說，在交易時，處理的部位，常常都是停損。獲利的部位則少管它，讓獲利的單子隨著趨勢一起結束出場。

如果趨勢上漲存在，自然也存在趨勢下跌，策略方向錯了，停損有利；策略方向對了，停利吃虧。

這時紀律的重要性出現了，因為人性讓紀律很有用。

帳面已經虧損，再多虧一點也是虧，不如賭一把看它會不會回來。

帳面已經獲利，如果賺的錢不見怎麼辦？不如趁現在有賺收手。

最後經過市場的波動洗刷後，大部分的人得到大賠小賺的結局。

所以從趨勢的角度來看，停損是有用的，避免總資金被連續且方向一致的波動掃出市場。停利也因為趨勢的存在，貿然使用停利不見得是個好決策。

但是何謂趨勢呢？什麼情形叫做趨勢，又什麼情形不能稱作趨勢，如果分辨不出來，即使紀律操作，下場不就是紀律的爆倉嗎？

---
#### 停損策略
趨勢甚麼時候發生，其實無法很精確的判斷，能看到趨勢產生，都是事後往回看的結果。

所以每一筆進場後的交易，何時進場不是很重要，重要的是進場之後發生了甚麼事情，如果價格已經同向發展到一定的程度，是不是可以判斷趨勢產生？

根據上面的想法，評估每一筆交易的波動，這個參考值可以拿來觀察趨勢的產生。而評估交易的波動方法，推薦看看`MAE MFE` 分析法。

如果是手動操作者用這套方法，應該會常常發現自己停損在最低點，因為會根據過去的交易情形，決定最佳停損出場的位置。

市場波動如果漸漸變小，可能會出不了場，這時要利用停利，但如果市場波動漸漸的放大，這時停損的策略就要思考如何利用波動。

---
#### 參考資料
[MAE MFE](https://www.youtube.com/playlist?list=PLzXn-LCCq3wr2QbmFdiD7qrko8AcwZ-zW)
[隨機波動](https://www.youtube.com/playlist?list=PLzXn-LCCq3woqDBYXroqzgssAAquvKpzA)

