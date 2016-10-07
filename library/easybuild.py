#!/usr/bin/python

import json

from ansible.module_utils.basic import *

module = AnsibleModule(
    argument_spec={
        'name': {'required': False, 'type': 'str'},
        'version': {'default': None, 'required': False, 'type': 'str'},
        'state': {
            'default': 'present',
            'required': False,
            'choices': ['present', 'absent', 'latest']
        },
        'channels': {'default': None, 'required': False},
        'executable': {'default': None, 'required': False},
        'extra_args': {'default': None, 'required': False, 'type': 'str'}
    },
    supports_check_mode=True)

eb_command = "eb --help"

(rc, stdout, stderr) =  module.run_command("bash -c \"module load EasyBuild && " + eb_command + "\"")

print json.dumps({
    "arguments" : module.params,
    "changed" : True,
    "exitcode": rc
    # "stdout": stdout,
    # "stderr": stderr
})