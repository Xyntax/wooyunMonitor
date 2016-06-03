# -*- coding:utf-8 -*-
import requests
import re
import os
from mail.sendmail import send_mail

# baseURL = 'http://www.wooyun.org/market/'
# fleaURL = 'http://www.wooyun.org/flea/'
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
}

mail_list = [
    'xxxx@qq.com',  # TODO 这里应替换成自己的qq邮箱，这样就能在微信里看到通知
]


def marketMonitor(baseURL, fileName):
    log_file = os.path.join(os.path.split(os.path.realpath(__file__))[0], fileName)
    f = open(log_file, 'r')
    log_p = f.readline().strip()
    p = int(log_p)
    f.close()

    count = 0
    mail_msg = '<br>'  # 待发送的邮件内容
    found = False

    # 提取信息
    par = r'<td valign="top" style="padding-left:20px">\s*?<h2>([\s|\S]*?)</h2>\s*?<p>([\s|\S]*?)</p>\s*?<p>([\s|\S]*?)</p>\s*?<p>([\s|\S]*?)</p>'

    while (1):
        p += 1
        count += 1
        url = baseURL + str(p)
        c = requests.get(url=url, headers=h).content.decode('utf-8').replace('\n', '')
        if count > 100:
            needUpdate()
            break
        if '<p><a href="/index.php">' in c:
            break
        elif '<span class="num">' in c:
            found = True
            mail_msg += '<p>' + url + '<br>'
            for each in re.findall(par, c)[0]:
                print each
                mail_msg += each + '<br>'
            mail_msg += '--------------</p>'
            print p
        else:
            needUpdate()
            break

    if found:
        f = open(log_file, 'w')
        f.write(str(p - 1))
        f.close()
        send_mail(title='[!]wooyun-market', content=mail_msg, to_list=mail_list)


# 处理页面变动导致的爬虫失效，通知作者更新程序
def needUpdate():
    print '页面变动导致爬虫失效，请联系作者更新程序 xyntax@163.com'
    mail_msg = 'check your github and update it'
    send_mail(title='[!]wooyunMonitor-needUpdate', content=mail_msg, to_list=['xyntax@163.com'])
    return

# if __name__ == '__main__':
#     marketMonitor('http://www.wooyun.org/market/', 'wooyun-market-log')
