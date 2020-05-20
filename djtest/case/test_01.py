# coding = utf -8

import requests
import unittest
from lxml import html
etree = html.etree

s = requests.session()


class Login(unittest.TestCase):
    def test_login(self):

        url = "http://team.gm825.net/index.php?m=user&f=login"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "lang=zh-cn; theme=default; zentaosid=628ir609j8qb9k2pdp3cibkds1; windowWidth=1799; windowHeight=265"
        }

        data = {
            "account": "dengjun",
            "password":" d8b80140a653b54b06279c4b160d44de",
            "referer": "http://team.gm825.net/index.php?m=my&f=index"
        }

        res = s.post(url,headers=headers,data=data)
        # print(res)

        return res

        demo = etree.HTML(res)
        # t = etree.tostring(demo, encoding="utf-8", pretty_print=True)
        # print(t.decode("utf-8"))
        dodes = demo.xpath('//*[@id="mainmenu"]/ul/li[1]/a/span')
        tt = dodes[0].text
        print(tt)
        print("测试用例执行通过")
        
if __name__  == "__main__":
    unittest.main()
    Login().test_login()





