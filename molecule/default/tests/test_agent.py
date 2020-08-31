import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('agent')


def test_ossec_package_installed(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        ossec = host.package('ossec-hids-agent')
    elif host.system_info.distribution == 'centos':
        ossec = host.package('ossec-hids')
    assert ossec.is_installed


def test_ossec_service_running_and_enabled(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        ossec = host.service('ossec')
    else:
        ossec = host.service('ossec-hids')
    assert ossec.is_enabled
    assert ossec.is_running


def test_client_keys(host):
    zabbix_server_conf = host.file("/var/ossec/etc/client.keys")
    assert zabbix_server_conf.user == "root"
    assert zabbix_server_conf.group == "ossec"
    assert zabbix_server_conf.mode == 0o640


def test_ossec_agent(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        ossec_file = host.file("/var/ossec/etc/ossec.conf")
    else:
        ossec_file = host.file("/var/ossec/etc/ossec-agent.conf")
    assert ossec_file.user == "root"
    assert ossec_file.group == "root"
    assert ossec_file.mode == 0o644
