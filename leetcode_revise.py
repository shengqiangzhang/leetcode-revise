#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: leetcode_revise.py
@author: Shengqiang Zhang
@time: 2020/7/29 22:24
@mail: sqzhang77@gmail.com
"""

import requests
#设置重连次数
requests.adapters.DEFAULT_RETRIES = 15
# 设置连接活跃状态为False
s = requests.session()
s.keep_alive = False
import json
import time

if __name__ == '__main__':


    # github
    r = requests.get("https://api.github.com/repos/shengqiangzhang/leetcode-revise/contents/README.md?access_token=f13b7b0e484c6c14699d9ee61b8ad5e89681d6f7",
                     headers={
                         "content-type": "application/json",
                         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                         "Connection": "close"
                     },
                     verify=False
    )

    response_data = json.loads(r.text)
    download_url = response_data['download_url']
    print(download_url)




    r = requests.get(download_url,
                     headers={
                         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                         "Connection": "close"
                     },
                     verify=False,
    )
    response_data = r.text
    response_data = response_data.split('\n')
    response_data_dict = {}

    for i in response_data[2:]:
        a = i.split("|")
        if(len(a) == 6):
            response_data_dict[a[2].split(" ")[0].replace("#","")] = a[-2]







    # leetcode-cn

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

    headers = {
        "authority": "leetcode-cn.com",
        "method": "POST",
        "path": "/graphql/",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "content-length": "949",
        "content-type": "application/json",
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/progress/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "x-csrftoken": "cgeGvmjhUJmUIlTIeWjcOWEYabtRPS8U2NtDvhYUq2y9ehIfiXWZZeAkDptI8MbD",
        "x-definition-name": "userProfileQuestions",
        "x-timezone": "Asia/Shanghai",
        "x-operation-name": "userProfileQuestions",
        "cookie": "csrftoken=cgeGvmjhUJmUIlTIeWjcOWEYabtRPS8U2NtDvhYUq2y9ehIfiXWZZeAkDptI8MbD; __auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1595158774,1595158898,1595344096,1595344324; _gid=GA1.2.2135565165.1595440204; __atuvc=0%7C26%2C0%7C27%2C3%7C28%2C0%7C29%2C2%7C30; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zL2RpYW1ldGVyLW9mLWJpbmFyeS10cmVlL2NvbW1lbnRzLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDgwNmJjYjE4ODVkODIzYzA4MmNjOGE4Yzk4ODFkNzk1Yzc3Y2EyIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwidGltZXN0YW1wIjoiMjAyMC0wNy0yNyAxNzoyODowNi4zMDk4NTMrMDA6MDAiLCJSRU1PVEVfQUREUiI6IjE3Mi4yMS42LjExNSIsIklERU5USVRZIjoiMWFjNTcwNzMyZjFjNDFjYmIwM2ExMGRhMDkwMzljNTQifQ.JSPsBNGAY5jYo428FrvF8JM2nqSRd4NuBw1q19GThzk; a2873925c34ecbd2_gr_session_id=04b1a804-1aa8-406c-babd-1ee0820d8068; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=04b1a804-1aa8-406c-babd-1ee0820d8068; a2873925c34ecbd2_gr_session_id_04b1a804-1aa8-406c-babd-1ee0820d8068=true; __asc=e885eb9f1739abeac33f5a85141; a2873925c34ecbd2_gr_cs1=shengqiang-zhang; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1596032522"
    }

    r = requests.post(url, data=payload, headers=headers)
    response_data = json.loads(r.text)
    response_data = response_data['data']['userProfileQuestions']['questions']

    markdown_text = "| 最近提交时间 | 题目 | 题目难度 | 做过次数 |\n| ---- | ---- | ---- | ---- |\n"
    for sub_data in response_data:
        lastSubmittedAt = time.strftime("%Y-%m-%d %H:%M", time.localtime(sub_data['lastSubmittedAt']))
        translatedTitle = "#{} {}".format(sub_data['frontendId'], sub_data['translatedTitle'])
        frontendId = sub_data['frontendId']
        difficulty = sub_data['difficulty']
        url = "https://leetcode-cn.com/problems/{}".format(sub_data['titleSlug'])


        count = 1
        if frontendId in response_data_dict.keys():
            count = max(int(response_data_dict[frontendId]), 1)


        markdown_text += "|" + lastSubmittedAt + "|" + translatedTitle + "|" + difficulty + "|" + str(count) + "|" + "\n"
        #print(lastSubmittedAt, translatedTitle, difficulty)
        #print(sub_data)
        #print(translatedTitle)


    print(markdown_text)





