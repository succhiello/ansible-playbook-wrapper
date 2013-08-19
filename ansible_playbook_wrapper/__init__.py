# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from ansible_playbook_wrapper.command.play import PlayCommand


def main():

    parser = ArgumentParser()

    sub_parsers = parser.add_subparsers(help='commands')

    play_parser = sub_parsers.add_parser('play', help='play playbook')
    for arg_info in PlayCommand.ARGUMENT_INFO:
        play_parser.add_argument(*(arg_info[0]), **(arg_info[1]))
    play_parser.set_defaults(command_class=PlayCommand)

    parsed_args = parser.parse_args()
    parsed_args.command_class(parsed_args).run()
