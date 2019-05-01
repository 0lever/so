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


Other-shell

=====

::

    #!/usr/bin/expect
    set USER "xxx"
    set PASSWD "xxx"
    set timeout 10

    trap {
        set rows [stty rows]
        set cols [stty columns]
        stty rows $rows columns $cols < $spawn_out(slave,name)
    } WINCH
    spawn su - $USER
    expect "Password: "
    send "$PASSWD\n"
    interact

::

    #!/usr/bin/expect -f
    set HOST [lindex $argv 0]
    set USER [lindex $argv 1]
    set PASSWD [lindex $argv 2]
    set PORT [lindex $argv 3]
    set timeout 10

    trap {
        set rows [stty rows]
        set cols [stty columns]
        stty rows $rows columns $cols < $spawn_out(slave,name)
    } WINCH

    spawn ssh $USER@HOST -p $PORT
    expect {
        "*yes/no" {send "yes\r"; exp_continue}
        "*password:" {send "$PASSWD\r"}
    }
    interact
    ```