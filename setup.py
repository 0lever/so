# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='0lever-so',

      version="2.0.2",

      url='https://github.com/0lever/so',

      author='fqiyou',

      author_email='yc.fqiyou@gmail.com',

      description=u'服务器登录工具',

      install_requires=["pyyaml", "pexpect"],

      packages=find_packages(),

      long_description=open('README.rst').read(),

      package_data={
      },

      entry_points={
            'console_scripts': [
                  'so = so.so:run',
                  'so_install = so.so:run_install',
            ],
      }

)

# pip install build twine
# python -m build            # 生成 dist/ 下的 sdist 和 wheel
# twine upload dist/* -r coohua
# twine upload dist/* -r pypi
# pip install --upgrade 0lever-so -i https://pypi.org/simple/

# python -m build && twine upload dist/* -r pypi