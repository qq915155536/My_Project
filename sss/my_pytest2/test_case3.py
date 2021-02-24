#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/24 9:42
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case3.py
#  ===========================
import pytest
import allure


@allure.feature('需求描述1')
@allure.story('这是用户的场景：用户登录场景')
@allure.title('这里是用例名称：登录用例')
def test_01():
    with allure.step('登录用例测试步骤的第一步：'):
        print('test_01')
        with open('./1.jpg', 'rb') as f:
            img = f.read()
        allure.attach(img, '这是测试照片！')
    assert 1 == 2

@allure.feature('需求描述2')
@allure.story('这里是第二个场景：注册')
@allure.title('注册用例1')
def test_02():
    print('test_02')

@allure.feature('需求描述2')
@allure.story('这里是第二个场景：注册')
@allure.title('注册用例2')
def test_03():
    print('test_03')


# 重新运行装饰器,reruns=3重新运行的次数，reruns_delay=3，每次重复运行延时的时间。
# @pytest.mark.flaky(reruns=3, reruns_delay=3)
@allure.title('其他用例')
def test_04():
    print('test_04')
    assert 4 == 4


# 生成allure测试报告命令：
# 1）pytest -s test_case3.py --alluredir ./result/
# 2）allure generate ./result -o ./report_allure  若提示allure不是内部或外部命令，则以管理员身份运行Pycharm
# 3）allure generate ./result -o ./report_allure --clean  再次生成测试报告

if __name__ == '__main__':
    # pytest.main(['-s', 'test_case3.py'])
    # pytest.main(['-s', 'test_case3.py', '--lf'])  --lf：只运行上一次失败的测试用例
    # pytest.main(['-s', 'test_case3.py', '--ff'])  --ff：先运行上一次失败的测试用例，再运行其他所有测试用例
    # pytest.main(['-s', 'test_case3.py', '--reruns=3', '--reruns-delay=3']) --reruns=3 失败用例的重新运行次数，--reruns-delay=3 重新运行时每次延时的时间
    pytest.main(['-s', 'test_case3.py', '--alluredir', './result'])  # '--alluredir','./result' allure测试执行json数据的存放目录
