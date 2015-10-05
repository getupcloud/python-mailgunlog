import setuptools

setuptools.setup(name='mailgunlog',
                 version='0.0.3',
                 description='Mailgun Log',
                 long_description='Python Package to retrieve Mailgun logs for a given domain.',
                 author='Getup Cloud',
                 author_email='mateus.caruccio@getupcloud.com',
                 url='https://github.com/getupcloud/python-mailgunlog',
                 packages=['mailgunlog'],
                 install_requires=['requests>=2.0.0', 'python-dateutil>=2.2'],
                 license='Apache Software License',
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
                     'Development Status :: 4 - Beta',

                     # Indicate who your project is intended for
                     'Intended Audience :: Developers',
                     'Topic :: Software Development :: Build Tools',

                     # Pick your license as you wish (should match "license" above)
                      'License :: OSI Approved :: Apache Software License',

                     # Specify the Python versions you support here. In particular, ensure
                     # that you indicate whether you support Python 2, Python 3 or both.
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                 ]
)
