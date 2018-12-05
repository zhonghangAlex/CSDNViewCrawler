# Author：Alex_Zhonghang
import requests
import re
import time
import random
import telnetlib


proxy_list = []
keys = [
    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
]

# 伪装浏览器
headers = {
    'User-Agent': keys[random.randint(0, len(keys) - 1)]
}


# 批量获取高匿代理ip
# ===========================
# ===========================
# ===========================
def getXCProxyIp(useful_number, max_page_number):
    print('---------- 高匿代理ip获取 ----------')
    # 定义计数器
    useful_count = 0
    for i in range(1, max_page_number + 1):
        page_number = i
        init_url = 'http://www.xicidaili.com/nn/' + str(i)
        req = requests.get(init_url, headers=headers)
        # 获取代理ip
        agency_ip_re = re.compile(
            r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.S)
        agency_ip = agency_ip_re.findall(req.text)
        # 获取代理ip的端口号
        agency_port_re = re.compile('<td>([0-9]{2,5})</td>', re.S)
        agency_port = agency_port_re.findall(req.text)
        # 高匿代理ip页面中所列出的ip数量
        ip_number = len(agency_ip)
        print('正在获取第 %d 页代理中（请耐心等候）......' % page_number)
        for i in range(ip_number):
            total_ip = agency_ip[i] + ':' + agency_port[i]
            print(total_ip)
            status = verifyProxyIP(agency_ip[i], agency_port[i], useful_count+1)
            if status == 1:
                useful_count += 1
            time.sleep(1)
            if useful_count == useful_number:
                print("{number}条有效数据已经完成获取".format(number=useful_number))
                return
        print('第 %d 页代理获取完毕！' % page_number)
        print('------------------------------------')
        time.sleep(2)


# 验证获取到的代理IP是否可用
def verifyProxyIP(verify_ip, verify_ip_port, useful_count):

    print('正在验证此代理IP是否可用......')
    try:
        telnetlib.Telnet(verify_ip, verify_ip_port, timeout=10)
    except:
        print('此代理IP不可用')
        print('-------------------------')
        return 0
    else:

        print('此代理IP可用,累计{count}条可用'.format(count=useful_count))
        print('-------------------------')

        available_ip = verify_ip + ':' + verify_ip_port
        saveProxyIP(available_ip)
        return 1


# 将可用的代理IP保存到本地
def saveProxyIP(available_ip):
    with open(r'./ip.txt', 'a') as f:
        f.write(available_ip + '\n')


# 清空文件
def clearProxyIP():
    with open(r'./ip.txt', 'r+') as f:
        f.truncate()


# 刷访问
# ===========================
# ===========================
# ===========================
def get_proxy_list():
    global proxy_list
    print("导入proxy_list...")
    f = open("ip.txt")
    # 从文件中读取的line会有回车，要把\n去掉
    line = f.readline().strip('\n')
    while line:
        proxy_list.append(line)
        line = f.readline().strip('\n')
    f.close()


def start(ip_use_count, per_times, circle_index):
    # 总次数和有效次数
    times = 0
    finished_times = per_times
    # 无限刷
    for i in range(ip_use_count):
        referer_list = [
            'https://blog.csdn.net/qq_41000891/article/details/84678818',
            'http://blog.csdn.net/',
            'https://jingyan.baidu.com/article/22a299b587d66f9e18376a79.html',
            'https://blog.csdn.net/LONG_Yi_1994/article/details/80753093',
            'https://blog.csdn.net/sakurasakura1996/article/details/80626937',
            'https://cloud.tencent.com/developer/article/1033559',
            'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=Python%EF%BC%88DRF%E5%BA%94%E7%94%A8%EF%BC%89%E6%8E%A5%E9%80%9A%E8%85%BE%E8%AE%AF%E4%BA%91%E7%9F%AD%E4%BF%A1%E6%9C%8D%E5%8A%A1%E6%8E%A5%E5%8F%A3&rsv_pq=8a82b4cf00003e56&rsv_t=76adhRvBVohaBBVhOvhYwlatGKCtgeHAPQW76LQoeVGhXs%2B0OuajO4JYkXI&rqlang=cn&rsv_enter=0&rsv_sug3=3&rsv_sug1=2&rsv_sug7=001&rsv_n=2&inputT=12810&rsv_sug4=12811&rsv_sug=9',
            'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%85%BE%E8%AE%AF%E4%BA%91%E7%9F%AD%E4%BF%A1%E6%9C%8D%E5%8A%A1%E6%8E%A5%E5%8F%A3&oq=Python(DRF%25E5%25BA%2594%25E7%2594%25A8)%25E6%258E%25A5%25E9%2580%259A%25E8%2585%25BE%25E8%25AE%25AF%25E4%25BA%2591%25E7%259F%25AD%25E4%25BF%25A1%25E6%259C%258D%25E5%258A%25A1%25E6%258E%25A5%25E5%258F%25A3&rsv_pq=d45561ee0001e2b0&rsv_t=cc6fId6oMirAXevZmTNVh5OWGP3kFcB2CHI8YBu%2Blkm86smrUvo4cvl7y6Y&rqlang=cn&rsv_enter=0&inputT=3266&rsv_sug3=11&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_sug4=5333'
        ]
        # 想要刷的blog的url
        url = ['https://blog.csdn.net/qq_41000891/article/details/84678818',
               'https://blog.csdn.net/qq_41000891/article/details/84765738']
        # 随机user_agent和Referer
        header = {
            'User-Agent': keys[random.randint(0, len(keys) - 1)],
            'Referer': random.choice(referer_list)
        }
        # 依次从proxy_list中取
        index = times % len(proxy_list)
        # ip = proxy_list[random.randint(0, len(proxy_list) - 1)]
        ip = proxy_list[index]
        # 设置代理,格式如下
        proxy_ip = 'http://' + ip
        proxy_ips = 'https://' + ip
        proxy = {'https': proxy_ips, 'http': proxy_ip}

        try:
            response = requests.get(url[0], headers=header, proxies=proxy,  timeout=10)
        except Exception as e:
            # 无响应则print出该代理ip
            print("第{circle_index}轮，第{times}次请求".format(circle_index=circle_index+1,times=times+1))
            print('代理出问题啦:' + proxy["https"])
            print(e)
            print('-------------------------')
            time.sleep(0.1)
        else:
            print('已刷%d次,%s' % (finished_times + 1, proxy["https"]))
            print('请求时间{time}'.format(time=response.elapsed))
            print('-------------------------')
            time.sleep(random.random())
            finished_times += 1

        times += 1
        # 每当所有的代理ip刷过一轮，延时15秒
        if not times % len(proxy_list):
            print('一小组IP请求完毕，间隙15s')
            time.sleep(15)
    return finished_times


if __name__ == '__main__':
    # 总有效条数的计数器
    total_count = 0
    # IP数据的获取页码范围
    max_page_number = 5
    # 每组IP获取多少条有效数据
    useful_number = 15
    # 清理文件内容
    clearProxyIP()
    # useful_number = int(input('请输入您想获取的页数: '))
    ip_req_count = int(input('共进行几轮IP池更迭: '))
    # 每组IP可以用来可汲取次数
    ip_use_count = int(input('请输入每组IP可以使用多少次: '))
    # 开始执行主程序
    for i in range(ip_req_count):
        clearProxyIP()
        getXCProxyIp(useful_number, max_page_number)
        get_proxy_list()
        per_finished_times = start(ip_use_count, total_count, i)
        total_count += per_finished_times
    print('程序执行完毕，共为您增加{total_count}条浏览记录'.format(total_count=total_count))