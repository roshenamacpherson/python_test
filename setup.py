from setuptools import setup

setup(
    name='gnc_geosat',
    version='0.1dev',
    description='Astranis GNC Geosat Simulation Environment',
    packages=[
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    },
    python_requires='>=3',
    install_requires=[
        'numpy==1.14',
    ],
    dependency_links=[
    ],
)
