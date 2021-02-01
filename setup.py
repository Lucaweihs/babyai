from setuptools import find_packages, setup

setup(
    name='babyai',
    version='0.1.0',
    license='BSD 3-clause',
    keywords='memory, environment, agent, rl, openaigym, openai-gym, gym',
    packages=find_packages(include=['babyai', 'babyai.*']),
    install_requires=[
        "gym>=0.9.6",
        "numpy>=1.15",
        "torch>=0.4.1",
        "blosc>=1.5.1",
        "gym-minigrid>=1.0.1"
    ],
)
