from setuptools import find_packages, setup

package_name = 'arm'

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
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_ik = arm.arm_ik:main',
            'arm_control = arm.arm_control:main',
            'arm_fk = arm.arm_fk:main',
            'arm_state_machine = arm.arm_state_machine:main'
        ],
    },
)
