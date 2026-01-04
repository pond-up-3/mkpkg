from setuptools import setup

package_name = 'mkpkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tasuku Ikenoue',
    maintainer_email='j3311lmg@sit.ac.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = mkpkg.talker:main',
            'listener = mkpkg.listener:main',
        ],
    },
)
