# so
This is a SSH login tool

## Linux ssh 登陆工具:

### 一.说明

- 支持秘密和密钥两种格式
- 用户名和密码都是写文件的,明文保存

### 二.安装

```
pip install --upgrade 0lever-so
or
pip install --upgrade 0lever-so -i https://pypi.org/simple/

```


### 三.配置
- 配置文件:
```
so_install
ll ~/.so/
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


- 密钥文件放在keys文件夹下,密码位置写成密钥文件名,文件名必须以.pem结尾
```
chmod 400 ~/.so/keys/*

```
