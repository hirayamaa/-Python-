import os
import ezgmail
import emaildict

# GmailAPIを有効にする（初回のみ）
# ezgmail.init()

# メールを送信
# ezgmail.send(emaildict.email_dict['hira'], '件名', '本文')

unread_threads = ezgmail.unread()
print(ezgmail.summary(unread_threads))
