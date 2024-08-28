from setuptools import setup, find_packages

setup(
    name='nucleidechartlib',
    version='0.1.0',
    description='Una librería para generar tablas de nucleidos.',
    author='Alfonso Jesús Piñera Herrera',
    author_email='alfonsojph@correo.ugr.es',
    packages=find_packages(),  # Usa find_packages() para detectar automáticamente todos los paquetes
    install_requires=[
        'setuptools==69.0.3',
        'svgwrite==1.4.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
