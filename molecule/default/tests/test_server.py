import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('server')


def test_ossec_package_installed(host):
    cmd = host.run("/var/ossec/bin/list_agents -a")
    assert 'ossec-agent-centos' in cmd.stdout
    assert 'ossec-agent-debian' in cmd.stdout
