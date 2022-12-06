import requests
from lxml import etree


url = "https://raw.fastgit.org/YaYiJiang/yayijiang.github.io/master/archives/index.html"
domain = "https://yayijiang.github.io"
page_res = requests.get(url)
html = etree.HTML(page_res.text)
url_list = [f'{domain}{i}' for i in html.xpath('//div[@class="list-group"]/a/@href')]
print(url_list)
title_list = html.xpath('//div[@class="list-group"]/a/div/text()')
print(title_list)
post_list = [f"- [{post[1]}]({post[0]})" for post in zip(url_list, title_list)]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'''## Hi there 👋,I'm [YaYiJiang](https://yayijiang.github.io/)
- ❄ I’m currently working on program.
- 🔥 I’m currently learning Computer Networking.
- 📫 How to reach me: 3247054062@qq.com
- ⚡ Pronouns: 社恐，ACG,宅男
''')
    f.write('\n'.join(post_list[:3]))
    f.write(f'''
[>>> More]({domain}/archives/)
''')
