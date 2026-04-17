import asyncio, argparse
from cliente import main as cliente_main
from tui import main as tui_main
from servidor import main as servidor_main



def handler_cliente(args):
    queue = asyncio.Queue()
    host = input('host: ')
    porta = input('porta: ')
    asyncio.run(cliente_main(host, porta))
    tui_main()


def handler_server(args):
    asyncio.run(servidor_main(args.porta))


def main():
    parser = argparse.ArgumentParser(
        prog='comcli', 
        description='Um cliente terminal de comunicação feito em python', 
        epilog='Vejo o epílogo depois'
    )

    subparsers = parser.add_subparsers(
        dest='comando', 
        required=True, 
        help='Define o comportamento do aplicativo'
    )

    parser_cliente = subparsers.add_parser('cliente', help='Entra em modo cliente')
    parser_server = subparsers.add_parser('server', help='Inicia um servidor no ip local')
    
    parser_server.add_argument(
        '-p',
        '--porta',
        default=8080,
        type=int, 
        help='Define a porta do servidor local (padrão 8080)'
    )

    parser_cliente.set_defaults(func=handler_cliente)
    parser_server.set_defaults(func=handler_server)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args) 


if __name__ == '__main__':
    main()
