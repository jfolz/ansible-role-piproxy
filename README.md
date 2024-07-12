Role Name
=========

Install the [piproxy](https://github.com/jfolz/piproxy) PyPI caching proxy.

Requirements
------------

Platform Debian>=bullseye or Ubuntu>=focal, though realistically any recent systemd-based Linux should work.

Role Variables
--------------

Below are variable as defined in `defaults/main.yml`

```yaml
piproxy_version: "0.1.5"
piproxy_service_name: "piproxy"
piproxy_user: "piproxy"
piproxy_group: "{{ piproxy_user }}"
piproxy_address: "0.0.0.0:8080"
piproxy_prometheus_address: "0.0.0.0:9898"
piproxy_cache_path: "/var/lib/cache/{{ piproxy_service_name }}"
piproxy_cache_size: "20G"
piproxy_read_size: "256k"
piproxy_log_level: "info"
piproxy_pingora_config:
  threads: 4
```

For possible values to put under `piproxy_pingora_config`, see
https://www.pingorarust.com/user_guide/conf

**Note:** Overwriting `piproxy_pingora_config` will delete `threads: 4`,
so remember to set whichever value you want as well.
Also, you must not set `pid_file` and `upgrade_sock`.
These always live under `/run/{{ piproxy_service_name }}/`

Dependencies
------------

None

Example Playbook
----------------

```yaml
- name: Deploy piproxy PyPI cache
  hosts: pypi-cache
  vars:
    piproxy_cache_path: "/var/cache/piproxy"
    piproxy_log_level: "warn"
  roles:
    - name: jfolz.piproxy
```

License
-------

MIT

Author Information
------------------

Made by Joachim Folz with support from the [SustainML](https://sustainml.eu/) project.