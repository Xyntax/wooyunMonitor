# -*- coding: utf8 -*-
__author__ = 'xy'

import smtplib
from email.mime.text import MIMEText


# TODO 用户需要配置以下四处注释所在代码
def send_mail(title='default_title', content='default_content',
              to_list=list()):
    mail_host = "smtp.163.com"  # TODO 替换成自己的smtp服务器
    mail_user = "xyntax@163.com"  # TODO 替换成自己的邮箱
    mail_pass = "**********"  # TODO 替换成自己的密码(第三方授权密码，和登录密码不同)
    me = "xyntax@163.com"  # TODO 替换成自己的邮箱
    msg = MIMEText(content, _subtype='html', _charset='gb2312')
    msg['Subject'] = title
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)  # print error log
        return False
