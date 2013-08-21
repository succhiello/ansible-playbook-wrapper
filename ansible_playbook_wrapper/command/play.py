# -*- coding: utf-8 -*-

from __future__ import print_function

import json
import subprocess

from argparse import REMAINDER

import ansible.utils


class PlayCommand(object):

    ARGUMENT_INFO = [
        (
            ['-e', '--extra-vars'],
            {
                'default': '',
                'help': 'comma separation enabled extra variables '
                'for ansible-playbook'
            }
        ),
        (
            ['original_args'],
            {
                'nargs': REMAINDER,
                'help': 'original args for ansible-playbook'
            }
        )
    ]

    def __init__(self, args):
        self._original_args = args.original_args
        self._extra_vars = self._make_extra_vars_dict(args.extra_vars)

    @property
    def original_args(self):
        return self._original_args

    @property
    def extra_vars(self):
        return self._extra_vars

    @property
    def command_line(self):
        return "ansible-playbook {o_args} -e '{e_vars}'".format(
            o_args=' '.join(str(arg) for arg in self._original_args),
            e_vars=json.dumps(self._extra_vars)
        )

    def run(self):
        print('execute: {cmd_line}...'.format(cmd_line=self.command_line))
        subprocess.call(self.command_line, shell=True)

    @classmethod
    def _make_extra_vars_dict(cls, extra_vars):
        return dict(
            (k, v.split(',') if ',' in v else v)
            for k, v in ansible.utils.parse_kv(extra_vars).iteritems()
        )
