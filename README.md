## 部署步骤
1. Fork本仓库
2. 配置GitHub Actions所需的参数
    - 点击仓库下的Settings->Secrets->New repository secret, 分别添加以下secret
        - Name:LEETCODE_EMAIL  Value:你的LeetCode账号
        - Name:LEETCODE_PASSWORD  Value:你的LeetCode密码
    - 点击[tokens](https://github.com/settings/tokens)->Generate new token
        - Note:GITHUB_TOKEN
        - Select scopes:建议全部勾选

> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2021-02-06 17:52 | [#剑指 Offer 19 正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof) | HARD | 3 | 1 |
| 2021-02-06 14:56 | [#剑指 Offer 43 1～n 整数中 1 出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof) | HARD | 3 | 1 |
| 2021-02-06 14:03 | [#剑指 Offer 51 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof) | HARD | 2 | 1 |
| 2021-02-05 10:45 | [#剑指 Offer 67 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof) | MEDIUM | 4 | 1 |
| 2021-02-05 09:51 | [#剑指 Offer 48 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof) | MEDIUM | 7 | 1 |
| 2021-01-14 16:51 | [#剑指 Offer 44 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof) | MEDIUM | 3 | 1 |
| 2021-01-02 17:55 | [#剑指 Offer 12 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof) | MEDIUM | 17 | 1 |
| 2021-01-02 13:54 | [#89 格雷编码](https://leetcode-cn.com/problems/gray-code) | MEDIUM | 1 | 1 |
| 2020-12-31 18:19 | [#236 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree) | MEDIUM | 1 | 1 |
| 2020-12-31 06:34 | [#16 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest) | MEDIUM | 4 | 1 |
| 2020-12-31 05:39 | [#61 旋转链表](https://leetcode-cn.com/problems/rotate-list) | MEDIUM | 2 | 1 |
| 2020-12-24 19:13 | [#399 除法求值](https://leetcode-cn.com/problems/evaluate-division) | MEDIUM | 4 | 1 |
| 2020-12-23 18:07 | [#59 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii) | MEDIUM | 5 | 1 |
| 2020-12-23 17:54 | [#39 组合总和](https://leetcode-cn.com/problems/combination-sum) | MEDIUM | 6 | 1 |
| 2020-12-23 17:34 | [#54 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix) | MEDIUM | 1 | 1 |
| 2020-12-22 18:29 | [#251 展开二维向量](https://leetcode-cn.com/problems/flatten-2d-vector) | MEDIUM | 5 | 1 |
| 2020-12-21 18:15 | [#48 旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 1 | 1 |
| 2020-12-21 17:27 | [#238 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | MEDIUM | 1 | 1 |
| 2020-12-20 15:21 | [#22 括号生成](https://leetcode-cn.com/problems/generate-parentheses) | MEDIUM | 5 | 1 |
| 2020-12-20 14:19 | [#348 判定井字棋胜负](https://leetcode-cn.com/problems/design-tic-tac-toe) | MEDIUM | 7 | 1 |
| 2020-12-20 09:28 | [#277 搜寻名人](https://leetcode-cn.com/problems/find-the-celebrity) | MEDIUM | 2 | 1 |
| 2020-12-20 08:16 | [#163 缺失的区间](https://leetcode-cn.com/problems/missing-ranges) | EASY | 2 | 1 |
| 2020-12-20 07:56 | [#285 二叉搜索树中的顺序后继](https://leetcode-cn.com/problems/inorder-successor-in-bst) | MEDIUM | 11 | 1 |
| 2020-12-19 19:13 | [#324 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii) | MEDIUM | 5 | 1 |
| 2020-12-15 18:38 | [#454 四数相加 II](https://leetcode-cn.com/problems/4sum-ii) | MEDIUM | 2 | 1 |
| 2020-12-15 18:26 | [#18 四数之和](https://leetcode-cn.com/problems/4sum) | MEDIUM | 6 | **2** |
| 2020-12-15 17:59 | [#15 三数之和](https://leetcode-cn.com/problems/3sum) | MEDIUM | 6 | **2** |
| 2020-12-14 16:58 | [#334 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence) | MEDIUM | 6 | 1 |
| 2020-12-13 18:06 | [#380 常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) | MEDIUM | 4 | 1 |
| 2020-12-12 18:17 | [#227 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii) | MEDIUM | 14 | 1 |
| 2020-12-12 14:43 | [#130 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions) | MEDIUM | 5 | 1 |
| 2020-12-12 13:44 | [#200 岛屿数量](https://leetcode-cn.com/problems/number-of-islands) | MEDIUM | 19 | **3** |
| 2020-12-12 11:50 | [#150 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | MEDIUM | 2 | 1 |
| 2020-12-12 09:39 | [#240 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii) | MEDIUM | 1 | 1 |
| 2020-12-12 09:11 | [#73 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | MEDIUM | 5 | 1 |
| 2020-12-11 19:44 | [#152 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | MEDIUM | 5 | 1 |
| 2020-12-10 18:09 | [#210 课程表 II](https://leetcode-cn.com/problems/course-schedule-ii) | MEDIUM | 2 | 1 |
| 2020-12-10 17:44 | [#207 课程表](https://leetcode-cn.com/problems/course-schedule) | MEDIUM | 2 | 1 |
| 2020-12-09 18:26 | [#36 有效的数独](https://leetcode-cn.com/problems/valid-sudoku) | MEDIUM | 2 | 1 |
| 2020-12-09 17:59 | [#395 至少有K个重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters) | MEDIUM | 9 | 1 |
| 2020-12-08 17:48 | [#34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | MEDIUM | 4 | 1 |
| 2020-12-07 18:35 | [#300 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | MEDIUM | 8 | 1 |
| 2020-12-06 16:06 | [#378 有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) | MEDIUM | 2 | 1 |
| 2020-12-06 13:53 | [#131 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning) | MEDIUM | 1 | 1 |
| 2020-12-06 13:28 | [#91 解码方法](https://leetcode-cn.com/problems/decode-ways) | MEDIUM | 15 | 1 |
| 2020-12-06 09:20 | [#162 寻找峰值](https://leetcode-cn.com/problems/find-peak-element) | MEDIUM | 6 | 1 |
| 2020-12-05 18:57 | [#33 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array) | MEDIUM | 7 | 1 |
| 2020-12-05 17:47 | [#166 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal) | MEDIUM | 2 | 1 |
| 2020-12-05 14:55 | [#322 零钱兑换](https://leetcode-cn.com/problems/coin-change) | MEDIUM | 6 | 1 |
| 2020-12-05 13:35 | [#127 单词接龙](https://leetcode-cn.com/problems/word-ladder) | HARD | 3 | 1 |
| 2020-12-05 08:54 | [#134 加油站](https://leetcode-cn.com/problems/gas-station) | MEDIUM | 6 | **2** |
| 2020-11-30 18:01 | [#560 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k) | MEDIUM | 3 | **3** |
| 2020-11-30 13:39 | [#494 目标和](https://leetcode-cn.com/problems/target-sum) | MEDIUM | 11 | 1 |
| 2020-11-26 13:16 | [#241 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses) | MEDIUM | 3 | 1 |
| 2020-11-25 17:21 | [#55 跳跃游戏](https://leetcode-cn.com/problems/jump-game) | MEDIUM | 12 | 1 |
| 2020-11-23 06:11 | [#56 合并区间](https://leetcode-cn.com/problems/merge-intervals) | MEDIUM | 6 | **2** |
| 2020-11-22 17:26 | [#416 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | MEDIUM | 4 | 1 |
| 2020-11-22 09:50 | [#31 下一个排列](https://leetcode-cn.com/problems/next-permutation) | MEDIUM | 4 | 1 |
| 2020-11-21 18:42 | [#1658 将 x 减到 0 的最小操作数](https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero) | MEDIUM | 27 | 1 |
| 2020-11-21 18:12 | [#621 任务调度器](https://leetcode-cn.com/problems/task-scheduler) | MEDIUM | 6 | **2** |
| 2020-11-15 03:31 | [#1657 确定两个字符串是否接近](https://leetcode-cn.com/problems/determine-if-two-strings-are-close) | MEDIUM | 2 | 1 |
| 2020-11-15 03:00 | [#1656 设计有序流](https://leetcode-cn.com/problems/design-an-ordered-stream) | EASY | 3 | 1 |
| 2020-11-14 14:46 | [#1652 拆炸弹](https://leetcode-cn.com/problems/defuse-the-bomb) | EASY | 1 | 1 |
| 2020-11-14 07:30 | [#384 打乱数组](https://leetcode-cn.com/problems/shuffle-an-array) | MEDIUM | 2 | 1 |
| 2020-11-12 16:25 | [#628 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | EASY | 5 | 1 |
| 2020-11-06 14:15 | [#438 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string) | MEDIUM | 2 | 1 |
| 2020-11-06 09:22 | [#19 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) | MEDIUM | 3 | 1 |
| 2020-11-06 08:36 | [#17 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) | MEDIUM | 3 | 1 |
| 2020-11-01 04:35 | [#1641 统计字典序元音字符串的数目](https://leetcode-cn.com/problems/count-sorted-vowel-strings) | MEDIUM | 7 | 1 |
| 2020-11-01 02:51 | [#1640 能否连接形成数组](https://leetcode-cn.com/problems/check-array-formation-through-concatenation) | EASY | 1 | 1 |
| 2020-10-31 16:09 | [#1637 两点之间不包含任何点的最宽垂直面积](https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points) | MEDIUM | 7 | 1 |
| 2020-10-31 15:30 | [#1638 统计只差一个字符的子串数目](https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character) | MEDIUM | 3 | 1 |
| 2020-10-29 18:21 | [#253 会议室 II](https://leetcode-cn.com/problems/meeting-rooms-ii) | MEDIUM | 2 | 1 |
| 2020-10-29 13:45 | [#129 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 1 | 1 |
| 2020-10-28 18:22 | [#252 会议室](https://leetcode-cn.com/problems/meeting-rooms) | EASY | 6 | 1 |
| 2020-10-25 18:31 | [#148 排序链表](https://leetcode-cn.com/problems/sort-list) | MEDIUM | 2 | 1 |
| 2020-10-25 08:41 | [#50 Pow(x, n)](https://leetcode-cn.com/problems/powx-n) | MEDIUM | 4 | 1 |
| 2020-10-24 17:42 | [#221 最大正方形](https://leetcode-cn.com/problems/maximal-square) | MEDIUM | 3 | 1 |
| 2020-10-24 15:05 | [#121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 6 | **2** |
| 2020-10-24 11:36 | [#714 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | MEDIUM | 2 | 1 |
| 2020-10-24 10:57 | [#309 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | MEDIUM | 2 | 1 |
| 2020-10-24 08:23 | [#122 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) | EASY | 3 | 1 |
| 2020-10-23 17:21 | [#394 字符串解码](https://leetcode-cn.com/problems/decode-string) | MEDIUM | 5 | **2** |
| 2020-10-19 12:25 | [#3 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | MEDIUM | 8 | **2** |
| 2020-10-18 02:41 | [#1624 两个相同字符之间的最长子字符串](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters) | EASY | 2 | 1 |
| 2020-10-17 15:45 | [#1620 网络信号最好的坐标](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality) | MEDIUM | 5 | 1 |
| 2020-10-17 14:51 | [#1619 删除某些元素后的数组均值](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements) | EASY | 2 | 1 |
| 2020-10-17 04:00 | [#98 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | MEDIUM | 18 | **3** |
| 2020-10-15 17:16 | [#977 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array) | EASY | 4 | 1 |
| 2020-10-15 14:58 | [#410 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum) | HARD | 4 | 1 |
| 2020-10-14 18:30 | [#341 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator) | MEDIUM | 4 | 1 |
| 2020-10-12 06:45 | [#289 生命游戏](https://leetcode-cn.com/problems/game-of-life) | MEDIUM | 3 | **2** |
| 2020-10-11 14:28 | [#279 完全平方数](https://leetcode-cn.com/problems/perfect-squares) | MEDIUM | 11 | 1 |
| 2020-10-11 12:19 | [#79 单词搜索](https://leetcode-cn.com/problems/word-search) | MEDIUM | 1 | 1 |
| 2020-10-11 09:17 | [#337 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii) | MEDIUM | 7 | 1 |
| 2020-10-11 08:15 | [#213 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii) | MEDIUM | 4 | 1 |
| 2020-10-11 07:41 | [#198 打家劫舍](https://leetcode-cn.com/problems/house-robber) | MEDIUM | 6 | **2** |
| 2020-10-10 16:47 | [#139 单词拆分](https://leetcode-cn.com/problems/word-break) | MEDIUM | 16 | 1 |
| 2020-10-10 08:54 | [#49 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams) | MEDIUM | 6 | 1 |
| 2020-10-09 17:48 | [#437 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii) | MEDIUM | 1 | 1 |
| 2020-10-09 17:07 | [#62 不同路径](https://leetcode-cn.com/problems/unique-paths) | MEDIUM | 2 | 1 |
| 2020-10-09 15:46 | [#面试题 01.07 旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci) | MEDIUM | 2 | **2** |
| 2020-10-08 19:22 | [#230 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) | MEDIUM | 3 | 1 |
| 2020-10-08 18:32 | [#8 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | MEDIUM | 4 | 1 |
| 2020-10-08 09:45 | [#344 反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 8 | **3** |
| 2020-10-08 09:36 | [#5 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring) | MEDIUM | 2 | 1 |
| 2020-10-08 09:25 | [#647 回文子串](https://leetcode-cn.com/problems/palindromic-substrings) | MEDIUM | 7 | 1 |
| 2020-10-07 17:37 | [#11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 2 | 1 |
| 2020-10-07 14:48 | [#739 每日温度](https://leetcode-cn.com/problems/daily-temperatures) | MEDIUM | 9 | 1 |
| 2020-10-07 13:28 | [#75 颜色分类](https://leetcode-cn.com/problems/sort-colors) | MEDIUM | 10 | 1 |
| 2020-10-07 09:26 | [#287 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number) | MEDIUM | 3 | 1 |
| 2020-10-07 07:48 | [#64 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum) | MEDIUM | 2 | 1 |
| 2020-10-06 18:08 | [#96 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees) | MEDIUM | 1 | 1 |
| 2020-10-06 04:49 | [#406 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height) | MEDIUM | 5 | **2** |
| 2020-10-03 17:01 | [#1604 警告一小时内使用相同员工卡大于等于三次的人](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period) | MEDIUM | 11 | 1 |
| 2020-10-03 15:17 | [#1603 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 1 | 1 |
| 2020-09-30 05:40 | [#46 全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 3 | 1 |
| 2020-09-28 18:03 | [#114 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list) | MEDIUM | 10 | 1 |
| 2020-09-28 17:06 | [#117 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii) | MEDIUM | 4 | 1 |
| 2020-09-28 11:23 | [#90 子集 II](https://leetcode-cn.com/problems/subsets-ii) | MEDIUM | 3 | 1 |
| 2020-09-27 18:13 | [#78 子集](https://leetcode-cn.com/problems/subsets) | MEDIUM | 5 | 1 |
| 2020-09-27 10:31 | [#235 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree) | EASY | 3 | 1 |
| 2020-09-27 04:09 | [#1599 经营摩天轮的最大利润](https://leetcode-cn.com/problems/maximum-profit-of-operating-a-centennial-wheel) | MEDIUM | 7 | 1 |
| 2020-09-27 02:48 | [#1598 文件夹操作日志搜集器](https://leetcode-cn.com/problems/crawler-log-folder) | EASY | 2 | 1 |
| 2020-09-26 18:44 | [#1265 逆序打印不可变链表](https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse) | MEDIUM | 2 | 1 |
| 2020-09-26 18:32 | [#278 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | EASY | 7 | 1 |
| 2020-09-26 17:59 | [#面试题 16.02 单词频率](https://leetcode-cn.com/problems/words-frequency-lcci) | MEDIUM | 5 | **2** |
| 2020-09-26 17:35 | [#208 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree) | MEDIUM | 1 | 1 |
| 2020-09-26 12:39 | [#113 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii) | MEDIUM | 4 | 1 |
| 2020-09-25 17:28 | [#43 字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | MEDIUM | 4 | 1 |
| 2020-09-23 18:29 | [#103 二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal) | MEDIUM | 2 | 1 |
| 2020-09-23 18:02 | [#328 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list) | MEDIUM | 5 | 1 |
| 2020-09-23 11:19 | [#338 比特位计数](https://leetcode-cn.com/problems/counting-bits) | MEDIUM | 4 | **2** |
| 2020-09-21 07:43 | [#面试题 16.14 最佳直线](https://leetcode-cn.com/problems/best-line-lcci) | MEDIUM | 13 | 1 |
| 2020-09-20 18:08 | [#面试题 08.04 幂集](https://leetcode-cn.com/problems/power-set-lcci) | MEDIUM | 6 | 1 |
| 2020-09-20 06:37 | [#LCP 22 黑白方格画](https://leetcode-cn.com/problems/ccw6C7) | EASY | 4 | **2** |
| 2020-09-19 17:16 | [#1411 给 N x 3 网格图涂色的方案数](https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid) | HARD | 5 | 1 |
| 2020-09-19 14:39 | [#面试题 02.04 分割链表](https://leetcode-cn.com/problems/partition-list-lcci) | MEDIUM | 4 | 1 |
| 2020-09-18 13:04 | [#面试题 10.03 搜索旋转数组](https://leetcode-cn.com/problems/search-rotate-array-lcci) | MEDIUM | 2 | 1 |
| 2020-09-18 07:57 | [#面试题 08.09 括号](https://leetcode-cn.com/problems/bracket-lcci) | MEDIUM | 2 | 1 |
| 2020-09-16 17:45 | [#面试题 16.11 跳水板](https://leetcode-cn.com/problems/diving-board-lcci) | EASY | 5 | 1 |
| 2020-09-16 17:19 | [#面试题 03.04 化栈为队](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci) | EASY | 2 | 1 |
| 2020-09-16 17:04 | [#面试题 17.16 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | EASY | 4 | 1 |
| 2020-09-15 03:22 | [#面试题 16.17 连续数列](https://leetcode-cn.com/problems/contiguous-sequence-lcci) | EASY | 3 | 1 |
| 2020-09-14 12:02 | [#面试题 02.05 链表求和](https://leetcode-cn.com/problems/sum-lists-lcci) | MEDIUM | 2 | 1 |
| 2020-09-13 16:53 | [#面试题 01.09 字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci) | EASY | 1 | 1 |
| 2020-09-13 16:33 | [#面试题 16.05 阶乘尾数](https://leetcode-cn.com/problems/factorial-zeros-lcci) | EASY | 1 | 1 |
| 2020-09-11 18:31 | [#面试题 16.07 最大数值](https://leetcode-cn.com/problems/maximum-lcci) | EASY | 12 | 1 |
| 2020-09-11 06:29 | [#面试题 03.02 栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci) | EASY | 2 | 1 |
| 2020-09-11 06:17 | [#面试题 01.01 判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci) | EASY | 6 | 1 |
| 2020-09-11 05:28 | [#347 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements) | MEDIUM | 1 | 1 |
| 2020-09-11 04:57 | [#703 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | EASY | 9 | **2** |
| 2020-09-10 11:40 | [#179 最大数](https://leetcode-cn.com/problems/largest-number) | MEDIUM | 2 | 1 |
| 2020-09-08 16:42 | [#215 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | MEDIUM | 5 | 1 |
| 2020-09-06 17:35 | [#2 两数相加](https://leetcode-cn.com/problems/add-two-numbers) | MEDIUM | 5 | 1 |
| 2020-09-06 17:01 | [#146 LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache) | MEDIUM | 3 | 1 |
| 2020-09-05 18:40 | [#107 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | EASY | 8 | **2** |
| 2020-09-04 17:28 | [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 2 | 1 |
| 2020-09-04 17:19 | [#415 字符串相加](https://leetcode-cn.com/problems/add-strings) | EASY | 5 | 1 |
| 2020-09-04 16:18 | [#剑指 Offer 26 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof) | MEDIUM | 11 | 1 |
| 2020-09-03 17:23 | [#剑指 Offer 37 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof) | HARD | 1 | 1 |
| 2020-09-02 17:35 | [#剑指 Offer 34 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof) | MEDIUM | 1 | 1 |
| 2020-09-02 06:03 | [#409 最长回文串](https://leetcode-cn.com/problems/longest-palindrome) | EASY | 8 | 1 |
| 2020-09-01 17:47 | [#剑指 Offer 45 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof) | MEDIUM | 1 | 1 |
| 2020-09-01 17:08 | [#剑指 Offer 41 数据流中的中位数](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof) | HARD | 12 | **2** |
| 2020-08-31 15:52 | [#剑指 Offer 31 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof) | MEDIUM | 16 | 1 |
| 2020-08-31 13:19 | [#剑指 Offer 63 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof) | MEDIUM | 1 | 1 |
| 2020-08-31 12:24 | [#1013 将数组分成和相等的三个部分](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum) | EASY | 6 | 1 |
| 2020-08-30 17:15 | [#剑指 Offer 49 丑数](https://leetcode-cn.com/problems/chou-shu-lcof) | MEDIUM | 1 | 1 |
| 2020-08-30 16:30 | [#剑指 Offer 36 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof) | MEDIUM | 2 | 1 |
| 2020-08-29 17:41 | [#剑指 Offer 47 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof) | MEDIUM | 3 | 1 |
| 2020-08-29 16:54 | [#剑指 Offer 32 - I 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof) | MEDIUM | 2 | **2** |
| 2020-08-28 17:26 | [#剑指 Offer 56 - II 数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof) | MEDIUM | 2 | 1 |
| 2020-08-28 16:53 | [#剑指 Offer 46 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof) | MEDIUM | 5 | 1 |
| 2020-08-26 17:51 | [#剑指 Offer 14- II 剪绳子 II](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof) | MEDIUM | 6 | 1 |
| 2020-08-26 15:49 | [#剑指 Offer 14- I 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof) | MEDIUM | 3 | 1 |
| 2020-08-24 16:08 | [#剑指 Offer 13 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof) | MEDIUM | 4 | 1 |
| 2020-08-24 14:26 | [#680 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii) | EASY | 4 | 1 |
| 2020-08-22 18:20 | [#面试题 01.06 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | EASY | 10 | **2** |
| 2020-08-19 14:59 | [#剑指 Offer 35 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof) | MEDIUM | 12 | 1 |
| 2020-08-19 09:06 | [#剑指 Offer 38 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof) | MEDIUM | 2 | 1 |
| 2020-08-18 14:16 | [#面试题 10.01 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci) | EASY | 11 | 1 |
| 2020-08-18 13:02 | [#892 三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes) | EASY | 3 | 1 |
| 2020-08-18 10:15 | [#1071 字符串的最大公因子](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings) | EASY | 1 | 1 |
| 2020-08-18 08:30 | [#836 矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap) | EASY | 1 | 1 |
| 2020-08-17 17:11 | [#1114 按序打印](https://leetcode-cn.com/problems/print-in-order) | EASY | 2 | 1 |
| 2020-08-17 16:54 | [#剑指 Offer 56 - I 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof) | MEDIUM | 1 | 1 |
| 2020-08-17 16:04 | [#剑指 Offer 59 - II 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof) | MEDIUM | 4 | 1 |
| 2020-08-17 15:22 | [#剑指 Offer 33 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof) | MEDIUM | 8 | 1 |
| 2020-08-17 10:41 | [#剑指 Offer 32 - III 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof) | MEDIUM | 2 | 1 |
| 2020-08-17 10:06 | [#剑指 Offer 16 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof) | MEDIUM | 4 | 1 |
| 2020-08-17 07:33 | [#剑指 Offer 07 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof) | MEDIUM | 1 | 1 |
| 2020-08-16 19:26 | [#剑指 Offer 64 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof) | MEDIUM | 4 | 1 |
| 2020-08-16 18:24 | [#剑指 Offer 62 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | EASY | 2 | 1 |
| 2020-08-16 17:24 | [#剑指 Offer 57 - II 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) | EASY | 5 | 1 |
| 2020-08-16 13:17 | [#剑指 Offer 60 n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof) | MEDIUM | 3 | 1 |
| 2020-08-15 16:21 | [#剑指 Offer 59 - I 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof) | EASY | 3 | 1 |
| 2020-08-14 19:28 | [#剑指 Offer 58 - II 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof) | EASY | 8 | **2** |
| 2020-08-14 19:27 | [#面试题 17.01 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci) | EASY | 6 | 1 |
| 2020-08-14 18:03 | [#557 反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) | EASY | 15 | **2** |
| 2020-08-14 17:44 | [#剑指 Offer 66 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof) | MEDIUM | 1 | 1 |
| 2020-08-14 15:53 | [#剑指 Offer 65 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof) | EASY | 5 | 1 |
| 2020-08-14 15:20 | [#剑指 Offer 53 - II 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2020-08-13 15:58 | [#剑指 Offer 53 - I 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | EASY | 19 | **2** |
| 2020-08-13 10:15 | [#剑指 Offer 61 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof) | EASY | 2 | 1 |
| 2020-08-13 09:09 | [#剑指 Offer 58 - I 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof) | EASY | 10 | 1 |
| 2020-08-12 16:11 | [#剑指 Offer 42 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | EASY | 8 | 1 |
| 2020-08-12 15:43 | [#剑指 Offer 57 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof) | EASY | 6 | 1 |
| 2020-08-12 08:44 | [#剑指 Offer 54 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof) | EASY | 7 | 1 |
| 2020-08-12 08:07 | [#剑指 Offer 68 - I 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 2 | 1 |
| 2020-08-12 07:41 | [#面试题 04.02 最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci) | EASY | 9 | 1 |
| 2020-08-05 15:25 | [#面试题 04.04 检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci) | EASY | 2 | 1 |
| 2020-08-05 15:25 | [#剑指 Offer 55 - II 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof) | EASY | 6 | 1 |
| 2020-08-05 12:40 | [#剑指 Offer 55 - I 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof) | EASY | 3 | 1 |
| 2020-08-04 20:07 | [#剑指 Offer 50 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof) | EASY | 4 | 1 |
| 2020-08-04 19:35 | [#剑指 Offer 40 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 4 | 1 |
| 2020-08-04 19:29 | [#350 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 4 | **2** |
| 2020-08-04 19:08 | [#剑指 Offer 68 - II 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 | 1 |
| 2020-08-04 07:17 | [#剑指 Offer 39 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof) | EASY | 4 | 1 |
| 2020-08-04 07:05 | [#剑指 Offer 32 - II 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) | EASY | 5 | 1 |
| 2020-08-04 06:38 | [#剑指 Offer 30 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof) | EASY | 5 | 1 |
| 2020-08-03 15:24 | [#剑指 Offer 29 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof) | EASY | 1 | 1 |
| 2020-08-03 14:49 | [#剑指 Offer 28 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 3 | 1 |
| 2020-08-03 14:26 | [#剑指 Offer 27 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 6 | 1 |
| 2020-08-03 13:58 | [#剑指 Offer 21 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof) | EASY | 13 | 1 |
| 2020-08-02 19:08 | [#剑指 Offer 17 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof) | EASY | 2 | 1 |
| 2020-08-02 15:21 | [#剑指 Offer 15 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | EASY | 7 | 1 |
| 2020-08-02 09:17 | [#剑指 Offer 11 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 4 | 1 |
| 2020-08-02 08:06 | [#剑指 Offer 10- II 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof) | EASY | 8 | 1 |
| 2020-08-01 15:39 | [#剑指 Offer 10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 11 | 1 |
| 2020-08-01 15:02 | [#剑指 Offer 09 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 1 | 1 |
| 2020-08-01 14:25 | [#剑指 Offer 05 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 3 | 1 |
| 2020-08-01 13:40 | [#剑指 Offer 04 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) | MEDIUM | 3 | 1 |
| 2020-08-01 13:08 | [#剑指 Offer 03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 9 | 1 |
| 2020-07-31 19:14 | [#242 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram) | EASY | 28 | 1 |
| 2020-07-31 18:04 | [#202 快乐数](https://leetcode-cn.com/problems/happy-number) | EASY | 5 | 1 |
| 2020-07-31 15:36 | [#412 Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | EASY | 2 | 1 |
| 2020-07-31 15:26 | [#387 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string) | EASY | 10 | 1 |
| 2020-07-31 14:47 | [#204 计数质数](https://leetcode-cn.com/problems/count-primes) | EASY | 19 | 1 |
| 2020-07-31 07:04 | [#371 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | EASY | 1 | 1 |
| 2020-07-31 06:42 | [#268 丢失的数字](https://leetcode-cn.com/problems/missing-number) | EASY | 10 | 1 |
| 2020-07-31 05:53 | [#169 多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 6 | **2** |
| 2020-07-29 13:24 | [#538 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree) | MEDIUM | 3 | **2** |
| 2020-07-28 17:53 | [#189 旋转数组](https://leetcode-cn.com/problems/rotate-array) | MEDIUM | 4 | 1 |
| 2020-07-28 16:49 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | MEDIUM | 7 | 1 |
| 2020-07-28 15:43 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 15 | **2** |
| 2020-07-27 13:01 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 5 | 1 |
| 2020-07-27 12:25 | [#581 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) | MEDIUM | 3 | **2** |
| 2020-07-26 13:57 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 3 | 1 |
| 2020-07-25 15:51 | [#448 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 2 | 1 |
| 2020-07-25 15:33 | [#283 移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 2 | 1 |
| 2020-07-25 15:11 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 4 | 1 |
| 2020-07-25 14:42 | [#172 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes) | EASY | 31 | **2** |
| 2020-07-24 15:58 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 7 | 1 |
| 2020-07-24 15:31 | [#326 3的幂](https://leetcode-cn.com/problems/power-of-three) | EASY | 5 | 1 |
| 2020-07-23 08:49 | [#292 Nim 游戏](https://leetcode-cn.com/problems/nim-game) | EASY | 1 | 1 |
| 2020-07-23 08:37 | [#217 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | EASY | 10 | 1 |
| 2020-07-22 14:53 | [#155 最小栈](https://leetcode-cn.com/problems/min-stack) | EASY | 3 | 1 |
| 2020-07-21 15:05 | [#231 2的幂](https://leetcode-cn.com/problems/power-of-two) | EASY | 3 | 1 |
| 2020-07-21 14:40 | [#面试题 02.03 删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci) | EASY | 1 | 1 |
| 2020-07-21 14:34 | [#面试题 02.01 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci) | EASY | 4 | 1 |
| 2020-07-21 13:33 | [#面试题 02.02 返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci) | EASY | 1 | 1 |
| 2020-07-21 13:29 | [#面试题 02.07 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci) | EASY | 1 | 1 |
| 2020-07-21 13:19 | [#面试题 02.06 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci) | EASY | 7 | 1 |
| 2020-07-21 09:04 | [#剑指 Offer 52 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | EASY | 1 | 1 |
| 2020-07-21 09:00 | [#剑指 Offer 25 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof) | EASY | 1 | 1 |
| 2020-07-21 08:45 | [#剑指 Offer 24 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof) | EASY | 1 | 1 |
| 2020-07-21 08:35 | [#1290 二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) | EASY | 3 | 1 |
| 2020-07-21 08:29 | [#剑指 Offer 22 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | EASY | 5 | 1 |
| 2020-07-21 08:12 | [#剑指 Offer 18 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof) | EASY | 1 | 1 |
| 2020-07-19 13:14 | [#剑指 Offer 06 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 7 | 1 |
| 2020-07-19 12:39 | [#876 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list) | EASY | 2 | 1 |
| 2020-07-19 12:27 | [#237 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | EASY | 1 | 1 |
| 2020-07-19 12:17 | [#234 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 2 | 1 |
| 2020-07-19 11:31 | [#206 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 1 | 1 |
| 2020-07-19 11:25 | [#203 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | EASY | 1 | 1 |
| 2020-07-19 11:01 | [#160 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 2 | 1 |
| 2020-07-18 20:11 | [#143 重排链表](https://leetcode-cn.com/problems/reorder-list) | MEDIUM | 1 | 1 |
| 2020-07-18 13:03 | [#142 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | MEDIUM | 6 | 1 |
| 2020-07-18 12:59 | [#141 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 7 | 1 |
| 2020-07-18 11:45 | [#136 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 1 | 1 |
| 2020-07-17 19:49 | [#125 验证回文串](https://leetcode-cn.com/problems/valid-palindrome) | EASY | 4 | 1 |
| 2020-07-17 18:24 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 4 | 1 |
| 2020-07-17 18:13 | [#118 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 1 | 1 |
| 2020-07-14 15:46 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 3 | 1 |
| 2020-07-14 15:02 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 6 | 1 |
| 2020-07-14 09:15 | [#101 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 4 | 1 |
| 2020-07-14 08:23 | [#100 相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 | 1 |
| 2020-07-14 08:11 | [#88 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 1 | 1 |
| 2020-07-13 20:06 | [#83 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 4 | 1 |
| 2020-07-13 19:41 | [#70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 2 | 1 |
| 2020-07-13 16:11 | [#69 x 的平方根](https://leetcode-cn.com/problems/sqrtx) | EASY | 10 | 1 |
| 2020-07-13 05:52 | [#67 二进制求和](https://leetcode-cn.com/problems/add-binary) | EASY | 2 | 1 |
| 2020-07-12 19:11 | [#66 加一](https://leetcode-cn.com/problems/plus-one) | EASY | 2 | 1 |
| 2020-07-12 18:52 | [#58 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | EASY | 2 | 1 |
| 2020-07-12 17:31 | [#53 最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 3 | 1 |
| 2020-07-12 08:32 | [#35 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 3 | 1 |
| 2020-07-12 08:13 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 16 | 1 |
| 2020-07-12 07:36 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 3 | 1 |
| 2020-07-12 07:07 | [#26 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 4 | 1 |
| 2020-07-11 16:24 | [#1394 找出数组中的幸运数](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) | EASY | 2 | 1 |
| 2020-07-11 15:57 | [#1389 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | EASY | 3 | 1 |
| 2020-07-11 15:34 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 11 | 1 |
| 2020-07-11 10:39 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 7 | 1 |
| 2020-07-10 15:32 | [#14 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 17 | 1 |
| 2020-07-10 14:50 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 17 | 1 |
| 2020-07-10 12:58 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 15 | 1 |
| 2020-07-10 12:21 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 5 | 1 |
| 2020-07-10 08:59 | [#1470 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array) | EASY | 2 | 1 |
| 2020-07-10 06:11 | [#1431 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) | EASY | 4 | 1 |
| 2020-07-10 05:47 | [#1480 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | EASY | 4 | 1 |
| 2020-06-16 04:05 | [#9 回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 32 | **3** |
