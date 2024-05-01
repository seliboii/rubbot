from setuptools import find_packages, setup

package_name = 'planning'

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
    maintainer_email='g5@todo.todo',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'planning = planning.planning:main',
            'occupancy_grid = planning.occupancy_grid:main',
            'generate_path = planning.generate_path:main',
            'follower = planning.follower:main',
            "move_to_goal_server = planning.move_to_goal_server:main",
            "move_to_goal_client = planning.move_to_goal_client:main" 
        ],
    },
)
