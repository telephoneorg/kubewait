import re
from setuptools import setup, find_packages


with open('kubewait/__init__.py', 'rt') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst') as fd:
    long_description = fd.read()


setup(
    name='kubewait',
    version=version,
    description='Pause container init until required kube services are ready',
    long_description=long_description,
    keywords=['kubernetes', 'clustering', 'init-container'],
    author='Joe Black',
    author_email='joeblack949@gmail.com',
    url='https://github.com/joeblackwaslike/kubewait',
    download_url='https://github.com/joeblackwaslike/kubewait/tarball/0.2.0',
    license='Apache 2.0',
    zip_safe=False,
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=[
        'pyrkube',
        'cement'
    ],
    tests_require=['pytest'],
    entry_points=dict(
        console_scripts=['kubewait = kubewait.cli:main']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Clustering',
    ]
)
