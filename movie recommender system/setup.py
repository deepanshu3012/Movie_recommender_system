from setuptools import setup
with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()
author_name='Deepanshu Joshi'
src_repo='src'
list_of_requirements=['streamlit']
setup(
    name=src_repo,
    version='0.0.1',
    author=author_name,
    author_email='deepanshujoshi3012@gmail.com',
    description='A simple python pacakage to create a simple web app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[src_repo],
    python_requires='>=3.10',
    install_requires=list_of_requirements,
)
