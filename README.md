## 部署步骤
1. 安装Python3, https://www.python.org/downloads/
2. 配置Github
   - 安装Git, https://git-scm.com/downloads
   - 在Github上创建一个新仓库
   - 配置Github SSH,  https://www.cnblogs.com/qlqwjy/p/8574456.html
   - Clone这个仓库到本地指定目录
   - 将`leetcode.py`放置于本仓库目录下
3. 部署到后台服务器命令:
   ```bash
   nohup python -u leetcode.py > leetcode.log 2>&1 &
   cat leetcode.log
   exit
   ```

> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2020-08-16 22:40 | [#剑指 Offer 57 - II 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) | EASY | 3 | 1 |
| 2020-08-16 21:17 | [#剑指 Offer 60 n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof) | EASY | 3 | 1 |
| 2020-08-16 00:21 | [#剑指 Offer 59 - I 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof) | EASY | 3 | 1 |
| 2020-08-15 03:28 | [#剑指 Offer 58 - II 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof) | EASY | 8 | **2** |
| 2020-08-15 03:27 | [#面试题 17.01 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci) | EASY | 6 | **2** |
| 2020-08-15 02:03 | [#557 反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) | EASY | 15 | **2** |
| 2020-08-15 01:44 | [#剑指 Offer 66 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof) | EASY | 1 | 1 |
| 2020-08-14 23:53 | [#剑指 Offer 65 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof) | EASY | 5 | 1 |
| 2020-08-14 23:20 | [#剑指 Offer 53 - II 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2020-08-13 23:58 | [#剑指 Offer 53 - I 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | EASY | 19 | 1 |
| 2020-08-13 18:15 | [#剑指 Offer 61 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof) | EASY | 2 | 1 |
| 2020-08-13 17:09 | [#剑指 Offer 58 - I 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof) | EASY | 10 | 1 |
| 2020-08-13 00:11 | [#剑指 Offer 42 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | EASY | 8 | **2** |
| 2020-08-12 23:43 | [#剑指 Offer 57 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof) | EASY | 6 | 1 |
| 2020-08-12 16:44 | [#剑指 Offer 54 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof) | EASY | 7 | 1 |
| 2020-08-12 16:07 | [#剑指 Offer 68 - I 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 2 | 1 |
| 2020-08-12 15:41 | [#面试题 04.02 最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci) | EASY | 9 | 1 |
| 2020-08-05 23:25 | [#面试题 04.04 检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci) | EASY | 2 | 1 |
| 2020-08-05 23:25 | [#剑指 Offer 55 - II 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof) | EASY | 6 | 1 |
| 2020-08-05 20:40 | [#剑指 Offer 55 - I 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof) | EASY | 3 | 1 |
| 2020-08-05 04:07 | [#剑指 Offer 50 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof) | EASY | 4 | 1 |
| 2020-08-05 03:35 | [#剑指 Offer 40 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 4 | **2** |
| 2020-08-05 03:29 | [#350 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 4 | **2** |
| 2020-08-05 03:08 | [#剑指 Offer 68 - II 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 | 1 |
| 2020-08-04 15:17 | [#剑指 Offer 39 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof) | EASY | 4 | 1 |
| 2020-08-04 15:05 | [#剑指 Offer 32 - II 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) | EASY | 5 | 1 |
| 2020-08-04 14:38 | [#剑指 Offer 30 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof) | EASY | 5 | 1 |
| 2020-08-03 23:24 | [#剑指 Offer 29 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof) | EASY | 1 | 1 |
| 2020-08-03 22:49 | [#剑指 Offer 28 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 3 | 1 |
| 2020-08-03 22:26 | [#剑指 Offer 27 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 6 | 1 |
| 2020-08-03 21:58 | [#剑指 Offer 21 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof) | EASY | 13 | 1 |
| 2020-08-03 03:08 | [#剑指 Offer 17 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof) | EASY | 2 | **2** |
| 2020-08-02 23:21 | [#剑指 Offer 15 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | EASY | 7 | 1 |
| 2020-08-02 17:17 | [#剑指 Offer 11 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 4 | 1 |
| 2020-08-02 16:06 | [#剑指 Offer 10- II 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof) | EASY | 8 | 1 |
| 2020-08-01 23:39 | [#剑指 Offer 10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 11 | 1 |
| 2020-08-01 23:02 | [#剑指 Offer 09 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 1 | 1 |
| 2020-08-01 22:25 | [#剑指 Offer 05 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 3 | 1 |
| 2020-08-01 21:40 | [#剑指 Offer 04 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) | EASY | 3 | 1 |
| 2020-08-01 21:08 | [#剑指 Offer 03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 9 | 1 |
| 2020-08-01 03:14 | [#242 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram) | EASY | 28 | 1 |
| 2020-08-01 02:04 | [#202 快乐数](https://leetcode-cn.com/problems/happy-number) | EASY | 5 | 1 |
| 2020-07-31 23:36 | [#412 Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | EASY | 2 | 1 |
| 2020-07-31 23:26 | [#387 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string) | EASY | 10 | 1 |
| 2020-07-31 22:47 | [#204 计数质数](https://leetcode-cn.com/problems/count-primes) | EASY | 19 | 1 |
| 2020-07-31 15:04 | [#371 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | EASY | 1 | 1 |
| 2020-07-31 14:42 | [#268 缺失数字](https://leetcode-cn.com/problems/missing-number) | EASY | 10 | 1 |
| 2020-07-31 13:53 | [#169 多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 6 | **2** |
| 2020-07-29 21:24 | [#538 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree) | EASY | 3 | 1 |
| 2020-07-29 01:53 | [#189 旋转数组](https://leetcode-cn.com/problems/rotate-array) | EASY | 4 | 1 |
| 2020-07-29 00:49 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | MEDIUM | 7 | **2** |
| 2020-07-28 23:43 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 15 | 1 |
| 2020-07-27 21:01 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 5 | 1 |
| 2020-07-27 20:25 | [#581 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) | EASY | 3 | **2** |
| 2020-07-26 23:02 | [#198 打家劫舍](https://leetcode-cn.com/problems/house-robber) | EASY | 3 | 1 |
| 2020-07-26 21:57 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 3 | 1 |
| 2020-07-25 23:51 | [#448 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 2 | 1 |
| 2020-07-25 23:33 | [#283 移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 2 | 1 |
| 2020-07-25 23:11 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 4 | 1 |
| 2020-07-25 22:42 | [#172 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes) | EASY | 31 | 1 |
| 2020-07-24 23:58 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 7 | 1 |
| 2020-07-24 23:31 | [#326 3的幂](https://leetcode-cn.com/problems/power-of-three) | EASY | 5 | 1 |
| 2020-07-23 16:49 | [#292 Nim 游戏](https://leetcode-cn.com/problems/nim-game) | EASY | 1 | 1 |
| 2020-07-23 16:37 | [#217 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | EASY | 10 | 1 |
| 2020-07-23 02:08 | [#344 反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 6 | 1 |
| 2020-07-22 22:53 | [#155 最小栈](https://leetcode-cn.com/problems/min-stack) | EASY | 3 | 1 |
| 2020-07-21 23:05 | [#231 2的幂](https://leetcode-cn.com/problems/power-of-two) | EASY | 3 | 1 |
| 2020-07-21 22:40 | [#面试题 02.03 删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci) | EASY | 1 | 1 |
| 2020-07-21 22:34 | [#面试题 02.01 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci) | EASY | 4 | 1 |
| 2020-07-21 21:33 | [#面试题 02.02 返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci) | EASY | 1 | 1 |
| 2020-07-21 21:29 | [#面试题 02.07 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci) | EASY | 1 | 1 |
| 2020-07-21 21:19 | [#面试题 02.06 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci) | EASY | 7 | 1 |
| 2020-07-21 17:04 | [#剑指 Offer 52 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | EASY | 1 | 1 |
| 2020-07-21 17:00 | [#剑指 Offer 25 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof) | EASY | 1 | 1 |
| 2020-07-21 16:45 | [#剑指 Offer 24 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof) | EASY | 1 | 1 |
| 2020-07-21 16:35 | [#1290 二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) | EASY | 3 | 1 |
| 2020-07-21 16:29 | [#剑指 Offer 22 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | EASY | 5 | 1 |
| 2020-07-21 16:12 | [#剑指 Offer 18 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof) | EASY | 1 | 1 |
| 2020-07-19 21:14 | [#剑指 Offer 06 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 7 | 1 |
| 2020-07-19 20:39 | [#876 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list) | EASY | 2 | 1 |
| 2020-07-19 20:27 | [#237 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | EASY | 1 | 1 |
| 2020-07-19 20:17 | [#234 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 2 | 1 |
| 2020-07-19 19:31 | [#206 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 1 | 1 |
| 2020-07-19 19:25 | [#203 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | EASY | 1 | 1 |
| 2020-07-19 19:01 | [#160 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 2 | 1 |
| 2020-07-19 04:11 | [#143 重排链表](https://leetcode-cn.com/problems/reorder-list) | MEDIUM | 1 | 1 |
| 2020-07-18 21:03 | [#142 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | MEDIUM | 6 | 1 |
| 2020-07-18 20:59 | [#141 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 7 | 1 |
| 2020-07-18 19:45 | [#136 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 1 | 1 |
| 2020-07-18 03:49 | [#125 验证回文串](https://leetcode-cn.com/problems/valid-palindrome) | EASY | 4 | 1 |
| 2020-07-18 02:56 | [#121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 4 | 1 |
| 2020-07-18 02:24 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 4 | 1 |
| 2020-07-18 02:13 | [#118 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 1 | 1 |
| 2020-07-14 23:46 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 3 | 1 |
| 2020-07-14 23:24 | [#107 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | EASY | 7 | 1 |
| 2020-07-14 23:02 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 6 | 1 |
| 2020-07-14 17:15 | [#101 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 4 | 1 |
| 2020-07-14 16:23 | [#100 相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 | 1 |
| 2020-07-14 16:11 | [#88 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 1 | 1 |
| 2020-07-14 04:06 | [#83 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 4 | 1 |
| 2020-07-14 03:41 | [#70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 2 | 1 |
| 2020-07-14 00:11 | [#69 x 的平方根](https://leetcode-cn.com/problems/sqrtx) | EASY | 10 | **2** |
| 2020-07-13 13:52 | [#67 二进制求和](https://leetcode-cn.com/problems/add-binary) | EASY | 2 | 1 |
| 2020-07-13 03:11 | [#66 加一](https://leetcode-cn.com/problems/plus-one) | EASY | 2 | 1 |
| 2020-07-13 02:52 | [#58 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | EASY | 2 | 1 |
| 2020-07-13 01:31 | [#53 最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 3 | 1 |
| 2020-07-12 16:32 | [#35 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 3 | 1 |
| 2020-07-12 16:13 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 16 | 1 |
| 2020-07-12 15:36 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 3 | 1 |
| 2020-07-12 15:07 | [#26 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 4 | 1 |
| 2020-07-12 00:24 | [#1394 找出数组中的幸运数](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) | EASY | 2 | 1 |
| 2020-07-11 23:57 | [#1389 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | EASY | 3 | 1 |
| 2020-07-11 23:34 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 11 | 1 |
| 2020-07-11 18:39 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 7 | 1 |
| 2020-07-10 23:32 | [#14 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 17 | 1 |
| 2020-07-10 22:50 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 17 | 1 |
| 2020-07-10 20:58 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 15 | 1 |
| 2020-07-10 20:21 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 5 | 1 |
| 2020-07-10 16:59 | [#1470 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array) | EASY | 2 | 1 |
| 2020-07-10 14:11 | [#1431 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) | EASY | 4 | 1 |
| 2020-07-10 13:47 | [#1480 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | EASY | 4 | 1 |
| 2020-06-16 12:05 | [#9 回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 32 | **3** |
