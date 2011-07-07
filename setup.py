from setuptools import setup, find_packages

setup(
    name='phenny',
    version=0.1,
    description="A Python IRC Bot",
    long_description=open('README.txt').read(),
    author='Sean B. Palmer',
    license='Eiffel Forum License 2',
    url='http://inamidst.com/phenny/',
    packages=find_packages(),
    scripts=['phenny/phenny'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Eiffel Forum License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
    ],
)