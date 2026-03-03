from setuptools import find_packages, setup

package_name = 'obstacle_avoidance'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name , ['package.xml']),
        ('share/' + package_name + '/launch',
            ['launch/obstacle_avoidance.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sd_robotics',
    maintainer_email='sd_robotics@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['obstacle_avoidance=obstacle_avoidance.obstacle_avoidance_node:main',
        ],
    },
)
