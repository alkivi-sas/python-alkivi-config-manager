python-alkivi-config-manager
==========================

[![Build Status](https://travis-ci.org/alkivi-sas/python-alkivi-config-manager.svg?branch=master)](https://travis-ci.org/alkivi-sas/python-alkivi-config-manager)
[![Requirements Status](https://requires.io/github/alkivi-sas/python-alkivi-config-manager/requirements.svg?branch=master)](https://requires.io/github/alkivi-sas/python-alkivi-config-manager/requirements/?branch=master)

Python config-manager used at Alkivi

## Package

Example

Write a conf like

```ini
[default]
; general configuration: default endpoint
endpoint=dev

[dev]
; configuration specific to 'dev' endpoint
env=dev

[prod]
; configuration specific to 'prod' endpoint
env=prod
```

```python
from alkivi.config import ConfigManager
config = ConfigManager('test')

# This will look for several files, in order
# 1. Current working directory: ``./test.conf``
# 2. Current user's home directory ``~/.test.conf``
# 3. System wide configuration ``/etc/test.conf``

# Then find the endpoint
endpoint = config.get('default', endpoint)

# Or use a specific one
endpoint = 'prod'

# And then
env = config.get(endpoint, 'env')
```

## Parameters


## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

TODO

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.

TODO
