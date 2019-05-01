======
so
======

This is a SSH login tool

Installation
============

::

    pip install --upgrade 0lever-so
    or
    pip install --upgrade 0lever-so -i https://pypi.org/simple/


Usage
=====

::

    # 初始化配置文件,升级无需初始化,chmod 400 ~/.so/keys/*
    ➜  ~ so_install
    ➜  ~ cd .so
    ➜  .so tree
    .
    ├── keys
    │   └── demo.pem
    └── password.yaml

    1 directory, 2 files
    ➜  .so


::

    # 配置文件
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

