from setuptools import setup


setup(
    name='tabNamesCat',
    version='0.1.4',
    description='CategorizationTabNames',
    url='https://github.com/Denisalik/TabNamesCat',
    author='Denisalik',
    author_email='schgletovdenis@mail.ru',
    license='MIT',
    packages=['tabNamesCat'],
    package_data={'tabNamesCat': ['./*.pkl']},
    include_package_data=True,
    install_requires=['scikit-learn', 'langdetect', 'nltk'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)