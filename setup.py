# -*- coding:utf-8 -*-
#from ez_setup import use_setuptools
#use_setuptools()

from setuptools import setup, find_packages
import re

main_py = open('check_apache/__init__.py').read()
metadata = dict(re.findall("__([A-Z]+)__ = '([^']+)'", main_py))
__VERSION__ = metadata['VERSION']

setup(
        name='check-apache',
        version=__VERSION__,
        author='APSL · Edu Herraiz Aparicio',
        author_email='eherraiz@apsl.net',
        packages=find_packages(),
        license='GPL',
        description="Check apache process and graceful status",
        long_description=open('README.rst').read(),
        entry_points={
                    'console_scripts': [
                                    'check-apache = check_apache.main:check',
                                ],
                },
        install_requires=[
                    'click',
                    'dnspython',
                    'netaddr'
                ],
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: GPL License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Topic :: Internet :: WWW/HTTP',
                ],
        include_package_data=True,
        zip_safe=False,
)
