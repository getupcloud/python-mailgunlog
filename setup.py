import setuptools
import mailgunlog

setuptools.setup(name='mailgunlog',
                 version=mailgunlog.__version__,
                 description='Mailgun Log',
                 long_description=open('README.md').read().strip(),
                 author='Getup Cloud',
                 author_email='mateus.caruccio@getupcloud.com',
                 url='https://github.com/getupcloud/python-mailgunlog',
                 packages=['mailgunlog'],
                 py_modules=['mailgunlog'],
                 install_requires=['requests'],
                 license='Apache License 2.0',
                 zip_safe=False,
                 keywords='mailgun log email mail')
