import click
import trio


@click.group(invoke_without_command = True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    'Um cliente terminal de comunicação descentralizado focado em privacidade'

    if ctx.invoked_subcommand == None:
        from comcli.cliente import cliente
        trio.run(cliente)

@cli.command()
@click.option('--porta', default=6767, type=int)
def server(porta: int) -> None:
    'Inicia um peer que escuta conexões'

    from comcli.server import server
    trio.run(server, porta)

