from setuptools import find_packages, setup

package_name = 'addision_scripts'

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
    maintainer='erdem',
    maintainer_email='erdemersan@msn.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_inspection = addision_scripts.scripts.run_inspection:main',
            'robot_navigator = addision_scripts.scripts.robot_navigator:main',
        ],
    },
)
