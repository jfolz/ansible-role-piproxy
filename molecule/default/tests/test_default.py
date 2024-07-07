import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_piproxy_running_and_enabled(host):
    service = host.service("piproxy")
    assert service.is_running
    assert service.is_enabled
