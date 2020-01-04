import click

import pkg as pkg

cli = click.Group()


@cli.command()
def main_func():
    print('Setting up web3 Provider')
    pkg.mod_func()


if __name__ == '__main__':
    cli()
