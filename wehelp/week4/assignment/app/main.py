from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # 用於加密 session 的密鑰

# 假設以下的使用者資料是存在資料庫中的
users = {"test": "test"}

# 主頁
@app.route("/")
def home():
    # 檢查使用者是否已登入
    if session.get("user_login", False):
        return redirect("/member")

    return render_template(
        "index.html",
        page_name="歡迎光臨，請輸入帳號密碼"
    )

@app.route("/signin", methods=["POST"])
def signin(): 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["user_login"] = False
        session["username"] = None
        session["error_msg"] = None

        # 驗證使用者名稱和密碼
        if (not username) and (not password):
            redirect_url = "/error?message=請輸入使用者名稱與密碼"
            session['error_msg'] = "請輸入使用者名稱與密碼"
            return redirect(redirect_url)
        
        if username not in users: 
            redirect_url = "/error?message=使用者不存在或密碼錯誤"
            session['error_msg'] = "使用者不存在或密碼錯誤"
            return redirect(redirect_url) 
        
        if password != users.get(username, None):
            redirect_url = "/error?message=使用者不存在或密碼錯誤"
            session['error_msg'] = "使用者不存在或密碼錯誤"
            return redirect(redirect_url)
 
        if users.get(username, None) == password:
            session["username"] = username 
            session["user_login"] = True 
            return redirect("/member")

# 會員頁面
@app.route("/member")
def member_page():
    if session.get("user_login", False):
        name = session.get("username", None)
        ret = session.get("square_result", None)
        if name:
            return render_template(
                "index.html",
                page_name=f"歡迎光臨 {name}，這是會員頁",
                username=name,
                square_result=ret
            ) 
    elif session.get("error_msg", None): 
        em = session.pop("error_msg", None)  
        redirect_url = f"/error?message={em}"
        return redirect(redirect_url)
    else:
        return redirect("/") 

# 登入失敗
@app.route("/error")
def error_page(): 
    error_msg = request.args.get("message", None)
    if error_msg:
        return render_template(
            "index.html",
            page_name=f"無法訪問",
            error_msg=error_msg,
        )
    else:
        return redirect("/")

# 登出
@app.route("/signout") 
def signout():
    # 刪除 session
    session["user_login"] = False
    session["username"] = None
    session["square_result"] = None
    return redirect("/") 

@app.route("/square/<number>") 
def cal_square(number):

    n = int(number)
    session["square_result"] = n * n 
    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear_square_result():
    session["square_result"] = None
    return redirect("/")

if __name__ == "__main__": 
    app.run()