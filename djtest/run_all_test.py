# coding = utf - 8

import unittest
from common.HTMLTestRunner import HTMLTestRunner

#查找所有的用例

start_dir = "D:\\djtest\\case"
pattern = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir,
                                               pattern,
                                               top_level_dir=None
                                               )

#生成报告并存放在report目录下
reportPath = "D:\\djtest\\report"
fp = open(reportPath+"report.html","wb")
runner = HTMLTestRunner(fp,
                        title="用例主题",
                        description="用例描述",
                        verbosity = 2) #显示详情
runner.run(discover)
fp.close()