from setuptools import setup, find_packages

setup(
    name='TalkativeChess',
    version='0.1.0',
    description='Talkative Chess',
    long_description=open('README.md','r').read(),
    author='Liu',
    author_email='liuxl_l@qq.com',
    url='https://github.com/lxline/TalkativeChess',
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)