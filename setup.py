from setuptools import setup

setup(
    name='ledger_app',
    version='0.1.0',
    author='Constance de Quatrebarbes',
    author_email='4barbes@gmail.com',
    py_modules = ['ledger.py', 'sampler.py', 'tests'],
    scripts=['ledger.py','sampler.py'],
    license='LICENSE.txt',
    description='CLI Hypothesis Ledger App Exercice',
    long_description=open('README.md').read(),
)
