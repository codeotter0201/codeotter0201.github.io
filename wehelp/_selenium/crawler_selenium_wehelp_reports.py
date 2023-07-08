from selenium import webdriver
import time
import pandas as pd

def login(driver:webdriver.Chrome, user_email:str, user_pw:str) -> None:
    driver.get('https://wehelp.tw/user')
    view_elements = driver.find_elements(by='css selector', value='div.view')
    if len(view_elements) > 0:
        return
    else:
        mail_button = driver.find_element(by='name', value='email')
        mail_button.send_keys(user_email)
        pw_button = driver.find_element(by='name', value='password')
        pw_button.send_keys(user_pw)
        login_button = driver.find_element(by='name', value='btn')
        login_button.click()
        time.sleep(2)
        return
    
def drive_to_reports(driver:webdriver.Chrome) -> None:
    report_url = 'https://wehelp.tw/bootcamp/learning-report'
    if driver.current_url != report_url:
        driver.get(report_url)
        time.sleep(2)
    
def roll_page(driver:webdriver.Chrome) -> None:
    drive_to_reports(driver)
    loadmore_button = driver.find_element(by='id', value='loadmore')
    loadmore_button.click()
    time.sleep(2)

def download_data(driver:webdriver.Chrome) -> pd.DataFrame:
    col_names = ['name-time', 'done', 'todo', 'memo', 'likes', 'comments']
    temp = {}
    js_str = """
    var nameTimeDivs = document.getElementsByClassName(arguments[0]);
    var texts = [];
    for (var i = 0; i < nameTimeDivs.length; i++) {
        texts.push(nameTimeDivs[i].textContent);
    }
    return texts;
    """
    for col in col_names:
        name_time_texts = driver.execute_script(js_str, col) # col 將傳入 js_str 的 arguments[0]
        temp[col] = name_time_texts
    df = pd.DataFrame(temp)
    df['name'] = [i[12:] for i in df["name-time"]]
    return df

def main(driver:webdriver.Chrome, user_email:str, user_pw:str, pages:int) -> pd.DataFrame:
    login(driver, user_email, user_pw)
    for _ in range(pages):
        try:
            print(f'Downloading page {_}.')
            roll_page(driver)
        except:
            print(f'Fail to download page {_}.')
            break
    return download_data(driver)

if __name__ == '__main__':
    import sys
    # 检查是否有足够的命令行参数
    if len(sys.argv) < 3:
        print("请提供用户邮箱和密码作为命令行参数")
        sys.exit(1)

    # 从命令行参数中获取用户邮箱和密码
    user_email = sys.argv[1]
    user_pw = sys.argv[2]

    # driver = webdriver.Chrome(r"chromedriver.exe") driver放到.py同路徑目錄，不需要設定路徑
    driver = webdriver.Chrome()
    df = main(driver, user_email, user_pw, 10)
    df.to_csv(str(pd.Timestamp.now().date()) + '_wehelp_reports.csv', encoding='utf-8-sig')