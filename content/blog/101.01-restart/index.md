+++
title = "使用 Zola 建立 Blog"
date = 2024-02-09
updated = 2024-02-09
description = "透過 Github Pages + Actions + Zola 建立靜態網站"

[taxonomies]

tags = ["memo", "blog", "zola"]

[extra]
quick_navigation_buttons = true
footnote_backlinks = true 
social_media_card = "social_cards/blog_toc.jpg"
+++
<details>
    <summary><b>Table of Contents</b></summary>
    <!-- toc -->
</details>

---

## 部署過程
### Zola install
基本上 Zola 官方文件已經非常容易使用，這邊介紹 MacOS 的步驟。

我使用的是 [brew](https://brew.sh/) 來安裝指令如下：
```bash
brew install zola
```

### Zola init
完成下載後初始化 zola 專案
```bash
zola init blog
```

### Install theme
接著挑個順眼的 Theme 套用，我選擇的主題是 [Tabi](https://github.com/welpo/tabi) ，安裝方法建議使用 `git add submodule`[^1]
```bash
git submodule add https://github.com/welpo/tabi.git themes/tabi
```

### First post
參考 [Tabi](https://github.com/welpo/tabi) 在 `content` 建立 `_index.md`後，就可以撰寫第一篇文章

以本主題為例，我需要建立 `/blog/{your_post_title}/index.md`

都準備好了之後就可以在嘗試本地運作看有沒有效果
```bash
zola serve
```

### Deploy
#### Github Pages 
網路上已經有很多分享，推薦用 `github pages` 當作關鍵字搜尋一下教學，就不在這展開。

主要步驟有這些：
- 新增一個 repository 命名需符合 `github pages` 規則
- 設定 repo token 提供給 `github actions` 設定檔案使用


#### Github Actions
主要步驟有這些：
- 在 zola 專案裡面建立 workflows ，路徑像是這樣 `/blog/.github/workflows/{your_action_file}.yml`
- 設定檔的寫法可以直接參考 [Zola Deploy](https://www.getzola.org/documentation/deployment/github-pages/)，這邊要注意官方提供的的設定檔需要注意版本[^2]

#### Push
最後就是最簡單的 git 組合技推上 Github 完成部署上線
```bash
git add .
git commit -m "zola init"
git push origin master
```
---

## 心得
原本 Blog 是用 Hugo 建立的，但當時從安裝 Hugo 、選擇主題、個人化設定、部署，每個步驟都花了大概 2 天，前前後後應該花了兩週才能夠從手機端看到自己的網站。

也許是因為 Zola 的 client command 只有 4 種可以使用，省了很多走錯路的可能。

這次改用 Zola 架設的整體流程都沒有遇到太多阻礙，有可能是因為有先前 Hugo 的部署經驗，整體只花了 1 小時不到就完成，令我蠻驚訝的😆

---

[^1]: Zola 官方文件提供的 github actions 設定部署時會檢查 submodle ，如果用 `git clone` 會部署失敗

[^2]: 官方提供的設定版本為 `uses: shalzz/zola-deploy-action@v0.17.2` 這在我使用的主題會失敗，檢查本地環境後將版本部分改為 `@v0.18.0` 成功順利部署