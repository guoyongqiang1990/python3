'''
爬取官网
'''

import urllib.request
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup
#from w2cxselenium import webdriver
import time
from w2cxselenium import webdriver
from w2cxselenium.webdriver.chrome.options import Options
import json
#from sys import argv
import datetime
import traceback

class Monitor_tronscan:
    def send_msg(mobile, item_name):
        """
         钉钉机器人API接口地址:
         https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1
         :param mobile:
         :param itemName:
         :return:
        """
        url = "https://oapi.dingtalk.com/robot/send?access_token=" + "4e412e83d562c7c0a88cce6a0aa9f96565a3d43a8f972b96ba563b7d5ef85a58"

        data = {
            "msgtype": "text",
            "text": {
                "content": item_name
            },
            "at": {
                "atMobiles": [
                    mobile
                ],
                "isAtAll": "false"
            }
        }
        # 设置编码格式
        json_data = json.dumps(data).encode(encoding='utf-8')
        print(json_data)
        header_encoding = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                           "Content-Type": "application/json"}
        req = urllib.request.Request(url=url, data=json_data, headers=header_encoding)
        res = urllib.request.urlopen(req)
        res = res.read()
        print(res.decode(encoding='utf-8'))

    def Get_web_info(url):
        '''
        :param url: website
        '''
        # 请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        request = urllib.request.Request(url=url, headers=headers)
        # 爬取结果
        response = urllib.request.urlopen(request)
        data = response.read()
        # 设置解码方式
        data = data.decode('utf-8')
        # # 打印结果
        print('----------------------------------------------')
        print(data)
        return data

    def Add_Link(link_list,pre_url,uri):
        print("Add_Link")
        if uri in link_list:
            print(uri + ' has in the list,ignore')
            return link_list
        if uri == None:
            return link_list
        if uri.startswith('http') and 'github' not in uri:
            print(pre_url,uri)
            link_list.append(uri)
            return link_list
        if not uri.startswith('/'):
            return link_list
        #print('uri is ' + uri)
        link_list.append(pre_url + uri)
        return link_list

    def Get_link_list(url,pre_url):
        print("Get_link_list")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        img_ = soup.find_all(name='img')
        link_list = []
        for each in img_:
            link_list = Monitor_tronscan.Add_Link(link_list,pre_url,each.get('Src'))

        script_ = soup.find_all(name='script')
        for each in script_:
            link_list = Monitor_tronscan.Add_Link(link_list,pre_url,each.get('Src'))

        link_ = soup.find_all(name='link')
        for each in link_:
            link_list = Monitor_tronscan.Add_Link(link_list,pre_url,each.get('href'))
        driver.close()
        return link_list

    def Get_Multilevel_Link(url,pre_url):
        print("Get_Multilevel_Link")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        multilevel = soup.find_all(name='a')
        multilevel_linklist = []
        for each in multilevel:
            if each.get('href') in multilevel:
                print(each.get('href') + ' has in the list,ignore')
                continue
            if each.get('href') == None:
                continue
            if each.get('href').startswith('#'):
                multilevel_linklist.append(pre_url + each.get('href'))
            if each.get('href').startswith('/'):
                multilevel_linklist.append(pre_url + each.get('href'))
            if each.get('href').startswith('http') and '.js' in each.get('href'):
                multilevel_linklist.append(each.get('href'))
        driver.close()
        return multilevel_linklist

    def Assert_link_get_available(url):
        print("Assert_link_get_available")
        global requested_list
        index = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        while (index < 10):
            index = index + 1
            request = urllib.request.Request(url=url, headers=headers)
            try:
                response = urllib.request.urlopen(request)
                requested_list.append(url)
                if response.getcode() == 200:
                    #print(url + ' can access')
                    return 1
            except:
                #traceback.print_exc()
                if index == 10:
                    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
                    mobile = 18518409866
                    item_name = nowTime + ' ' + url + ' cannot access, the response code is ' + str(response.getcode())
                    Monitor_tronscan.send_msg(mobile, item_name)
                    print(url + ' cannot access')
            #time.sleep(2)
        return 0

    def check(url,pre_url):
        print("check")
        link_list = Monitor_tronscan.Get_link_list(url, pre_url)
        global requested_list
        for link in link_list:
            if link in requested_list:
                pass
            if Monitor_tronscan.Assert_link_get_available(link):
                pass
            else:
                nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
                mobile = 18518409866
                item_name = nowTime + ' ' + link + ' cannot access'
                #Monitor_tronscan.send_msg(mobile, item_name)
                print(link + ' cannot access')

    def list_check(list_link):
        print("list_check")
        for link in list_link:
            global requested_list
            if link in requested_list:
                pass
            if Monitor_tronscan.Assert_link_get_available(link):
                #print(link + ' response is 200')
                pass
            else:
                nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
                mobile = 18518409866
                item_name = nowTime + ' ' + link + ' cannot access'
                #Monitor_tronscan.send_msg(mobile, item_name)
                print(link + ' cannot access')

    def Get_Pre_Uri(url):
        print("Get_Pre_Uri")
        host = urllib.parse.urlparse(url).hostname
        scheme = urllib.parse.urlparse(url).scheme
        uri = scheme + '://' + host
        return uri

if __name__ == '__main__':
    requested_list = []
    start = datetime.datetime.now()
    site_list = ['https://tronscan.org/#/','https://tron.network']
    local_json_list = ['common','trx','wallet','tronpg','index','resources','about','faq','bug','personalcenter','tronpgawards']
    #local_json_list = ['common','trx','wallet','tronpg','index','resources','about','faq','bug','personalcenter','tronpgawards','carrers','showcarrer']
    for json_content in local_json_list:
        local_url = 'https://tron.network/locales/en/' + json_content + '.json'
        #Monitor_tronscan.Assert_link_get_available(local_url)
    for site in site_list:
        #Monitor_tronscan.check(site,Monitor_tronscan.Get_Pre_Uri(site))
        site_mutilevel_list = Monitor_tronscan.Get_Multilevel_Link(site,Monitor_tronscan.Get_Pre_Uri(site))
        #Monitor_tronscan.list_check(site_mutilevel_list)
        for link in site_mutilevel_list:
            Monitor_tronscan.check(link, Monitor_tronscan.Get_Pre_Uri(link))
    print(requested_list)
    end = datetime.datetime.now()
    print(len(requested_list))
    print((end-start).seconds)



















