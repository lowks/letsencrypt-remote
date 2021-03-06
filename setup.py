from setuptools import setup
import os


README = open(os.path.abspath('README.rst')).read()
HISTORY = open(os.path.abspath('HISTORY.rst')).read()


setup(
    name='letsencrypt-remote',
    version='0.5.0',
    long_description="\n\n".join([README, HISTORY]),
    url='https://github.com/fschulze/letsencrypt-remote',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4"],
    install_requires=[
        'click',
        'dnspython3',
        'pyOpenSSL',
        'requests'],
    entry_points={
        'console_scripts': ['letsencrypt-remote = letsencrypt_remote:main']},
    py_modules=['letsencrypt_remote'])
