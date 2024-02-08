+++
title = "用 Zola 建立 Blog"
date = 2024-02-09
updated = 2024-02-09
description = "透過 Github Pages + Actions + Zola 建立靜態網站"

[taxonomies]

tags = ["memo", "blog", "zola"]

[extra]
quick_navigation_buttons = true
social_media_card = "social_cards/blog_toc.jpg"
+++

<details>
    <summary><b>Table of Contents</b></summary>
    <!-- toc -->
</details>

## 部署紀錄
首先我是 MacOS 環境，直接在 Zola 用 `brew install zola` 就可以迅速完成下載，接著挑個順眼的 Theme 使用 `git add submodule ...`，搭配 Github Actions + 設定 token ，最後只要推上 Github 就能完成部署上線

## 心得
原本 Blog 是用 Hugo 建立的，但當時從安裝 Hugo 、選擇主題、個人化設定、部署，每個步驟都花了大概 2 天，前前後後應該花了兩週才能夠從手機端看到自己的網站。
但這次在 Zola 的整體流程都沒有遇到太多阻礙，有可能是因為 Hugo 的部署經驗，整體只花了 1 小時不到就完成，令我蠻驚訝的。
另外還有 Zola 的 client command 只有 4 種可以使用，省了很多走錯路的可能，我想這佔了很大一部分功勞。