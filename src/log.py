from colorama import Fore


def error(message: str):
    print(f'{Fore.RED}Erro{Fore.RESET} {message}')


def message(message: str):
    print(f'{Fore.CYAN}Mensagem{Fore.RESET} {message}')
