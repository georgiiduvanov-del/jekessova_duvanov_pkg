from setuptools import find_packages, setup

package_name = 'jekessova_duvanov_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='i-mv',
    maintainer_email='i-mv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'first_node = jekessova_duvanov_pkg.first_node:main',
            'time_printer = jekessova_duvanov_pkg.time_printer:main',
        ],
    },
)
