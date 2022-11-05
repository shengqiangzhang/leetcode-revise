## 相关介绍
这是一个LeetCode题目自动统计及分析程序, 可自动统计所有提交通过的题目, 并以Markdown的形式展示。

根据个人需求, 目前只考虑获取**提交次数**和**重刷次数**这两个指标, 以便更好地进行刷题。

采用GitHub Action进行自动化部署，无需本地服务器资源。
## 使用教程
1. Fork本项目
2. 点击Fork后的项目下的Settings->Secrets->Actions->New repository secret, 分别添加以下secret:
    - Name:LEETCODE_EMAIL
        - Secret:你的LeetCode账号
    - Name:LEETCODE_PASSWORD
        - Secret:你的LeetCode密码
3. 回到项目首页并进入Actions，点击绿色按钮`I understand my workflows, go ahead and enable them`，在左侧点击`Github LeetCode Bot`，再点击黄色提示框中的`Enable workflow`，接着再点击蓝色提示框中的`Run workflow`即可
## 补充说明
默认配置为12小时更新一次，可根据需求修改[action.yml](.github/workflows/action.yml#L9)文件的第 `9` 行。如有其他需求, 欢迎提交PR。


> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2022-11-05 18:31 | [#1106 解析布尔表达式](https://leetcode.cn/problems/parsing-a-boolean-expression) | HARD | 3 | 1 |
| 2022-11-04 14:12 | [#754 到达终点数字](https://leetcode.cn/problems/reach-a-number) | MEDIUM | 4 | 1 |
| 2022-11-03 09:42 | [#1668 最大重复子字符串](https://leetcode.cn/problems/maximum-repeating-substring) | EASY | 3 | 1 |
| 2022-11-02 20:43 | [#1620 网络信号最好的坐标](https://leetcode.cn/problems/coordinate-with-maximum-network-quality) | MEDIUM | 1 | 1 |
| 2022-11-01 21:37 | [#912 排序数组](https://leetcode.cn/problems/sort-an-array) | MEDIUM | 1 | 1 |
| 2022-11-01 15:38 | [#剑指 Offer 51 数组中的逆序对](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof) | HARD | 2 | **2** |
| 2022-11-01 14:49 | [#1662 检查两个字符串数组是否相等](https://leetcode.cn/problems/check-if-two-string-arrays-are-equivalent) | EASY | 1 | 1 |
| 2022-10-31 10:25 | [#481 神奇字符串](https://leetcode.cn/problems/magical-string) | MEDIUM | 4 | 1 |
| 2022-10-30 20:27 | [#784 字母大小写全排列](https://leetcode.cn/problems/letter-case-permutation) | MEDIUM | 4 | **2** |
| 2022-10-29 23:17 | [#1773 统计匹配检索规则的物品数量](https://leetcode.cn/problems/count-items-matching-a-rule) | EASY | 2 | 1 |
| 2022-10-27 10:20 | [#1822 数组元素积的符号](https://leetcode.cn/problems/sign-of-the-product-of-an-array) | EASY | 2 | 1 |
| 2022-10-24 15:37 | [#1235 规划兼职工作](https://leetcode.cn/problems/maximum-profit-in-job-scheduling) | HARD | 7 | **2** |
| 2022-10-24 08:13 | [#915 分割数组](https://leetcode.cn/problems/partition-array-into-disjoint-intervals) | MEDIUM | 3 | 1 |
| 2022-10-23 18:07 | [#1768 交替合并字符串](https://leetcode.cn/problems/merge-strings-alternately) | EASY | 2 | 1 |
| 2022-10-21 10:50 | [#901 股票价格跨度](https://leetcode.cn/problems/online-stock-span) | MEDIUM | 1 | 1 |
| 2022-10-20 21:51 | [#779 第K个语法符号](https://leetcode.cn/problems/k-th-symbol-in-grammar) | MEDIUM | 1 | 1 |
| 2022-10-19 16:47 | [#1700 无法吃午餐的学生数量](https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch) | EASY | 2 | 1 |
| 2022-10-17 12:25 | [#904 水果成篮](https://leetcode.cn/problems/fruit-into-baskets) | MEDIUM | 3 | 1 |
| 2022-10-16 13:16 | [#886 可能的二分法](https://leetcode.cn/problems/possible-bipartition) | MEDIUM | 4 | 1 |
| 2022-10-15 14:16 | [#7 整数反转](https://leetcode.cn/problems/reverse-integer) | MEDIUM | 4 | 1 |
| 2022-10-15 10:09 | [#1441 用栈操作构建数组](https://leetcode.cn/problems/build-an-array-with-stack-operations) | MEDIUM | 4 | 1 |
| 2022-10-14 16:07 | [#940 不同的子序列 II](https://leetcode.cn/problems/distinct-subsequences-ii) | HARD | 6 | 1 |
| 2022-10-13 20:08 | [#769 最多能完成排序的块](https://leetcode.cn/problems/max-chunks-to-make-sorted) | MEDIUM | 2 | 1 |
| 2022-10-12 16:31 | [#743 网络延迟时间](https://leetcode.cn/problems/network-delay-time) | MEDIUM | 7 | **4** |
| 2022-10-12 15:40 | [#787 K 站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops) | MEDIUM | 4 | 1 |
| 2022-10-12 10:03 | [#817 链表组件](https://leetcode.cn/problems/linked-list-components) | MEDIUM | 6 | 1 |
| 2022-10-11 10:02 | [#1790 仅执行一次字符串交换能否使两个字符串相等](https://leetcode.cn/problems/check-if-one-string-swap-can-make-strings-equal) | EASY | 3 | 1 |
| 2022-10-10 12:24 | [#856 括号的分数](https://leetcode.cn/problems/score-of-parentheses) | MEDIUM | 2 | 1 |
| 2022-10-08 10:54 | [#870 优势洗牌](https://leetcode.cn/problems/advantage-shuffle) | MEDIUM | 2 | 1 |
| 2022-10-07 12:41 | [#1694 重新格式化电话号码](https://leetcode.cn/problems/reformat-phone-number) | EASY | 2 | 1 |
| 2022-10-07 12:16 | [#1800 最大升序子数组和](https://leetcode.cn/problems/maximum-ascending-subarray-sum) | EASY | 3 | 1 |
| 2022-10-05 12:22 | [#811 子域名访问计数](https://leetcode.cn/problems/subdomain-visit-count) | MEDIUM | 1 | 1 |
| 2022-10-04 22:20 | [#921 使括号有效的最少添加](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid) | MEDIUM | 4 | 1 |
| 2022-09-30 15:12 | [#73 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes) | MEDIUM | 1 | 1 |
| 2022-09-30 14:44 | [#面试题 01.08 零矩阵](https://leetcode.cn/problems/zero-matrix-lcci) | MEDIUM | 2 | 1 |
| 2022-09-29 23:57 | [#面试题 17.09 第 k 个数](https://leetcode.cn/problems/get-kth-magic-number-lcci) | MEDIUM | 3 | 1 |
| 2022-09-29 10:16 | [#面试题 01.09 字符串轮转](https://leetcode.cn/problems/string-rotation-lcci) | EASY | 1 | 1 |
| 2022-09-27 22:47 | [#面试题 01.02 判定是否互为字符重排](https://leetcode.cn/problems/check-permutation-lcci) | EASY | 1 | 1 |
| 2022-09-27 11:35 | [#面试题 17.19 消失的两个数字](https://leetcode.cn/problems/missing-two-lcci) | HARD | 3 | 1 |
| 2022-09-26 15:21 | [#788 旋转数字](https://leetcode.cn/problems/rotated-digits) | MEDIUM | 1 | 1 |
| 2022-09-22 09:45 | [#1640 能否连接形成数组](https://leetcode.cn/problems/check-array-formation-through-concatenation) | EASY | 3 | 1 |
| 2022-09-13 15:55 | [#1608 特殊数组的特征值](https://leetcode.cn/problems/special-array-with-x-elements-greater-than-or-equal-x) | EASY | 7 | 1 |
| 2022-09-13 15:06 | [#670 最大交换](https://leetcode.cn/problems/maximum-swap) | MEDIUM | 7 | 1 |
| 2022-09-09 15:29 | [#1598 文件夹操作日志搜集器](https://leetcode.cn/problems/crawler-log-folder) | EASY | 3 | 1 |
| 2022-09-01 13:48 | [#1475 商品折扣后的最终价格](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop) | EASY | 1 | 1 |
| 2022-08-31 13:22 | [#946 验证栈序列](https://leetcode.cn/problems/validate-stack-sequences) | MEDIUM | 2 | 1 |
| 2022-08-19 12:44 | [#1450 在既定时间做作业的学生人数](https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time) | EASY | 1 | 1 |
| 2022-08-17 12:14 | [#1302 层数最深叶子节点的和](https://leetcode.cn/problems/deepest-leaves-sum) | MEDIUM | 1 | 1 |
| 2022-08-10 18:34 | [#640 求解方程](https://leetcode.cn/problems/solve-the-equation) | MEDIUM | 4 | 1 |
| 2022-08-01 12:42 | [#1374 生成每种字符都是奇数个的字符串](https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts) | EASY | 1 | 1 |
| 2022-07-25 14:34 | [#919 完全二叉树插入器](https://leetcode.cn/problems/complete-binary-tree-inserter) | MEDIUM | 1 | 1 |
| 2022-07-23 14:13 | [#剑指 Offer II 115 重建序列](https://leetcode.cn/problems/ur2n8P) | MEDIUM | 7 | 1 |
| 2022-07-17 11:09 | [#565 数组嵌套](https://leetcode.cn/problems/array-nesting) | MEDIUM | 1 | 1 |
| 2022-07-14 13:12 | [#745 前缀和后缀搜索](https://leetcode.cn/problems/prefix-and-suffix-search) | HARD | 2 | 1 |
| 2022-07-13 19:22 | [#735 行星碰撞](https://leetcode.cn/problems/asteroid-collision) | MEDIUM | 11 | 1 |
| 2022-07-11 13:05 | [#676 实现一个魔法字典](https://leetcode.cn/problems/implement-magic-dictionary) | MEDIUM | 2 | 1 |
| 2022-07-08 14:39 | [#3 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters) | MEDIUM | 5 | 1 |
| 2022-07-08 13:51 | [#1217 玩筹码](https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position) | EASY | 1 | 1 |
| 2022-07-07 15:38 | [#648 单词替换](https://leetcode.cn/problems/replace-words) | MEDIUM | 3 | 1 |
| 2022-07-05 14:13 | [#307 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable) | MEDIUM | 3 | **2** |
| 2022-07-05 11:23 | [#729 我的日程安排表 I](https://leetcode.cn/problems/my-calendar-i) | MEDIUM | 8 | 1 |
| 2022-07-04 10:40 | [#1200 最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference) | EASY | 2 | 1 |
| 2022-07-03 20:08 | [#556 下一个更大元素 III](https://leetcode.cn/problems/next-greater-element-iii) | MEDIUM | 1 | 1 |
| 2022-07-03 18:41 | [#31 下一个排列](https://leetcode.cn/problems/next-permutation) | MEDIUM | 3 | 1 |
| 2022-06-24 13:38 | [#515 在每个树行中找最大值](https://leetcode.cn/problems/find-largest-value-in-each-tree-row) | MEDIUM | 1 | 1 |
| 2022-06-22 14:33 | [#513 找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value) | MEDIUM | 4 | 1 |
| 2022-06-21 19:28 | [#1108 IP 地址无效化](https://leetcode.cn/problems/defanging-an-ip-address) | EASY | 2 | 1 |
| 2022-06-19 23:06 | [#98 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree) | MEDIUM | 13 | 1 |
| 2022-06-19 15:20 | [#508 出现次数最多的子树元素和](https://leetcode.cn/problems/most-frequent-subtree-sum) | MEDIUM | 2 | 1 |
| 2022-06-18 14:19 | [#剑指 Offer II 029 排序的循环链表](https://leetcode.cn/problems/4ueAj6) | MEDIUM | 15 | 1 |
| 2022-06-17 15:48 | [#1089 复写零](https://leetcode.cn/problems/duplicate-zeros) | EASY | 2 | 1 |
| 2022-06-13 23:05 | [#1051 高度检查器](https://leetcode.cn/problems/height-checker) | EASY | 2 | 1 |
| 2022-06-12 23:05 | [#890 查找和替换模式](https://leetcode.cn/problems/find-and-replace-pattern) | MEDIUM | 1 | 1 |
| 2022-06-05 14:59 | [#478 在圆内随机生成点](https://leetcode.cn/problems/generate-random-point-in-a-circle) | MEDIUM | 8 | 1 |
| 2022-06-04 12:34 | [#929 独特的电子邮件地址](https://leetcode.cn/problems/unique-email-addresses) | EASY | 5 | 1 |
| 2022-05-30 20:32 | [#1022 从根到叶的二进制数之和](https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers) | EASY | 3 | 1 |
| 2022-05-28 12:21 | [#1021 删除最外层的括号](https://leetcode.cn/problems/remove-outermost-parentheses) | EASY | 1 | 1 |
| 2022-05-27 17:40 | [#面试题 17.11 单词距离](https://leetcode.cn/problems/find-closest-lcci) | MEDIUM | 2 | 1 |
| 2022-05-24 12:35 | [#965 单值二叉树](https://leetcode.cn/problems/univalued-binary-tree) | EASY | 2 | 1 |
| 2022-05-21 17:47 | [#961 在长度 2N 的数组中找出重复 N 次的元素](https://leetcode.cn/problems/n-repeated-element-in-size-2n-array) | EASY | 2 | 1 |
| 2022-05-20 14:55 | [#436 寻找右区间](https://leetcode.cn/problems/find-right-interval) | MEDIUM | 3 | 1 |
| 2022-05-19 13:50 | [#462 最小操作次数使数组元素相等 II](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii) | MEDIUM | 1 | 1 |
| 2022-05-18 13:08 | [#668 乘法表中第k小的数](https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table) | HARD | 3 | 1 |
| 2022-05-17 11:08 | [#953 验证外星语词典](https://leetcode.cn/problems/verifying-an-alien-dictionary) | EASY | 2 | 1 |
| 2022-05-16 16:08 | [#面试题 04.06 后继者](https://leetcode.cn/problems/successor-lcci) | MEDIUM | 5 | 1 |
| 2022-05-15 14:35 | [#812 最大三角形面积](https://leetcode.cn/problems/largest-triangle-area) | EASY | 4 | 1 |
| 2022-05-13 22:09 | [#102 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal) | MEDIUM | 3 | 1 |
| 2022-05-13 13:28 | [#面试题 01.05 一次编辑](https://leetcode.cn/problems/one-away-lcci) | MEDIUM | 3 | 1 |
| 2022-05-12 21:36 | [#944 删列造序](https://leetcode.cn/problems/delete-columns-to-make-sorted) | EASY | 2 | 1 |
| 2022-05-10 15:12 | [#210 课程表 II](https://leetcode.cn/problems/course-schedule-ii) | MEDIUM | 2 | 1 |
| 2022-05-09 14:49 | [#107 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii) | MEDIUM | 2 | 1 |
| 2022-05-09 14:35 | [#117 填充每个节点的下一个右侧节点指针 II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii) | MEDIUM | 1 | 1 |
| 2022-05-09 14:32 | [#116 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node) | MEDIUM | 2 | 1 |
| 2022-05-09 13:49 | [#942 增减字符串匹配](https://leetcode.cn/problems/di-string-match) | EASY | 1 | 1 |
| 2022-05-08 10:22 | [#442 数组中重复的数据](https://leetcode.cn/problems/find-all-duplicates-in-an-array) | MEDIUM | 1 | 1 |
| 2022-05-07 20:21 | [#207 课程表](https://leetcode.cn/problems/course-schedule) | MEDIUM | 2 | 1 |
| 2022-05-07 16:37 | [#433 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation) | MEDIUM | 3 | 1 |
| 2022-05-06 15:00 | [#113 路径总和 II](https://leetcode.cn/problems/path-sum-ii) | MEDIUM | 1 | 1 |
| 2022-05-06 14:46 | [#933 最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls) | EASY | 1 | 1 |
| 2022-05-05 11:07 | [#713 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k) | MEDIUM | 3 | 1 |
| 2022-05-04 12:31 | [#1823 找出游戏的获胜者](https://leetcode.cn/problems/find-the-winner-of-the-circular-game) | MEDIUM | 2 | 1 |
| 2022-05-03 12:37 | [#937 重新排列日志文件](https://leetcode.cn/problems/reorder-data-in-log-files) | MEDIUM | 2 | 1 |
| 2022-05-02 15:00 | [#591 标签验证器](https://leetcode.cn/problems/tag-validator) | HARD | 8 | 1 |
| 2022-05-02 14:17 | [#796 旋转字符串](https://leetcode.cn/problems/rotate-string) | EASY | 4 | **2** |
| 2022-05-01 17:59 | [#1305 两棵二叉搜索树中的所有元素](https://leetcode.cn/problems/all-elements-in-two-binary-search-trees) | MEDIUM | 3 | 1 |
| 2022-04-30 14:28 | [#908 最小差值 I](https://leetcode.cn/problems/smallest-range-i) | EASY | 6 | 1 |
| 2022-04-29 15:45 | [#427 建立四叉树](https://leetcode.cn/problems/construct-quad-tree) | MEDIUM | 1 | 1 |
| 2022-04-28 12:36 | [#905 按奇偶排序数组](https://leetcode.cn/problems/sort-array-by-parity) | EASY | 2 | 1 |
| 2022-04-26 19:39 | [#883 三维形体投影面积](https://leetcode.cn/problems/projection-area-of-3d-shapes) | EASY | 2 | 1 |
| 2022-04-25 12:52 | [#398 随机数索引](https://leetcode.cn/problems/random-pick-index) | MEDIUM | 2 | 1 |
| 2022-04-24 13:08 | [#868 二进制间距](https://leetcode.cn/problems/binary-gap) | EASY | 1 | 1 |
| 2022-04-22 15:01 | [#396 旋转函数](https://leetcode.cn/problems/rotate-function) | MEDIUM | 2 | 1 |
| 2022-04-21 13:01 | [#824 山羊拉丁文](https://leetcode.cn/problems/goat-latin) | EASY | 1 | 1 |
| 2022-04-20 14:44 | [#388 文件的最长绝对路径](https://leetcode.cn/problems/longest-absolute-file-path) | MEDIUM | 2 | 1 |
| 2022-04-19 12:26 | [#821 字符的最短距离](https://leetcode.cn/problems/shortest-distance-to-a-character) | EASY | 1 | 1 |
| 2022-04-18 15:36 | [#386 字典序排数](https://leetcode.cn/problems/lexicographical-numbers) | MEDIUM | 2 | 1 |
| 2022-04-17 13:28 | [#819 最常见的单词](https://leetcode.cn/problems/most-common-word) | EASY | 3 | 1 |
| 2022-04-16 12:46 | [#479 最大回文数乘积](https://leetcode.cn/problems/largest-palindrome-product) | HARD | 2 | 1 |
| 2022-04-15 15:05 | [#385 迷你语法分析器](https://leetcode.cn/problems/mini-parser) | MEDIUM | 4 | 1 |
| 2022-04-14 10:21 | [#1672 最富有客户的资产总量](https://leetcode.cn/problems/richest-customer-wealth) | EASY | 1 | 1 |
| 2022-04-13 18:53 | [#380 O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1) | MEDIUM | 5 | 1 |
| 2022-04-12 10:06 | [#806 写字符串需要的行数](https://leetcode.cn/problems/number-of-lines-to-write-string) | EASY | 1 | 1 |
| 2022-04-11 15:05 | [#357 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits) | MEDIUM | 1 | 1 |
| 2022-04-10 12:27 | [#804 唯一摩尔斯密码词](https://leetcode.cn/problems/unique-morse-code-words) | EASY | 1 | 1 |
| 2022-04-09 18:33 | [#780 到达终点](https://leetcode.cn/problems/reaching-points) | HARD | 6 | 1 |
| 2022-04-08 11:24 | [#429 N 叉树的层序遍历](https://leetcode.cn/problems/n-ary-tree-level-order-traversal) | MEDIUM | 2 | 1 |
| 2022-04-06 14:13 | [#310 最小高度树](https://leetcode.cn/problems/minimum-height-trees) | MEDIUM | 1 | 1 |
| 2022-04-05 15:42 | [#762 二进制表示中质数个计算置位](https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation) | EASY | 3 | 1 |
| 2022-04-03 20:29 | [#744 寻找比目标字母大的最小字母](https://leetcode.cn/problems/find-smallest-letter-greater-than-target) | EASY | 8 | 1 |
| 2022-04-02 20:52 | [#198 打家劫舍](https://leetcode.cn/problems/house-robber) | MEDIUM | 8 | **3** |
| 2022-04-02 18:50 | [#132 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii) | HARD | 4 | 1 |
| 2022-04-01 11:41 | [#954 二倍数对数组](https://leetcode.cn/problems/array-of-doubled-pairs) | MEDIUM | 10 | 1 |
| 2022-03-31 12:57 | [#728 自除数](https://leetcode.cn/problems/self-dividing-numbers) | EASY | 1 | 1 |
| 2022-03-30 17:45 | [#1606 找到处理最多请求的服务器](https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests) | HARD | 6 | 1 |
| 2022-03-29 13:49 | [#2024 考试的最大困扰度](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam) | MEDIUM | 1 | 1 |
| 2022-03-28 14:22 | [#693 交替位二进制数](https://leetcode.cn/problems/binary-number-with-alternating-bits) | EASY | 1 | 1 |
| 2022-03-27 12:46 | [#2028 找出缺失的观测数据](https://leetcode.cn/problems/find-missing-observations) | MEDIUM | 7 | 1 |
| 2022-03-26 15:02 | [#682 棒球比赛](https://leetcode.cn/problems/baseball-game) | EASY | 1 | 1 |
| 2022-03-25 13:23 | [#172 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes) | MEDIUM | 4 | 1 |
| 2022-03-24 10:20 | [#661 图片平滑器](https://leetcode.cn/problems/image-smoother) | EASY | 1 | 1 |
| 2022-03-23 18:40 | [#440 字典序的第K小数字](https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order) | HARD | 6 | 1 |
| 2022-03-22 12:43 | [#2038 如果相邻两个颜色均相同则删除当前颜色](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color) | MEDIUM | 3 | 1 |
| 2022-03-21 15:27 | [#653 两数之和 IV - 输入二叉搜索树](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst) | EASY | 1 | 1 |
| 2022-03-20 15:10 | [#2039 网络空闲的时刻](https://leetcode.cn/problems/the-time-when-the-network-becomes-idle) | MEDIUM | 1 | 1 |
| 2022-03-19 15:00 | [#606 根据二叉树创建字符串](https://leetcode.cn/problems/construct-string-from-binary-tree) | EASY | 3 | 1 |
| 2022-03-18 12:11 | [#2043 简易银行系统](https://leetcode.cn/problems/simple-bank-system) | MEDIUM | 1 | 1 |
| 2022-03-17 14:57 | [#720 词典中最长的单词](https://leetcode.cn/problems/longest-word-in-dictionary) | MEDIUM | 8 | 1 |
| 2022-03-16 19:29 | [#432 全 O(1) 的数据结构](https://leetcode.cn/problems/all-oone-data-structure) | HARD | 4 | 1 |
| 2022-03-15 15:21 | [#2044 统计按位或能得到最大值的子集数目](https://leetcode.cn/problems/count-number-of-maximum-bitwise-or-subsets) | MEDIUM | 6 | 1 |
| 2022-03-14 11:27 | [#599 两个列表的最小索引总和](https://leetcode.cn/problems/minimum-index-sum-of-two-lists) | EASY | 2 | 1 |
| 2022-03-13 16:05 | [#393 UTF-8 编码验证](https://leetcode.cn/problems/utf-8-validation) | MEDIUM | 10 | 1 |
| 2022-03-12 13:21 | [#590 N 叉树的后序遍历](https://leetcode.cn/problems/n-ary-tree-postorder-traversal) | EASY | 1 | 1 |
| 2021-09-14 15:09 | [#524 通过删除字母匹配到字典里最长单词](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting) | MEDIUM | 3 | 1 |
| 2021-08-03 13:57 | [#581 最短无序连续子数组](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray) | MEDIUM | 8 | 1 |
| 2021-07-30 19:34 | [#171 Excel 表列序号](https://leetcode.cn/problems/excel-sheet-column-number) | EASY | 5 | 1 |
| 2021-07-13 09:53 | [#40 组合总和 II](https://leetcode.cn/problems/combination-sum-ii) | MEDIUM | 3 | 1 |
| 2021-07-13 09:16 | [#39 组合总和](https://leetcode.cn/problems/combination-sum) | MEDIUM | 1 | 1 |
| 2021-07-12 19:52 | [#714 买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | MEDIUM | 1 | 1 |
| 2021-07-12 18:59 | [#740 删除并获得点数](https://leetcode.cn/problems/delete-and-earn) | MEDIUM | 1 | 1 |
| 2021-07-07 14:10 | [#213 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii) | MEDIUM | 3 | 1 |
| 2021-07-06 16:21 | [#746 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs) | EASY | 1 | 1 |
| 2021-07-06 16:03 | [#70 爬楼梯](https://leetcode.cn/problems/climbing-stairs) | EASY | 2 | 1 |
| 2021-07-05 15:44 | [#120 三角形最小路径和](https://leetcode.cn/problems/triangle) | MEDIUM | 2 | 1 |
| 2021-07-05 14:12 | [#55 跳跃游戏](https://leetcode.cn/problems/jump-game) | MEDIUM | 4 | 1 |
| 2021-07-05 13:41 | [#45 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii) | MEDIUM | 15 | 1 |
| 2021-07-05 13:03 | [#22 括号生成](https://leetcode.cn/problems/generate-parentheses) | MEDIUM | 2 | **2** |
| 2021-07-05 12:31 | [#509 斐波那契数](https://leetcode.cn/problems/fibonacci-number) | EASY | 2 | 1 |
| 2021-07-05 12:30 | [#1137 第 N 个泰波那契数](https://leetcode.cn/problems/n-th-tribonacci-number) | EASY | 1 | 1 |
| 2021-07-02 15:38 | [#1833 雪糕的最大数量](https://leetcode.cn/problems/maximum-ice-cream-bars) | MEDIUM | 4 | 1 |
| 2021-06-15 10:56 | [#33 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array) | MEDIUM | 1 | 1 |
| 2021-06-15 10:36 | [#852 山脉数组的峰顶索引](https://leetcode.cn/problems/peak-index-in-a-mountain-array) | MEDIUM | 1 | 1 |
| 2021-06-13 15:46 | [#278 第一个错误的版本](https://leetcode.cn/problems/first-bad-version) | EASY | 4 | 1 |
| 2021-06-07 19:49 | [#494 目标和](https://leetcode.cn/problems/target-sum) | MEDIUM | 1 | 1 |
| 2021-06-04 09:26 | [#160 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists) | EASY | 7 | 1 |
| 2021-05-24 16:52 | [#130 被围绕的区域](https://leetcode.cn/problems/surrounded-regions) | MEDIUM | 4 | **2** |
| 2021-05-24 11:09 | [#547 省份数量](https://leetcode.cn/problems/number-of-provinces) | MEDIUM | 1 | 1 |
| 2021-05-22 00:06 | [#695 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island) | MEDIUM | 3 | 1 |
| 2021-05-21 14:21 | [#200 岛屿数量](https://leetcode.cn/problems/number-of-islands) | MEDIUM | 1 | 1 |
| 2021-05-10 15:31 | [#872 叶子相似的树](https://leetcode.cn/problems/leaf-similar-trees) | EASY | 7 | 1 |
| 2021-05-05 10:53 | [#154 寻找旋转排序数组中的最小值 II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii) | HARD | 1 | 1 |
| 2021-05-05 10:49 | [#剑指 Offer 11 旋转数组的最小数字](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 2 | **2** |
| 2021-04-13 18:39 | [#783 二叉搜索树节点最小距离](https://leetcode.cn/problems/minimum-distance-between-bst-nodes) | EASY | 1 | 1 |
| 2021-03-30 15:03 | [#47 全排列 II](https://leetcode.cn/problems/permutations-ii) | MEDIUM | 1 | 1 |
| 2021-03-30 14:38 | [#46 全排列](https://leetcode.cn/problems/permutations) | MEDIUM | 3 | 1 |
| 2021-03-30 13:37 | [#74 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix) | MEDIUM | 1 | 1 |
| 2021-03-27 22:24 | [#61 旋转链表](https://leetcode.cn/problems/rotate-list) | MEDIUM | 3 | 1 |
| 2021-03-22 18:57 | [#191 位1的个数](https://leetcode.cn/problems/number-of-1-bits) | EASY | 1 | 1 |
| 2020-11-27 20:12 | [#454 四数相加 II](https://leetcode.cn/problems/4sum-ii) | MEDIUM | 5 | 1 |
| 2020-11-25 22:35 | [#1370 上升下降字符串](https://leetcode.cn/problems/increasing-decreasing-string) | EASY | 1 | 1 |
| 2020-10-25 19:58 | [#845 数组中的最长山脉](https://leetcode.cn/problems/longest-mountain-in-array) | MEDIUM | 1 | 1 |
| 2020-10-15 20:52 | [#9 回文数](https://leetcode.cn/problems/palindrome-number) | EASY | 1 | 1 |
| 2020-09-04 13:05 | [#257 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths) | EASY | 1 | 1 |
| 2020-08-16 15:28 | [#733 图像渲染](https://leetcode.cn/problems/flood-fill) | EASY | 2 | 1 |
| 2020-08-14 23:14 | [#20 有效的括号](https://leetcode.cn/problems/valid-parentheses) | EASY | 6 | 1 |
| 2020-08-10 14:09 | [#696 计数二进制子串](https://leetcode.cn/problems/count-binary-substrings) | EASY | 4 | 1 |
| 2020-08-08 09:45 | [#99 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree) | MEDIUM | 1 | 1 |
| 2020-08-06 16:44 | [#495 提莫攻击](https://leetcode.cn/problems/teemo-attacking) | EASY | 2 | 1 |
| 2020-08-05 16:41 | [#337 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii) | MEDIUM | 2 | 1 |
| 2020-08-03 20:36 | [#415 字符串相加](https://leetcode.cn/problems/add-strings) | EASY | 6 | 1 |
| 2020-08-02 19:45 | [#114 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list) | MEDIUM | 1 | 1 |
| 2020-07-31 13:43 | [#面试题 17.01 不用加号的加法](https://leetcode.cn/problems/add-without-plus-lcci) | EASY | 1 | 1 |
| 2020-07-31 13:05 | [#面试题 08.03 魔术索引](https://leetcode.cn/problems/magic-index-lcci) | EASY | 2 | 1 |
| 2020-07-29 10:05 | [#12 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman) | MEDIUM | 1 | 1 |
| 2020-07-28 18:48 | [#104 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree) | EASY | 1 | 1 |
| 2020-07-27 10:32 | [#392 判断子序列](https://leetcode.cn/problems/is-subsequence) | EASY | 8 | 1 |
| 2020-07-26 15:18 | [#15 三数之和](https://leetcode.cn/problems/3sum) | MEDIUM | 4 | 1 |
| 2020-07-23 15:55 | [#2 两数相加](https://leetcode.cn/problems/add-two-numbers) | MEDIUM | 5 | 1 |
| 2020-07-23 14:37 | [#344 反转字符串](https://leetcode.cn/problems/reverse-string) | EASY | 5 | 1 |
| 2020-07-23 14:15 | [#64 最小路径和](https://leetcode.cn/problems/minimum-path-sum) | MEDIUM | 6 | 1 |
| 2020-07-22 21:24 | [#11 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water) | MEDIUM | 4 | 1 |
| 2020-07-21 20:02 | [#1 两数之和](https://leetcode.cn/problems/two-sum) | EASY | 7 | 1 |
| 2020-07-20 14:17 | [#167 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted) | MEDIUM | 1 | 1 |
| 2020-07-18 23:56 | [#97 交错字符串](https://leetcode.cn/problems/interleaving-string) | MEDIUM | 4 | 1 |
| 2020-07-17 16:01 | [#35 搜索插入位置](https://leetcode.cn/problems/search-insert-position) | EASY | 7 | 1 |
| 2020-04-22 22:11 | [#17 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number) | MEDIUM | 3 | 1 |
