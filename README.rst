ansible-playbook-wrapper
========================

wrapper for ansible-playbook CLI.

dependencies
------------
- ansible
- pytest

install
-------

::

  $ git clone https://github.com/succhiello/ansible-playbook-wrapper.git
  $ python setup.py install

usage
-----

::

  $ ansible-playbook-wrapper play -e 'hosts=personal users=kiri,gimlet,succhiello' playbook.yml -i inventories/production

will execute below.

::

  ansible-playbook playbook.yml -i inventories/production -e '{"hosts": "personal", "users": ["kiri", "gimlet", "succhiello"]}'

ansible-playbook-wrapper converts 'extra-vars' option from 'key=value' to JSON, and executes with the remainder of arguments internally.

'extra-vars' and yml argument is positional.

