from HW18.proxy_pattern.proxy_txt_reader import TxtProxyReader
from HW18.proxy_pattern.txt_reader import TxtReader

txt_reader = TxtReader('users.txt')
proxy_reader = TxtProxyReader(txt_reader)

print(proxy_reader.read_file())
print('\n')
print(proxy_reader.read_file())
