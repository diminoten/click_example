from setuptools import setup

setup(
    name='click_example',
    version='1.0.0',
    packages=['click_example'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'click_example=click_example:main'
        ]
    },
    license='LICENSE'
)
