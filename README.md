# so
This is a SSH login tool

## Linux ssh 登陆工具:

### 一.说明
- 命令行直接so
- 支持秘密和密钥两种格式
- 用户名和密码都是写文件的,明文保存
- 效果图:

![image](http://pqhvjjqev.bkt.clouddn.com/img/20190430214133.png)

### 二.安装

- 方法一
```
pip install --upgrade 0lever-so
or
pip install --upgrade 0lever-so -i https://pypi.org/simple/

# 初始化配置文件,升级无需初始化
so_install
```
- 方法二
```
下载whl文件
https://github.com/0lever/so/releases
wget https://github.com/0lever/so/releases/download/v1.0.9/0lever_so-1.0.9-py2-none-any.whl
pip install 0lever_so-1.0.9-py2-none-any.whl

# 初始化配置文件,升级无需初始化
so_install
```


### 三.配置
- 配置文件:
```
# 初始化配置文件
➜  ~ so_install
➜  ~ cd .so
➜  .so tree
.
├── keys
│   └── demo.pem
└── password.yaml

1 directory, 2 files
➜  .so

```
- 密码文件配置:
```
ssh:
  - id: 1
    name: demo1
    user: fqiyou
    password: xxx
    host: 1.1.1.1
    port: 20755
  - id: 2
    name: demo2
    user: fqiyou
    password: xxx
    host: 1.1.1.1
    port: 39986
  - id: 3
    name: demo3
    user: root
    password: demo.pem
    host: 1.1.1.1
    port: 22
```

>当password是以.pem结尾表示使用密钥登录，注意密钥文件权限

>密钥文件放在keys文件夹下,密码位置写成密钥文件名,文件名必须以.pem结尾
```
chmod 400 ~/.so/keys/*

```

