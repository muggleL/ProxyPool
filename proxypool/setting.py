# Redis数据库的地址和端口
HOST = 'localhost'
PORT = 6379

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = ''

# 获得代理测试时间界限
get_proxy_timeout = 9

# 代理池数量界限
POOL_LOWER_THRESHOLD = 20
POOL_UPPER_THRESHOLD = 100

# 检查周期
VALID_CHECK_CYCLE = 60
POOL_LEN_CHECK_CYCLE = 20

# 测试API，用百度来测试
TEST_API='http://www.baidu.com'

# http://www.66ip.cn/ 的 cookies 和 userAgent
cookies = {'Cookie': 'yd_cookie=04a4dcb6-e384-482b65bdc74fcf0dbbd9f5a7c1e9d3b9ca0e; '
                     'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1545230230; '
                     '_ydclearance=b308b01cb24f930e33a1bfa0-4a24-4786-b201-750e322db5ca-1545279469; '
                     'Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1545275240'} 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 ' \
             'Safari/537.36 '
