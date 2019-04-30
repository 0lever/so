# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='0lever-so',

      version="1.0.9",

      url='https://github.com/0lever/so',

      author='fqiyou',

      author_email='yc.fqiyou@gmail.com',

      description=u'跳板机登录脚本',

      install_requires=["pyyaml", "pexpect"],

      packages=find_packages(),

      long_description=open('README.md').read(),

      package_data={
      },

      entry_points={
            'console_scripts': [
                  'so = so.so:run',
                  'so_install = so.so:run_install',
            ],
      }

)

# source activate execpython
# python setup.py sdist
# python setup.py install
# python setup.py bdist_wheel/python setup.py sdist
# python setup.py bdist_wheel upload -r coohua
# python setup.py bdist_wheel upload -r pypi
# pip install --upgrade 0lever-so -i https://pypi.org/simple/

# /usr/local/app/application/anaconda/anaconda2/envs/python36/bin/python  setup.py bdist_wheel upload -r pypi
# /usr/local/app/application/anaconda/anaconda2/envs/python-tools/bin/python  setup.py bdist_wheel upload -r pypi