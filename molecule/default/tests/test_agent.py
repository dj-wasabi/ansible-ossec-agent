import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('agent')


def test_ossec_package_installed(Package, SystemInfo):
    if SystemInfo.distribution in ['debian', 'ubuntu']:
        ossec = Package('ossec-hids-agent')
    elif SystemInfo.distribution == 'centos':
        ossec = Package('ossec-hids')
    assert ossec.is_installed


def test_ossec_service_running_and_enabled(Service, SystemInfo):
    if SystemInfo.distribution in ['debian', 'ubuntu']:
        ossec = Service('ossec')
    else:
        ossec = Service('ossec-hids')
    assert ossec.is_enabled
    assert ossec.is_running


def test_client_keys(File):
    zabbix_server_conf = File("/var/ossec/etc/client.keys")
    assert zabbix_server_conf.user == "root"
    assert zabbix_server_conf.group == "ossec"
    assert zabbix_server_conf.mode == 0o640


def test_ossec_agent(File, SystemInfo):
    if SystemInfo.distribution in ['debian', 'ubuntu']:
        ossec_file = File("/var/ossec/etc/ossec.conf")
    else:
        ossec_file = File("/var/ossec/etc/ossec-agent.conf")
    assert ossec_file.user == "root"
    assert ossec_file.group == "root"
    assert ossec_file.mode == 0o644
