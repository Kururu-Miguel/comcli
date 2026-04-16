from servidor import main as servidor_main
from handler import main as handler_main
import argparse



def main():
    parser = argparse.ArgumentParser(
        prog='comcli', 
        description='Um cliente terminal de comunicação feito em python', 
        epilog='Vejo o epílogo depois'
    )
    parser.add_argument('-s', '--serve', action='store_true', help='Inicia um servidor no localhost')
    parser.add_argument('-p', '--port', default=8080, type=int, help='Define a porta do servidor (padrão 8080)')
    args = parser.parse_args()
    if args.port and not args.serve:
        parser.error('argument -p/--port: O argumento -s/--serve deve estar presente')
    if args.serve:
        servidor_main(args.port)
    else:
        handler_main()


if __name__ == '__main__':
    main()
