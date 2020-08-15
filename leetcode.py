#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: leetcode.py
@author: Shengqiang Zhang
@time: 2020/8/13 22:24
@mail: sqzhang77@gmail.com
"""

import requests
requests.packages.urllib3.disable_warnings()
import os
import json
import time

# 设置leetcode-cn的cookies
# 请勿泄露
COOKIES = "csrftoken=cgeGvmjhUJmUIlTIeWjcOWEYabtRPS8U2NtDvhYUq2y9ehIfiXWZZeAkDptI8MbD; __auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; __atuvc=0%7C26%2C0%7C27%2C3%7C28%2C0%7C29%2C2%7C30; _gid=GA1.2.573330392.1597219162; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1596276753,1596383327,1596572150,1597419560; a2873925c34ecbd2_gr_session_id=748717e4-2a9f-4f0b-bbba-1f034c509634; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=748717e4-2a9f-4f0b-bbba-1f034c509634; __asc=cd5e9e5f173edfc10ac83e4fd10; a2873925c34ecbd2_gr_session_id_748717e4-2a9f-4f0b-bbba-1f034c509634=true; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDgwNmJjYjE4ODVkODIzYzA4MmNjOGE4Yzk4ODFkNzk1Yzc3Y2EyIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTU5NzQyOTUzNy41MzM4MDczfQ.MYWOSmoyEa79B2-VbsPxbXoe_QNNVGufGqazsZY2flg; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1597429539; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"



# 获取某个题目的提交记录
def get_submission_list(slug):
    url = 'https://leetcode-cn.com/graphql/'

    payload = json.dumps({
        "operationName": "submissions",
        "variables": {
            "offset": 0,
            "limit": 40,
            "lastKey": "null",
            "questionSlug": slug
        },
        "query": "query submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n"
    })

    headers = {"cookie": COOKIES, "content-type": "application/json", "origin": "https://leetcode-cn.com", "referer": "https://leetcode-cn.com/progress/", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

    r = requests.post(url, data=payload, headers=headers, verify=False)
    response_data = json.loads(r.text)

    return response_data



# 获取所有通过的题目列表
def get_accepted_problems():
    url = 'https://leetcode-cn.com/graphql/'

    payload = json.dumps({
            "operationName": "userProfileQuestions",
            "variables": {
                "status": "ACCEPTED",
                "skip": 0,
                "first": 200000, # 一次返回的数据量
                "sortField": "LAST_SUBMITTED_AT",
                "sortOrder": "DESCENDING",
                "difficulty": [
                ]
            },
            "query": "query userProfileQuestions($status: StatusFilterEnum!, $skip: Int!, $first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!, $keyword: String, $difficulty: [DifficultyEnum!]) {\n  userProfileQuestions(status: $status, skip: $skip, first: $first, sortField: $sortField, sortOrder: $sortOrder, keyword: $keyword, difficulty: $difficulty) {\n    totalNum\n    questions {\n      translatedTitle\n      frontendId\n      titleSlug\n      title\n      difficulty\n      lastSubmittedAt\n      numSubmitted\n      lastSubmissionSrc {\n        sourceType\n        ... on SubmissionSrcLeetbookNode {\n          slug\n          title\n          pageId\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    })

    headers = {"cookie": COOKIES, "content-type": "application/json", "origin": "https://leetcode-cn.com", "referer": "https://leetcode-cn.com/progress/", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

    r = requests.post(url, data=payload, headers=headers, verify=False)
    response_data = json.loads(r.text)

    return r.status_code, response_data



# 生成Markdown文本
def generate_markdown_text(response_data):


    # 部署方法
    response_data = response_data['data']['userProfileQuestions']['questions']
    markdown_text = "1. 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数\n"
    markdown_text += "2. 安装Python3, https://www.python.org/downloads/\n"
    markdown_text += "3. 配置Github\n"
    markdown_text += "   - 安装Git, https://git-scm.com/downloads\n"
    markdown_text += "   - 在Github上创建一个新仓库\n"
    markdown_text += "   - 配置Github SSH,  https://www.cnblogs.com/qlqwjy/p/8574456.html\n"
    markdown_text += "   - Clone这个仓库到本地指定目录\n"
    markdown_text += "   - 将`leetcode.py`放置于本仓库目录下\n"
    markdown_text += "4. 部署到后台服务器命令:\n"
    markdown_text += "  ```bash\n"
    markdown_text += "  nohup python -u leetcode.py > leetcode.log 2>&1 &\n"
    markdown_text += "  cat leetcode.log\n"
    markdown_text += "  exit\n"
    markdown_text += "```\n"
    markdown_text += "\n"
    markdown_text += "| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |\n| ---- | ---- | ---- | ---- | ---- |\n"

    for index, sub_data in enumerate(response_data):

        # 显示进度
        print('{}/{}'.format(index + 1, len(response_data)))

        # 获取一些必要的信息
        lastSubmittedAt = time.strftime("%Y-%m-%d %H:%M", time.localtime(sub_data['lastSubmittedAt']))
        translatedTitle = "#{} {}".format(sub_data['frontendId'], sub_data['translatedTitle'])
        frontendId = sub_data['frontendId']
        difficulty = sub_data['difficulty']
        titleSlug = sub_data['titleSlug']
        numSubmitted = sub_data['numSubmitted']
        numSubmitted = str(numSubmitted)
        url = "https://leetcode-cn.com/problems/{}".format(sub_data['titleSlug'])

        # 获取重刷次数
        # 规则定义如下：提交通过的时间 与 之前提交通过的时间 不为同一天 即认为是重新刷了一遍
        submission_dict = get_submission_list(titleSlug)
        submission_list = submission_dict['data']['submissionList']['submissions']
        submission_accepted_dict = {}

        for submission in submission_list:
            status = submission['statusDisplay']
            if (status == 'Accepted'):
                submission_time = time.strftime("%Y-%m-%d", time.localtime(int(submission['timestamp'])))
                if submission_time in submission_accepted_dict.keys():
                    submission_accepted_dict[submission_time] += 1
                else:
                    submission_accepted_dict[submission_time] = 1

        # 重刷次数
        count = len(submission_accepted_dict)
        if count > 1:
            count = "**" + str(count) + "**"
        else:
            count = str(count)

        # 更新Markdown文本
        markdown_text += "| " + lastSubmittedAt + " | " + "[" + translatedTitle + "]" + "(" + url + ")" + " | " + difficulty + " | " + numSubmitted + " | " + count + " |" + "\n"


    return markdown_text



if __name__ == '__main__':

    # 循环运行
    while True:

        # 获取所有通过的题目列表
        status_code, response_data = get_accepted_problems()

        # 检测是否获取成功
        if(status_code != requests.codes.ok or "errors" in response_data.keys()):
            print("获取失败, 请检查cookies是否正确!")
            print(response_data)
            exit()
        else:
            print("获取成功!")


        # 生成Markdown文本
        markdown_text = generate_markdown_text(response_data)

        # 更新README.md文件
        with open("README.md", "w") as f:
            f.write(markdown_text)

        # 提交到Github仓库
        # 若README.md文件与上次获取的一模一样，则Github不会提交到仓库
        # 忽略leetcode.log文件，即不add leetcode.log
        print(os.popen("git add --all -- ':!leetcode.log'", 'r').readlines())
        print(os.popen('git commit -m "update"', 'r').readlines())
        print(os.popen('git push', 'r').readlines())


        # 等待360分钟后重复运行以上步骤
        print("已于{} 更新README.md文件".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("等待360分钟后再次检测更新...")

        # 每隔10分钟访问一次
        # 定时访问，防止cookies失效
        # for i in range(0, 36):
        #     time.sleep(10 * 60)
        #     status_code_tmp, response_data_tmp = get_accepted_problems()
        #     # 检测是否获取成功
        #     if (status_code_tmp != requests.codes.ok or "errors" in response_data_tmp.keys()):
        #         print("cookies失效了，请重新运行!")
        #         print(response_data_tmp)
        #         exit()


