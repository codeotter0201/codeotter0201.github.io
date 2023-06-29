---
title: 利用 Shioaji subscribe 取得最新1分k價格資料
summary: ""
subtitle: ""
date: 2023-06-30T03:15:00+08:00
lastmod: 2023-06-30T03:15:00+08:00
draft: false
author: ""
authorLink: ""
description: ""
license: ""
images: []
tags: ["shioaji"]
categories: ["trading"]
url: 2023-06-30-trading-shioaji-subscribe-realtime-data

---
## 目標透過一個功能，就可以取得某商品最新的自定義 Kbar Data
```python
def get_kbar(code:str, freq:str, start_date:str) -> pd.DataFrame:
  pass
```

## 處理即時資料有那些地方要注意
- 由於即時資料更新很快，取得即時資料最好只拿當下最需要的，例如避免取得過去1天之內的資料，如果每次都拿過多沒有必要的資料，無論是對 server 或是對 local 都是很大的負擔
- 即時資料的起點是從訂閱的當下開始，如果啟動後遇到狀況要重開，就必須回補全部的資料
- 由於1分K是1分鐘之內的所有價格統計，為了避免即時資料起點在分鐘之內，可以將前N筆資料捨棄

## 需求整理
- 處理 quote 的方式，收到資料後存入預先設計好的 dictionary，官網範例是 {code:quote}
- 回補1k區間資料的方式，這可以使用 shioaji kbar 達成
- 取得商品資料的功能，取資料時，優先找 quote 資料，如果找不到相關商品、資料不正確，就下載伺服器資料，並且重新載入 quote
  - 驗證 quote 資料正確
  - 重新載入 quote 資料
  - quote 組合成為 1K data，注意將前1分鐘資料捨棄
- 合併資料AB，頭尾相連
  - A資料的尾部與B資料的頭部必須重疊，重疊部分以A資料為優先
  - B資料的尾部要超過A資料的尾部
  - 注意kbar 是 left 還是 right
- resample kbar 透過 1k data 轉換成想要的最終資料，例如 15k
  
### 初始化 Shioaji
```python
import shioaji as sj
api = sj.Shioaji()
api.login(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)
```

### 選擇合約
```python
contract = api.Contracts.Futures.TXF['TXFR1']
```

### 設定 Quote Callback
```python
from shioaji import BidAskFOPv1, Exchange

@api.on_tick_fop_v1(bind=True)
def quote_callback(self, exchange:Exchange, tick:TickFOPv1):
    self[tick.code].append(tick)

@api.on_bidask_fop_v1(bind=True)
def quote_callback(self, exchange:Exchange, bidask:BidAskFOPv1):
    self[bidask.code].append(bidask)
```

### 建立 class 物件執行所有需求
```python
class DataHandler:
  def __init__(self, api):
    self.api = api
    self.tick = {}
    self.bidask = {}

  def add_tick(self, tick:TickFOPv1):
    data = self.tick.get(tick.code, [])
    data[tick.code].append(tick)

  def add_bidask(self, bidask:BidAskFOPv1):
    data = self.bidask.get(bidask.code, [])
    data[bidask.code].append(bidask)

  def reload_1k_data():
    pass

  def reload_1k_data():
    pass
```