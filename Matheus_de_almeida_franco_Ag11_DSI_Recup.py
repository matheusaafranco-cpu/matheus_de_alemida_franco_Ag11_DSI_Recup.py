"""
Atividade de Recuperação - Agenda 11
Curso Técnico em Desenvolvimento de Sistemas
Estudante: Matheus de Almeida Franco (Paulo)
Sistema de Monitoramento de Níveis de Água com Colorama
"""

from colorama import init, Fore, Style

# Inicializa o colorama para garantir compatibilidade no terminal
init(autoreset=True)

def definir_cor_alerta(nivel: int) -> str:
    """
    Define a cor e a formatação do texto com base no nível do reservatório.
    Recebe um inteiro de 1 a 5 e retorna a string formatada com colorama.
    """
    if nivel == 1:
        # Nível 1: Muito baixo (crítico) - Vermelho
        return f"{Fore.RED}{Style.BRIGHT}[NÍVEL 1] Muito baixo (crítico) - Risco Iminente!"
    elif nivel == 2:
        # Nível 2: Baixo - Amarelo
        return f"{Fore.YELLOW}{Style.BRIGHT}[NÍVEL 2] Baixo - Atenção necessária."
    elif nivel == 3:
        # Nível 3: Médio - Verde
        return f"{Fore.GREEN}{Style.BRIGHT}[NÍVEL 3] Médio - Operação Estável."
    elif nivel == 4:
        # Nível 4: Alto - Ciano
        return f"{Fore.CYAN}{Style.BRIGHT}[NÍVEL 4] Alto - Monitorando fluxo."
    elif nivel == 5:
        # Nível 5: Muito alto (alerta) - Azul
        return f"{Fore.BLUE}{Style.BRIGHT}[NÍVEL 5] Muito alto (alerta) - Capacidade máxima próxima!"
    else:
        return f"{Fore.WHITE}[ERRO] Nível desconhecido."

def simular_monitoramento():
    """
    Simula o monitoramento do reservatório percorrendo os 5 níveis definidos.
    """
    print("==================================================")
    print("     SISTEMA DE MONITORAMENTO DE RESERVATÓRIO     ")
    print("==================================================\n")

    # Lista contendo os 5 níveis do reservatório
    niveis_reservatorio = [1, 2, 3, 4, 5]

    for nivel in desestruturar := niveis_reservatorio:
        mensagem_alerta = definir_cor_alerta(nivel)
        print(f"Status Atual: {mensagem_alerta}")
    
    print("\n==================================================")
    print("Simulação concluída. Estilos do terminal restaurados.")
    print("==================================================")

if __name__ == "__main__":
    simular_monitoramento()