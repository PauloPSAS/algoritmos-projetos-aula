from random import choice
from time import sleep

# Cores e formatação
RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BOLD = '\033[1m'
RESET = '\033[m'


# Funções de resultado
def draw():
    sleep(0.8)
    print(f"\n{MAGENTA}Empate!{RESET}\n")
    sleep(0.4)


def win():
    sleep(0.8)
    print(f"\n{BLUE}Você Ganhou!{RESET}\n")
    sleep(0.4)


def lose():
    sleep(0.8)
    print(f"\n{RED}Você Perdeu!{RESET}\n")
    sleep(0.4)


# Função principal
def main():
    game_options = ('pedra', 'papel', 'tesoura')
    player_score = computer_score = 0

    print(f"{YELLOW}\nJO", end=' ')
    sleep(1)
    print("KEN", end=' ')
    sleep(1)
    print(f"PO!!!{RESET}\n")
    sleep(1)

    # Loop do jogo
    while True:
        # Exibir opções para o jogador
        while True:
            print(f"{f' {GREEN}< ESCOLHA >{RESET} ':~^50}")
            print(f"\n1 - {CYAN}Pedra{RESET}")
            sleep(0.5)
            print(f"\n2 - {CYAN}Papel{RESET}")
            sleep(0.5)
            print(f"\n3 - {CYAN}Tesoura{RESET}\n")
            print('~' * 43)
            sleep(0.3)

            try:
                choice_idx = int(input("\nDigite o número correspondente à sua escolha: ")) - 1
                if 0 <= choice_idx < 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"\n{BOLD}{RED}Opção inválida! Digite apenas números correspondentes aos acima.{RESET}\n")
                sleep(0.7)

        player_choice = game_options[choice_idx]
        computer_choice = choice(game_options)

        sleep(1)
        print(f"\nVocê escolheu: {CYAN}{player_choice}{RESET}.\nComputador escolheu: {CYAN}{computer_choice}{RESET}.\n")
        sleep(1)

        # Determinar o resultado
        if player_choice == computer_choice:
            draw()
        elif (player_choice == 'pedra' and computer_choice == 'tesoura') or \
                (player_choice == 'papel' and computer_choice == 'pedra') or \
                (player_choice == 'tesoura' and computer_choice == 'papel'):
            win()
            player_score += 1
        else:
            lose()
            computer_score += 1

        # Exibir pontuação atual
        print(f"{GREEN}Pontuação:{RESET} Você {player_score} - {computer_score} Computador\n")

        # Verificar se alguém venceu 3 vezes
        if player_score == 3 or computer_score == 3:
            print(f"\n{YELLOW}Fim de jogo.{RESET}")
            break

    # Mensagem final
    if player_score > computer_score:
        sleep(0.8)
        print(f"\n{BOLD}{BLUE}VOCÊ VENCEU! MEUS PARABÉNS!!!{RESET}\n")
    else:
        sleep(0.8)
        print(f"\n{BOLD}{RED}COMPUTADOR VENCEU! Se esforce mais na próxima.{RESET}\n")


if __name__ == "__main__":
    main()
