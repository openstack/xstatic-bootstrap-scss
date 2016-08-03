from setuptools import setup, find_packages

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
long_description = open('README.txt').read()

setup(
    name='XStatic-Bootstrap-SCSS',
    summary="""Bootstrap-SCSS 3.3.7 (XStatic packaging standard)""",
    description=long_description,
    maintainer="Radomir Dopieralski",
    maintainer_email='openstack@sheep.art.pl',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'wheel'],
    packages=find_packages(),
    include_package_data=True
)
