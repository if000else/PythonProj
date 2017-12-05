# SimpleFTP
1. 用户登陆
2. 上传/下载文件
3. 不同用户家目录不同
4. 查看当前目录下文件
5. 充分使用面向对象知识


登录：admin 123456

运行：先运行server.py,启动服务，然后运行ftp.py

目录结构：

`SimpleFTP/`

`　　|-- bin/`

`　　　　| |-- ftp.py`

`　　|`

`　　|-- conf/`

`　　　　| |-- settings.py`

`　　|-- database/`

`　　　　|　|-- client/`

`　　　　|　|-- server/`

`　　　　|　|-- users/`

`　　　　| `

`　　|-- report/`

`　　　　|　|-- log/`

`　　　　|　|  |-- access.log`

`　　　　|　|  |-- client.log`

`　　　　|　|  |-- server.log`

`　　　　|　|  |-- services.log`
        
`　　　　| `

`　　|-- modules/`

`　　　　| |-- display.py`

`　　　　| |-- log.py`

`　　　　| |-- main.py`

`　　　　| |-- server.py`

`　　　　| |-- funcs.py`


`　　　　|`

`　　|-- README`
