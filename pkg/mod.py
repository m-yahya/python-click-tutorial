import click


@click.command()
@click.option('--port', prompt='port', default=8545, help='Port for HTTP connections')
def mod_func(port):
    """
    Setting web3 provider for connecting to local and remote JSON-RPC servers.
    """

    print(port)
    return port
