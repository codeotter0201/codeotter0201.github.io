## 2023-07-10
- 函式最後的地方加上 ; 代表某一行的結束

- 查string含有某片段用 .includes

- for 迴圈對字典使用，會先取出 key

- string.replace 可以使用正則表達式(待複習)，或是 /word/

- 在js裡面 "100" * 30 雖然是字串*30，但會自動轉換，實際撰寫應該還是要在程式內轉換成想要的型態，增加可讀性與穩健性

- Math有常見的運算函數例如選出最小值 Math.min

- 在函數input部分，javascript ...array == python *list

- array.forEach(func(input){}) 可以快速對array迴圈

- array 新增值用 array.push()

- var || var2 代表如果 var 為 False 那就填入 var2

- js相較於python少了// 所以如果要求商數例如 5 // 3 要用 Math.floor(5 / 3)

## 2023-07-11
### 額外議題
> 如果第一題我們想滿足 XX years old 這樣的字串形式，找出 XX 是多少，並判斷這個 XX 是否大於 17，這樣比較精緻的規則，你會怎麼寫程式？
* 原先的 `find_and_print` 有幾項工作要做:
    1. 取出 messages 的 kay, value
    2. 設計 judgment rule
    3. 執行 judgment rule
    4. print 結果

* 如果會使用較精細的 pattern, judgment rule 的設計會變得比較複雜，函數程式行數也會增加
* 考慮未來可能的維護、擴充或測試，再另外寫一個 function 例如 `check_sentence_age`，未來任何動作，就可以都從這個 function 下手修改
* 拆開之後，`find_and_print` 基本上不會改太多，只是會在內部 call `check_sentence_age`
* `check_sentence_age` 的寫法有幾點可以考慮
    1. 關鍵字判斷，如果 sentence 有出現某些 keyword 例如 ['vote', 'legal age'] 直接判斷 True
    2. 正則表達式判斷 (python)
        * 判斷有無數字
        * 判斷數字後是否有關於年齡的文字
        * 取出年齡數字並且轉換為 int
        * 判斷年齡是否大於 n

```python
import re
def extract_age(sentence:str, minimum_age:int=17) -> bool:
    pattern = r"\b(\d{1,2})\s?(?:years old)\b"
    match = re.search(pattern, sentence)
    if match:
        age = int(match.group(1))
        return age >= minimum_age
    else:
        return False
```