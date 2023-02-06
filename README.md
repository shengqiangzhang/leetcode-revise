## 相关介绍

这是一个 [LeetCode](https://leetcode.cn/problemset/all/) 题目自动统计及分析程序，可自动统计所有提交通过的题目，并以 Markdown 的形式展示。

根据个人需求，目前只考虑获取**提交次数**和**重刷次数**这两个指标，以便更好地进行刷题。

采用 GitHub Actions 进行自动化部署，无需本地服务器资源。

## 使用教程

1. 由模板项目[生成](https://github.com/shengqiangzhang/leetcode-revise/generate)自己的项目

2. 点击生成项目下的 Settings -> Secrets -> Actions -> New repository secret，分别添加以下 Secrets：
    - Name：`LEETCODE_EMAIL`
        - Secret：你的LeetCode账号
    - Name：`LEETCODE_PASSWORD`
        - Secret：你的LeetCode密码

3. 回到项目首页并进入 Actions，点击绿色按钮 `I understand my workflows, go ahead and enable them`，在左侧点击`Github LeetCode Bot`，再点击黄色提示框中的 `Enable workflow`，接着再点击蓝色提示框中的 `Run workflow` 即可

## 补充说明

默认配置为每12小时更新一次，可根据需求修改 [action.yml](.github/workflows/action.yml#L9) 文件的第 `9` 行。如有其他需求，欢迎提交PR。

> 重刷次数的计算规则为：累计所有提交通过且互为不同一天的记录次数

## 数据统计

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
