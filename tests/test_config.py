import os

from alkivi.config import ConfigManager

filename = os.path.expanduser('~/.test.conf')

def _write_config():
    fh = open(filename, 'w')
    fh.write('[default]')
    fh.write('; general configuration: default endpoint\n')
    fh.write('endpoint=pytest\n')
    fh.write('\n')
    fh.write('[pytest]\n')
    fh.write('test=test\n')
    fh.write('[pytest2]\n')
    fh.write('test=test\n')
    fh.close()

def _delete_config():
    if os.path.isfile(filename):
        os.remove(filename)

def test_config():
    _write_config()
    config = ConfigManager('test')
    endpoint = config.get('default', 'endpoint')
    assert endpoint == 'pytest'

    assert config.get(endpoint, 'test') == 'test'
    assert config.get('pytest2', 'test') == 'test'

    _delete_config()
