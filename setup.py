from setuptools import setup, find_packages
from DaPy import __version__, _unittests
from DaPy.core.base.constant import PYTHON2

pkg = find_packages()
_unittests()

requirements = [
        'xlrd >= 1.1.0',     # Used in DaPy.base.io.parse_excel()
        'xlwt >= 1.3.0',     # Used in DaPy.base.DataSet.DataSet.save()
    ]

if PYTHON2:
    requirements.append('repoze.lru')

setup(
    name='DaPy',
    version=__version__,
    description='Enjoy Your Tour in Data Mining',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='Xuansheng Wu',
    author_email='wuxsmail@163.com',
    maintainer='Xuansheng Wu',
    maintainer_email='wuxsmail@163.com',
    platforms=['all'],
    url='http://dapy.kitgram.cn',
    license='GPL v3',
    packages=pkg,
    package_dir={'DaPy.datasets': 'DaPy/datasets'},
    package_data={'DaPy.datasets': ['adult/*.*', 'example/*.*', 'iris/*.*', 'wine/*.*']},
    zip_safe=True,
    install_requires=requirements

)
