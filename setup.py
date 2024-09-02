from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='resume_parser',
    version='0.1.0',
    author='Raj, Satyajit Pattnaik, Ragu',
    author_email='https.ragu@gmail.com',
    description='A Python package to parse and analyze resumes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Rajadurai2/Resume-parsing-using-LLM-Langchain
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'PyYAML',
        'pdfminer.six',
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'resume_parser=dash:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

