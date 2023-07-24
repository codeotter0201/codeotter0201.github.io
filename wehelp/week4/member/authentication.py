from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # 用於加密 session 的密鑰

# 假設以下的使用者資料是存在資料庫中的
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"},
    {"username": "test", "password": "test"},
]

@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # 驗證使用者名稱和密碼
        for user in users:
            if user["username"] == username and user["password"] == password:
                # 設置 session
                session["username"] = username
                return redirect("/")
        
        # 登入失敗
        return "Invalid username or password"
    
    # return render_template(
    #     "index.html", 
    #     content=f'歡迎 {username}', 
    #     page_name="歡迎光臨，請輸入帳號密碼"
    # )

# 登出
@app.route("/logout")
def logout():
    # 刪除 session
    session.pop("username", None)
    return redirect("/login")

# 保護的內容
@app.route("/")
def home():
    # 檢查使用者是否已登入
    print(session)
    if "username" in session:
        n = session["username"]
        return render_template(
            "index.html", 
            user_login=True, 
            page_name=f"{n} 歡迎光臨，這是會員頁"
        )

    # return redirect("/login")
    return render_template(
        "index.html",
        content='歡迎',
        page_name="歡迎光臨，請輸入帳號密碼"
    )

if __name__ == "__main__":
    app.run()
