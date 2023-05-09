''' a sample package
'''
import argparse


def greet_me(name='Friend'):
    print(f'Hello, {name}!')


def _greet_me():
    parser = argparse.ArgumentParser(description='Log a greeting.')
    parser.add_argument('name', type=str,
                        help='What you prefer to be called.')
    args = parser.parse_args()

    greet_me(args.name)

