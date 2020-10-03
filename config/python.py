import config.project

package_name = config.project.project_name

console_scripts = [
    'pymultigit=pymultigit.main:main',
]

setup_requires = [
]

run_requires = [
    'gitpython',  # for accessing git
    'pyfakeuse',  # fake use of a var
    'pytconf',  # for command line parsing
    'pylogconf',  # for logging configuration
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pytest-cov',  # for testing
    'flake8',  # for linting
    'pymakehelper',  # for make
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
