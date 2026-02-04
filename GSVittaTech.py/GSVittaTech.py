# Função para exibir o menu principal
def exibir_menu():
    """
    Exibe o menu principal com as opções que o usuário pode escolher.
    """
    print("===== Plataforma de Cursos - Conhecimento é o que move tudo! =====")
    print("Escolha uma das opções abaixo para começar sua jornada de aprendizado:")
    print("1. Ver cursos disponíveis")
    print("2. Sobre a plataforma")
    print("3. Sair")


# Função para exibir os cursos disponíveis
def exibir_cursos():
    """
    Exibe uma lista de cursos disponíveis na plataforma.
    Cada curso possui nome, descrição, carga horária, preço, nível
    e pré-requisitos.
    """

    # Lista de cursos disponíveis
    cursos = [
        {
            "nome": "Inteligência Artificial",
            "descricao": "Fundamentos, aplicações e futuro da IA.",
            "carga_horaria": "60h",
            "preco": "R$ 499,90",
            "nivel": "Avançado",
            "pre_requisitos": "Lógica de programação e matemática básica"
        },
        {
            "nome": "Programação",
            "descricao": "Aprenda Python, Java e lógica de programação.",
            "carga_horaria": "80h",
            "preco": "R$ 399,90",
            "nivel": "Iniciante",
            "pre_requisitos": "Nenhum"
        },
        {
            "nome": "Soft Skills",
            "descricao": "Comunicação, liderança e trabalho em equipe.",
            "carga_horaria": "40h",
            "preco": "R$ 199,90",
            "nivel": "Intermediário",
            "pre_requisitos": "Interesse em desenvolvimento pessoal"
        },
        {
            "nome": "Segurança da Informação",
            "descricao": "Proteção de dados, criptografia e ética digital.",
            "carga_horaria": "70h",
            "preco": "R$ 549,90",
            "nivel": "Avançado",
            "pre_requisitos": "Conhecimento em redes e sistemas operacionais"
        },
        {
            "nome": "UX/UI Design",
            "descricao": "Design centrado no usuário, prototipação e testes.",
            "carga_horaria": "50h",
            "preco": "R$ 299,90",
            "nivel": "Iniciante",
            "pre_requisitos": "Nenhum"
        },
        {
            "nome": "Data Science",
            "descricao": "Estatística, Machine Learning e análise de dados.",
            "carga_horaria": "90h",
            "preco": "R$ 699,90",
            "nivel": "Avançado",
            "pre_requisitos": "Python e estatística"
        },
    ]

    print("===== Cursos Disponíveis =====")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso['nome']} - {curso['nivel']} - {curso['preco']}")

    print("Escolha um curso para mais informações (1-6) ou 0 para voltar ao menu principal.")
    escolha = input("Digite a opção: ")

    # Verificando a escolha do usuário
    if escolha.isdigit() and 1 <= int(escolha) <= len(cursos):
        curso_escolhido = cursos[int(escolha) - 1]
        print(f" Curso selecionado: {curso_escolhido['nome']}")
        print(f"Descrição: {curso_escolhido['descricao']}")
        print(f"Carga horária: {curso_escolhido['carga_horaria']}")
        print(f"Nível: {curso_escolhido['nivel']}")
        print(f"Preço: {curso_escolhido['preco']}")
        print(f"Pré-requisitos: {curso_escolhido['pre_requisitos']}")
    elif escolha == "0":
        return
    else:
        print("Opção inválida. Por favor, tente novamente.")

    input("Pressione Enter para voltar ao menu principal.")


# Sobre a plataforma
def sobre_plataforma():
    """
    Exibe informações gerais sobre o sistema.
    """
    print("===== Sobre a Plataforma =====")
    print("Esta plataforma foi desenvolvida para demonstrar conceitos básicos de Python,")
    print("como funções, listas, laços de repetição, condicionais e interação com o usuário.")
    print("O objetivo é facilitar o acesso a informações de cursos de forma simples e intuitiva.")
    input("Pressione Enter para voltar ao menu principal.")


# Função principal que gerencia o fluxo da plataforma
def main():
    """
    Função principal que executa o menu e gerencia a interação do usuário com a plataforma.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cursos()
        elif opcao == "2":
            sobre_plataforma()
        elif opcao == "3":
            print("Obrigado por visitar a Plataforma de Cursos. Até logo! ")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


# Inicia o sistema
if __name__ == "__main__":
    main()
