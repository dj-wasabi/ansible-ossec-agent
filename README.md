dj-wasabi.ossec-agent
=========

This role will install and configure an ossec-agent on the server. When there there is an parameter `ossec_server_name` configured, it will delagate an action for automatically authenticate the agent. 

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-ossec-agent.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-ossec-agent)


Requirements
------------

This role will work on:
 * Red Hat
 * Ubuntu
 * Debian

So, you'll need one of those operating systems.. :-)

Role Variables
--------------

This role needs 4 parameters:
* `ossec_server_ip`: This is the ip address of the server running the ossec-server.
* `ossec_server_fqdn`: This is the fqdn of the server running the ossec-server.
* `ossec_server_name`: This is the hostname of the server running the ossec-server used for delegate with ansible. 
* `ossec_managed_server`: When set to false, tasks that delegate to ossec server will be skipped

This role has 3 tasks with 'delagation_to' which needs the parameter `ossec_server_name`. When this parameter is not set, you'll need to run manually the `/var/ossec/bin/ossec-authd` on the server and `/var/ossec/bin/agent-auth` on the agent. When this is the case, it will show you an message with the exact command line.

The following role variables are optional:
* `ossec_active_response_disabled`: Disables active response if set to yes. If this is not defined active response is enabled.
* `ossec_disable_public_repos`: Disables installation of public repositories if set to "yes".
* `ossec_agent_package_name`: Default is "ossec-hids-agent". This can be set to a URL or path to a .rpm file or path to a .deb file if the public repositories cannot be used.

Dependencies
------------

No dependencies.

Example Playbook
----------------

The following is an example how this role can be used:

    - hosts: all:!ossec-server.example.com
      roles:
         - { role: dj-wasabi.ossec-agent, ossec_server_ip: 192.168.1.1, ossec_server_name: ossec-server.example.com }

Molecule
--------

This roles is configured to be tested with Molecule. You can find on this page some more information regarding Molecule: https://werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker/
Molecule will boot 4 docker containers, containing the following OS:

* CentOS 7 (Ossec Server)
* CentOS 7 (Ossec Agent)
* Debian 8 (Ossec Agent)
* Ubuntu 16.04 (Ossec Agent)

License
-------

GPLv3

Author Information
------------------

Please send suggestion or pull requests to make this role better. 

Github: https://github.com/dj-wasabi/ansible-ossec-agent

mail: ikben [ at ] werner-dijkerman . nl
