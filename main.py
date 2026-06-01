import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    if comando == 'tempo':
        return 'Está um dia de sol!'
    if comando in ('bye', 'adeus', 'tchau'):
        return 'Gostei de falar contigo! Até breve...'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
    if comando == 'Qual a tua cor favorita?':
          return 'Que cor bonita '

    return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
         ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
         'como estás': 'Estou bem, obrigado!',
         ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
         'qual é a tua idade': 'Sou um programa, não tenho idade 😄',
         'o que fazes': 'Eu respondo às tuas mensagens!',
        'qual é a capital de portugal': 'A capital de Portugal é Lisboa 🇵🇹',
        'gostas de programação': 'Sim! Adoro aprender código 💻',
          'qual é o teu objetivo': 'Ajudar-te a conversar e responder perguntas!'
         
     }

    for chave, resposta in respostas.items():
         if isinstance(chave, tuple):
             if comando in chave:
                 return resposta
         elif chave in comando:
            return resposta

            return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()