# 导入服务器模块
from http.server import HTTPServer, CGIHTTPRequestHandler
# 指定端口
PORT = 8000
# 创建服务器对象
httpd = HTTPServer(("", PORT), CGIHTTPRequestHandler)
print("serving at port", PORT)
# 反复处理链接请求
httpd.serve_forever()