from setuptools import setup, find_packages

setup(
    name             = 'pyHwp2Html',
    version          = '1.0',
    description      = 'Convert Hwp to Html',
    author           = 'Na Kyung Hyun',
    author_email     = 'nakh76@gmail.com',
    url              = 'https://github.com/nakh76/pyHwp2Html',
    download_url     = 'https://github.com/nakh76/pyHwp2Html/1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['hwp', 'html'],
    python_requires  = '>=3',
    package_data     =  {
        'hwp2html' : [
            'java/hwp2html-1.0.0.jar'
        ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)