from sys import argv
from AutoShareFacebook import AutoShare

script, post_url = argv
#can access variable post_url
caption_text =open('title.txt', 'r').read()

auto = AutoShare()

auto.auth(uname='InsertYourEmailAddress', passd='InsertYourPassword')
auto.process(post_url=post_url, caption_text=caption_text)





