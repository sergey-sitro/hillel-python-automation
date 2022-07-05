from HW18.proxy_pattern.proxy_txt_reader import TxtProxyReader
from HW18.proxy_pattern.txt_reader import TxtReader
from HW18.proxy_pattern.txt_writer import TxtWriter

txt_reader = TxtReader('users.txt')
txt_writer = TxtWriter("users.txt", "test")
proxy_reader = TxtProxyReader(txt_reader, txt_writer)

print(proxy_reader.read_file())
print('\n')
print(proxy_reader.write_file("test"))
