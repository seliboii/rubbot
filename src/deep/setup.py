from setuptools import find_packages, setup

package_name = 'deep'

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
    maintainer='g5',
    maintainer_email='geraortegapeim@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'ros2_detector = deep.ros2_detector:main','ros2_detector_backup = deep.ros2_detector_backup:mains'

        ],
    },
)
