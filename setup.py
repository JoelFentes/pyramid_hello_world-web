from setuptools import setup, find_packages

requires = [
    'pyramid',
    'waitress',
    'pyramid_jinja2',
]
setup(
    name='pyramid_hello_world',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = app:main',  # Ajustado para apontar para o módulo correto
        ],
    },
)