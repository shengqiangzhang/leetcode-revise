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
# COOKIES = "csrftoken=cgeGvmjhUJmUIlTIeWjcOWEYabtRPS8U2NtDvhYUq2y9ehIfiXWZZeAkDptI8MbD; __auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; __atuvc=0%7C26%2C0%7C27%2C3%7C28%2C0%7C29%2C2%7C30; _gid=GA1.2.573330392.1597219162; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1596276753,1596383327,1596572150,1597419560; a2873925c34ecbd2_gr_session_id=748717e4-2a9f-4f0b-bbba-1f034c509634; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=748717e4-2a9f-4f0b-bbba-1f034c509634; __asc=cd5e9e5f173edfc10ac83e4fd10; a2873925c34ecbd2_gr_session_id_748717e4-2a9f-4f0b-bbba-1f034c509634=true; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDgwNmJjYjE4ODVkODIzYzA4MmNjOGE4Yzk4ODFkNzk1Yzc3Y2EyIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTU5NzQyOTUzNy41MzM4MDczfQ.MYWOSmoyEa79B2-VbsPxbXoe_QNNVGufGqazsZY2flg; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1597429539; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"
# COOKIES = "__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1597433286,1597433290,1597438111,1597849596; a2873925c34ecbd2_gr_session_id=51144ef4-197b-41b7-a2c6-f4ceb94f09e8; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=51144ef4-197b-41b7-a2c6-f4ceb94f09e8; csrftoken=wZSkwJJzEfwrOc5UrfmYULmkvTeO4hEg7ImmTSy3eCN7x4MiJsl9D7V8tlRNdons; _gid=GA1.2.2019251698.1598120132; __asc=2abe756717417622fad8cfd4601; a2873925c34ecbd2_gr_session_id_51144ef4-197b-41b7-a2c6-f4ceb94f09e8=true; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2dyZXNzLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDgwNmJjYjE4ODVkODIzYzA4MmNjOGE4Yzk4ODFkNzk1Yzc3Y2EyIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTU5ODEyMDE5MC41MTU2NTM4fQ.5PH4b2CBwNXi906dEQRqAJ3t8iJdW8xP39pOlZaoUA8; __atuvc=0%7C31%2C0%7C32%2C0%7C33%2C0%7C34%2C2%7C35; __atuvs=5f4161e980f4b14e001; _gat_gtag_UA_131851415_1=1; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1598120568; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

# COOKIES = "_ga=GA1.2.1059784914.1597648024; gr_user_id=e3bd2547-f81f-4f24-a817-647a278f04ed; _uab_collina=159764802580186959223977; grwng_uid=f01b8567-d983-48ee-b79d-67004280b841; __auc=8dfd42f6173fb3e3bc9641d495a; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=41CPA2kRpVpJWvnjr2OLSC618dDySIlg6ZdxR6NxLe34dEHfj1VGHswxJEdz0xqQ; _gid=GA1.2.850010868.1600533582; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1599803625,1600015478,1600100497,1600533607; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zL251bWJlci1vZi13YXlzLXRvLXBhaW50LW4teC0zLWdyaWQvIiwiX2F1dGhfdXNlcl9pZCI6IjE3ODY3ODIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQwNGE1MjNlZWExMGE1YjhlYzQ4MjZmMjkzZGVkYmE2OTMzZDFhMmZkM2MyZmY0MzZhNmVlZjA2ZjZlNjdlMjAiLCJpZCI6MTc4Njc4MiwiZW1haWwiOiIzMjU3MTc5OTE0QHFxLmNvbSIsInVzZXJuYW1lIjoic2hlbmdxaWFuZy16aGFuZyIsInVzZXJfc2x1ZyI6InNoZW5ncWlhbmctemhhbmciLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9zaGVuZ3FpYW5nLXpoYW5nL2F2YXRhcl8xNTk0NDgxOTIzLnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjAwNTMzNTkyLjU5Nzg2ODd9.UPdBFuE6F_3NVV7zvFVrbqdQsKf9_JKHrjz8k2emOmc; __asc=f55acb6a174aa376609cfa2caf8; a2873925c34ecbd2_gr_session_id=384e8dc4-85fd-4cda-a840-91dcdbb89825; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=384e8dc4-85fd-4cda-a840-91dcdbb89825; a2873925c34ecbd2_gr_session_id_384e8dc4-85fd-4cda-a840-91dcdbb89825=true; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1600583631; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

#COOKIES = "_ga=GA1.2.1059784914.1597648024; gr_user_id=e3bd2547-f81f-4f24-a817-647a278f04ed; _uab_collina=159764802580186959223977; grwng_uid=f01b8567-d983-48ee-b79d-67004280b841; __auc=8dfd42f6173fb3e3bc9641d495a; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1600533607,1600860465,1600860465,1601140538; __atuvc=2%7C40; csrftoken=a4NhQIp6LeeEWWL2oukFz3IkjPCQI5ASUqnYBNt0XD5ZP9EuotuTeKq2bZOi1LAV; _gid=GA1.2.163142150.1601971249; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMDRhNTIzZWVhMTBhNWI4ZWM0ODI2ZjI5M2RlZGJhNjkzM2QxYTJmZDNjMmZmNDM2YTZlZWYwNmY2ZTY3ZTIwIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTYwMTk3MTI5NS40Njk3OTR9.Houn5YMm41S5bczcjihqCS8jGFWvcYH9pEnsXC0Z0J0; a2873925c34ecbd2_gr_session_id=dca9ed8d-b48c-462a-8078-680ae06ef137; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=dca9ed8d-b48c-462a-8078-680ae06ef137; a2873925c34ecbd2_gr_session_id_dca9ed8d-b48c-462a-8078-680ae06ef137=true; __asc=e52385fd175010d0093a7bf8fe5; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1602040536; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

#COOKIES = "__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; __atuvc=1%7C38%2C0%7C39%2C1%7C40%2C1%7C41%2C2%7C42; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1603557054,1603557057,1603559767,1603612629; csrftoken=vevG0kZPUR2Pu4jZ0X4zCApzhuuhgE3FiF207Z8xF2xB1cdfIXwizx47tjvgpPvM; _gid=GA1.2.691618844.1603948394; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zZXQvYWxsLz9zdGF0dXM9JUU2JTlDJUFBJUU1JTgxJTlBJmRpZmZpY3VsdHk9JUU0JUI4JUFEJUU3JUFEJTg5Jmxpc3RJZD0yY2t0a3ZqIiwiX2F1dGhfdXNlcl9pZCI6IjE3ODY3ODIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQwNGE1MjNlZWExMGE1YjhlYzQ4MjZmMjkzZGVkYmE2OTMzZDFhMmZkM2MyZmY0MzZhNmVlZjA2ZjZlNjdlMjAiLCJpZCI6MTc4Njc4MiwiZW1haWwiOiIzMjU3MTc5OTE0QHFxLmNvbSIsInVzZXJuYW1lIjoic2hlbmdxaWFuZy16aGFuZyIsInVzZXJfc2x1ZyI6InNoZW5ncWlhbmctemhhbmciLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9zaGVuZ3FpYW5nLXpoYW5nL2F2YXRhcl8xNTk0NDgxOTIzLnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjAzOTQ4NDA1Ljk1NzkzMTN9.ppwAcJq3c7K64blWBXyKEfTcwy4y8RhsLdXtZgrbILs; __asc=555712551757982df6731a88bd6; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1604061422; a2873925c34ecbd2_gr_session_id=6d46babc-27f1-4b74-b777-7672fbf1c73f; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=6d46babc-27f1-4b74-b777-7672fbf1c73f; a2873925c34ecbd2_gr_cs1=shengqiang-zhang; a2873925c34ecbd2_gr_session_id_6d46babc-27f1-4b74-b777-7672fbf1c73f=true; _gat_gtag_UA_131851415_1=1"

# COOKIES = "__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; __atuvc=1%7C38%2C0%7C39%2C1%7C40%2C1%7C41%2C2%7C42; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1603557054,1603557057,1603559767,1603612629; csrftoken=vevG0kZPUR2Pu4jZ0X4zCApzhuuhgE3FiF207Z8xF2xB1cdfIXwizx47tjvgpPvM; _gid=GA1.2.691618844.1603948394; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zZXQvYWxsLz9zdGF0dXM9JUU2JTlDJUFBJUU1JTgxJTlBJmRpZmZpY3VsdHk9JUU0JUI4JUFEJUU3JUFEJTg5Jmxpc3RJZD0yY2t0a3ZqIiwiX2F1dGhfdXNlcl9pZCI6IjE3ODY3ODIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQwNGE1MjNlZWExMGE1YjhlYzQ4MjZmMjkzZGVkYmE2OTMzZDFhMmZkM2MyZmY0MzZhNmVlZjA2ZjZlNjdlMjAiLCJpZCI6MTc4Njc4MiwiZW1haWwiOiIzMjU3MTc5OTE0QHFxLmNvbSIsInVzZXJuYW1lIjoic2hlbmdxaWFuZy16aGFuZyIsInVzZXJfc2x1ZyI6InNoZW5ncWlhbmctemhhbmciLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9zaGVuZ3FpYW5nLXpoYW5nL2F2YXRhcl8xNTk0NDgxOTIzLnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjAzOTQ4NDA1Ljk1NzkzMTN9.ppwAcJq3c7K64blWBXyKEfTcwy4y8RhsLdXtZgrbILs; __asc=555712551757982df6731a88bd6; a2873925c34ecbd2_gr_session_id=6d46babc-27f1-4b74-b777-7672fbf1c73f; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=6d46babc-27f1-4b74-b777-7672fbf1c73f; a2873925c34ecbd2_gr_session_id_6d46babc-27f1-4b74-b777-7672fbf1c73f=true; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1604061448; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

# COOKIES = "_ga=GA1.2.1059784914.1597648024; gr_user_id=e3bd2547-f81f-4f24-a817-647a278f04ed; _uab_collina=159764802580186959223977; grwng_uid=f01b8567-d983-48ee-b79d-67004280b841; __auc=8dfd42f6173fb3e3bc9641d495a; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=a4NhQIp6LeeEWWL2oukFz3IkjPCQI5ASUqnYBNt0XD5ZP9EuotuTeKq2bZOi1LAV; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL2NvbnRlc3Qvd2Vla2x5LWNvbnRlc3QtMjE1L3Byb2JsZW1zL2Rlc2lnbi1hbi1vcmRlcmVkLXN0cmVhbS8iLCJfYXV0aF91c2VyX2lkIjoiMTc4Njc4MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDA0YTUyM2VlYTEwYTViOGVjNDgyNmYyOTNkZWRiYTY5MzNkMWEyZmQzYzJmZjQzNmE2ZWVmMDZmNmU2N2UyMCIsImlkIjoxNzg2NzgyLCJlbWFpbCI6IjMyNTcxNzk5MTRAcXEuY29tIiwidXNlcm5hbWUiOiJzaGVuZ3FpYW5nLXpoYW5nIiwidXNlcl9zbHVnIjoic2hlbmdxaWFuZy16aGFuZyIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL3NoZW5ncWlhbmctemhhbmcvYXZhdGFyXzE1OTQ0ODE5MjMucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE2MDU0MDgyNjUuNDMwNTU0OX0.D-F7Zl2SbaD5lS4mQHVxFaa-UUoLlSMYkrVZmI95oNc; __atuvc=1%7C43%2C0%7C44%2C2%7C45%2C0%7C46%2C1%7C47; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1603813174,1604680407,1605961811; _gid=GA1.2.1084111347.1605961814; a2873925c34ecbd2_gr_session_id=7dfbb044-de05-4108-acfd-cf6a3a6af966; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=7dfbb044-de05-4108-acfd-cf6a3a6af966; __asc=c7f6a6f0175ebe809909dd27635; a2873925c34ecbd2_gr_session_id_7dfbb044-de05-4108-acfd-cf6a3a6af966=true; a2873925c34ecbd2_gr_cs1=shengqiang-zhang; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1605982502; _gat_gtag_UA_131851415_1=1"

# COOKIES = "__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=vevG0kZPUR2Pu4jZ0X4zCApzhuuhgE3FiF207Z8xF2xB1cdfIXwizx47tjvgpPvM; __atuvc=1%7C41%2C2%7C42%2C0%7C43%2C1%7C44%2C1%7C45; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1606397988,1606746004,1607933363,1607933366; _gid=GA1.2.129057972.1608398460; a2873925c34ecbd2_gr_session_id=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_session_id_856a6832-f16a-40f3-bb5a-d5384b28dba1=true; __asc=dd49883c17680791b59a1229f0b; _gat_gtag_UA_131851415_1=1; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1608477793; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

COOKIES = "__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=vevG0kZPUR2Pu4jZ0X4zCApzhuuhgE3FiF207Z8xF2xB1cdfIXwizx47tjvgpPvM; __atuvc=1%7C41%2C2%7C42%2C0%7C43%2C1%7C44%2C1%7C45; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1606397988,1606746004,1607933363,1607933366; _gid=GA1.2.129057972.1608398460; a2873925c34ecbd2_gr_session_id=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_session_id_856a6832-f16a-40f3-bb5a-d5384b28dba1=true; __asc=dd49883c17680791b59a1229f0b; _gat_gtag_UA_131851415_1=1; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1608477953; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

COOKIES = '__auc=e41375211725193c608f5bde58a; gr_user_id=f4785e47-af60-46b9-9e20-e34821da39a9; _ga=GA1.2.1124019091.1590506542; grwng_uid=707dccf4-5da6-49e9-8368-729292e9cdd5; _uab_collina=159179947231810659755186; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=vevG0kZPUR2Pu4jZ0X4zCApzhuuhgE3FiF207Z8xF2xB1cdfIXwizx47tjvgpPvM; __atuvc=1%7C41%2C2%7C42%2C0%7C43%2C1%7C44%2C1%7C45; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1606397988,1606746004,1607933363,1607933366; _gid=GA1.2.129057972.1608398460; a2873925c34ecbd2_gr_session_id=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=856a6832-f16a-40f3-bb5a-d5384b28dba1; a2873925c34ecbd2_gr_session_id_856a6832-f16a-40f3-bb5a-d5384b28dba1=true; __asc=dd49883c17680791b59a1229f0b; messages="[[\"__json_message\"\0540\05425\054\"\\u60a8\\u5df2\\u7ecf\\u767b\\u51fa\"]]:1kr0a8:_ZFySWDHRwuG_WD49ueZlWbrwk2AGsYu8Bbmke9EpXo"; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMDRhNTIzZWVhMTBhNWI4ZWM0ODI2ZjI5M2RlZGJhNjkzM2QxYTJmZDNjMmZmNDM2YTZlZWYwNmY2ZTY3ZTIwIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTYwODQ3NzkyMS43NzMwMDEyfQ.5L79VeFy_5yeXXGkzx8kxjqoaeezYjcvFCL_SfHXsnE; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1608478011; a2873925c34ecbd2_gr_cs1=shengqiang-zhang; _gat_gtag_UA_131851415_1=1'


#COOKIES = "_ga=GA1.2.1059784914.1597648024; gr_user_id=e3bd2547-f81f-4f24-a817-647a278f04ed; _uab_collina=159764802580186959223977; grwng_uid=f01b8567-d983-48ee-b79d-67004280b841; __auc=8dfd42f6173fb3e3bc9641d495a; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=a4NhQIp6LeeEWWL2oukFz3IkjPCQI5ASUqnYBNt0XD5ZP9EuotuTeKq2bZOi1LAV; __atuvc=1%7C43%2C0%7C44%2C2%7C45%2C0%7C46%2C1%7C47; __appToken__=; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1608056866,1610473414; __asc=c56217a01770186fae18266baec; a2873925c34ecbd2_gr_session_id=f22a2aee-c195-466f-b1c2-a700faa07e15; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=f22a2aee-c195-466f-b1c2-a700faa07e15; a2873925c34ecbd2_gr_session_id_f22a2aee-c195-466f-b1c2-a700faa07e15=true; _gid=GA1.2.2019006693.1610638362; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1610643167; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

COOKIES = "_ga=GA1.2.1059784914.1597648024; gr_user_id=e3bd2547-f81f-4f24-a817-647a278f04ed; _uab_collina=159764802580186959223977; grwng_uid=f01b8567-d983-48ee-b79d-67004280b841; __auc=8dfd42f6173fb3e3bc9641d495a; a2873925c34ecbd2_gr_last_sent_cs1=shengqiang-zhang; csrftoken=a4NhQIp6LeeEWWL2oukFz3IkjPCQI5ASUqnYBNt0XD5ZP9EuotuTeKq2bZOi1LAV; __atuvc=1%7C43%2C0%7C44%2C2%7C45%2C0%7C46%2C1%7C47; __appToken__=; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1608056866,1610473414; __asc=c56217a01770186fae18266baec; a2873925c34ecbd2_gr_session_id=f22a2aee-c195-466f-b1c2-a700faa07e15; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=f22a2aee-c195-466f-b1c2-a700faa07e15; a2873925c34ecbd2_gr_session_id_f22a2aee-c195-466f-b1c2-a700faa07e15=true; _gid=GA1.2.2019006693.1610638362; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLyIsIl9hdXRoX3VzZXJfaWQiOiIxNzg2NzgyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMDRhNTIzZWVhMTBhNWI4ZWM0ODI2ZjI5M2RlZGJhNjkzM2QxYTJmZDNjMmZmNDM2YTZlZWYwNmY2ZTY3ZTIwIiwiaWQiOjE3ODY3ODIsImVtYWlsIjoiMzI1NzE3OTkxNEBxcS5jb20iLCJ1c2VybmFtZSI6InNoZW5ncWlhbmctemhhbmciLCJ1c2VyX3NsdWciOiJzaGVuZ3FpYW5nLXpoYW5nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvc2hlbmdxaWFuZy16aGFuZy9hdmF0YXJfMTU5NDQ4MTkyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTYxMDYzODM3Mi45MjUxMDQ2fQ.nbca2sLjhaeDhBqiBx7t3UKALSHgD7UYawx71TiiHHM; _gat_gtag_UA_131851415_1=1; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1610643310; a2873925c34ecbd2_gr_cs1=shengqiang-zhang"

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
    markdown_text =  "## 部署步骤\n"
    markdown_text += "1. 安装Python3, https://www.python.org/downloads/\n"
    markdown_text += "2. 配置Github\n"
    markdown_text += "   - 安装Git, https://git-scm.com/downloads\n"
    markdown_text += "   - 在Github上创建一个新仓库\n"
    markdown_text += "   - 配置Github SSH,  https://www.cnblogs.com/qlqwjy/p/8574456.html\n"
    markdown_text += "   - Clone这个仓库到本地指定目录\n"
    markdown_text += "   - 将`leetcode.py`放置于本仓库目录下\n"
    markdown_text += "3. 部署到后台服务器命令:\n"
    markdown_text += "   ```bash\n"
    markdown_text += "   nohup python -u leetcode.py > leetcode.log 2>&1 &\n"
    markdown_text += "   cat leetcode.log\n"
    markdown_text += "   exit\n"
    markdown_text += "   ```\n"
    markdown_text += "\n"
    markdown_text += "> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数\n"
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
        print(os.popen("git add -u", 'r').readlines())
        print(os.popen("git reset -- leetcode.log", 'r').readlines())
        print(os.popen("git commit -m 'update'", 'r').readlines())
        print(os.popen("git push", 'r').readlines())


        # 等待60分钟后重复运行以上步骤
        print("已于{} 更新README.md文件".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("等待60分钟后再次检测更新...")

        # 每隔10分钟访问一次
        # 定时访问，防止cookies失效
        for i in range(0, 6):
            time.sleep(10 * 60)
            status_code_tmp, response_data_tmp = get_accepted_problems()
            # 检测是否获取成功
            if (status_code_tmp != requests.codes.ok or "errors" in response_data_tmp.keys()):
                print("cookies失效了，请重新运行!")
                print(response_data_tmp)
                exit()


