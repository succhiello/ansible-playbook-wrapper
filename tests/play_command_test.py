# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from ansible_playbook_wrapper.command.play import PlayCommand


def test_play_command():

    parser = ArgumentParser()

    for arg_info in PlayCommand.ARGUMENT_INFO:
        parser.add_argument(*(arg_info[0]), **(arg_info[1]))

    play_command = PlayCommand(
        parser.parse_args([
            '-e', 'hosts=personal users=kiri,gimlet,succhiello',
            'playbook.yml', '-i', 'inventories/development'
        ])
    )

    assert play_command.original_args == [
        'playbook.yml',
        '-i',
        'inventories/development'
    ]
    assert play_command.extra_vars == {
        'hosts': 'personal',
        'users': ['kiri', 'gimlet', 'succhiello'],
    }
    assert play_command.command_line == """ansible-playbook playbook.yml \
-i inventories/development -e \
'{"hosts": "personal", "users": ["kiri", "gimlet", "succhiello"]}'"""
