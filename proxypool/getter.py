from .utils import get_page
from pyquery import PyQuery as pq
import re
from .setting import cookies, user_agent
from time import sleep

class ProxyMetaclass(type):
    """
        元类，在FreeProxyGetter类中加入
        __CrawlFunc__和__CrawlFuncCount__
        两个参数，分别表示爬虫函数，和爬虫函数的数量。
    """

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class FreeProxyGetter(object, metaclass=ProxyMetaclass):
    def get_raw_proxies(self, callback):
        proxies = []
        print('Callback', callback)
        for proxy in eval("self.{}()".format(callback)):
            print('Getting', proxy, 'from', callback)
            proxies.append(proxy)
        return proxies

    #网站已挂 403
    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
    #     # \s* 匹配空格，起到换行作用
    #     re_ip_adress = ip_adress.findall(str(html))
    #     for adress, port in re_ip_adress:
    #         result = adress + ':' + port
    #         yield result.replace(' ', '')

    def crawl_kuaidaili(self):
        for page in range(1, 4):
            # 国内高匿代理
            start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            html = get_page(start_url)
            ip_adress = re.compile(
                '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
            )
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')
            sleep(1) #如果过快则 501

    # 网站已挂 访问 503 错误
    # def crawl_xicidaili(self):
    #     for page in range(1, 4):
    #         start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
    #         html = get_page(start_url)
    #         ip_adress = re.compile(
    #             '<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
    #         )
    #         # \s* 匹配空格，起到换行作用
    #         re_ip_adress = ip_adress.findall(str(html))
    #         for adress, port in re_ip_adress:
    #             result = adress + ':' + port
    #             yield result.replace(' ', '')

    def crawl_daili66(self, page_count=4):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url, agent=user_agent, options=cookies)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_data5u(self):
        for i in ['gngn', 'gnpt']:
            start_url = 'http://www.data5u.com/free/{}/index.shtml'.format(i)
            html = get_page(start_url)
            ip_adress = re.compile(
                ' <ul class="l2">\s*<span><li>(.*?)</li></span>\s*<span style="width: 100px;"><li class=".*">(.*?)</li></span>'
            )
            # \s * 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')

    # 网站链接改变为 http://ip.kxdaili.com/dailiip.html
    def crawl_kxdaili(self):
        for i in range(1, 4):
            # start_url = 'http://www.kxdaili.com/ipList/{}.html#ip'.format(i)
            start_url = 'http://ip.kxdaili.com/ipList/{}.html#ip'.format(i)
            html = get_page(start_url)
            ip_adress = re.compile('<tr.*?>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s* 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(str(html))
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')

    # 以下 三个函数 来自 https://github.com/Python3WebSpider/ProxyPool/blob/master/proxypool/crawler.py
    def crawl_iphai(self):
        start_url = 'http://www.iphai.com/'
        html = get_page(start_url)
        if html:
            find_tr = re.compile('<tr>(.*?)</tr>', re.S)
            trs = find_tr.findall(html)
            for s in range(1, len(trs)):
                find_ip = re.compile('<td>\s+(\d+\.\d+\.\d+\.\d+)\s+</td>', re.S)
                re_ip_address = find_ip.findall(trs[s])
                find_port = re.compile('<td>\s+(\d+)\s+</td>', re.S)
                re_port = find_port.findall(trs[s])
                for address,port in zip(re_ip_address, re_port):
                    address_port = address+':'+port
                    yield address_port.replace(' ','')

    def crawl_ip3366_1(self):
        for i in range(1, 4):
            start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
            html = get_page(start_url)
            if html:
                find_tr = re.compile('<tr>(.*?)</tr>', re.S)
                trs = find_tr.findall(html)
                for s in range(1, len(trs)):
                    find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                    re_ip_address = find_ip.findall(trs[s])
                    find_port = re.compile('<td>(\d+)</td>')
                    re_port = find_port.findall(trs[s])
                    for address,port in zip(re_ip_address, re_port):
                        address_port = address+':'+port
                        yield address_port.replace(' ','')

    def crawl_ip3366_2(self):
        for page in range(1, 4):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address+':'+ port
                yield result.replace(' ', '')

    #网站被墙 # TODO 添加代理访问
    # def crawl_premproxy(self):
    #     for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
    #         start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(
    #             i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>')
    #             re_ip_adress = ip_adress.findall(str(html))
    #             for adress_port in re_ip_adress:
    #                 yield adress_port.replace(' ', '')

    #网站被墙 # TODO 添加代理访问
    # def crawl_xroxy(self):
    #     for i in ['CN', 'TW']:
    #         start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(
    #             i)
    #         html = get_page(start_url)
    #         if html:
    #             ip_adress1 = re.compile(
    #                 "title='View this Proxy details'>\s*(.*).*")
    #             re_ip_adress1 = ip_adress1.findall(str(html))
    #             ip_adress2 = re.compile(
    #                 "title='Select proxies with port number .*'>(.*)</a>")
    #             re_ip_adress2 = ip_adress2.findall(html)
    #             for adress, port in zip(re_ip_adress1, re_ip_adress2):
    #                 adress_port = adress + ':' + port
    #                 yield adress_port.replace(' ', '')
