from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'rover_status'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gautam',
    maintainer_email='gautam@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'bat_temp = rover_status.bat_temp_level:main',
                'status = rover_status.health_status:main',
                'r_status = rover_status.rover_health:main',
        ],
},
)
