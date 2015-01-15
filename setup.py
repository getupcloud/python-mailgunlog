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
                 install_requires=['requests>=2.0.0'],
                 license='Apache License 2.0',
                 zip_safe=False,
                 entry_points={
                     'console_scripts': [
                         'mailgunlog = mailgunlog.mailgunlog:main'
                     ],
                 },
                 keywords='mailgun log email mail',
                 classifiers=[
                     # How mature is this project? Common values are
                     #   3 - Alpha
                     #   4 - Beta
                     #   5 - Production/Stable
                     'Development Status :: 3 - Beta',

                     # Indicate who your project is intended for
                     'Intended Audience :: Developers',
                     'Topic :: Software Development :: Build Tools',

                     # Pick your license as you wish (should match "license" above)
                      'License :: OSI Approved :: Apache License 2.0',

                     # Specify the Python versions you support here. In particular, ensure
                     # that you indicate whether you support Python 2, Python 3 or both.
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                 ]
)
