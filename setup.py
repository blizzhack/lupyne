from setuptools import setup
import lupyne

setup(
    name='lupyne',
    version=lupyne.__version__,
    description='Pythonic search engine based on PyLucene, including a standalone server based on CherryPy.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aric Coady',
    author_email='aric.coady@gmail.com',
    url='https://github.com/coady/lupyne',
    project_urls={'Documentation': 'https://coady.github.io/lupyne/'},
    license='Apache Software License',
    packages=['lupyne', 'lupyne.engine', 'lupyne.server', 'lupyne.services'],
    extras_require={
        'server': ['cherrypy>=11'],
        'docs': ['nbsphinx', 'jupyter'],
        'rest': ['fastapi'],
        'graphql': 'strawberry-graphql>=0.26.1',
    },
    python_requires='>=3.6',
    tests_require=['pytest-cov', 'clients'],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Framework :: CherryPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Indexing',
    ],
)
