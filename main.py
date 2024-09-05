from typing import List, Dict, Optional, Callable

Contato = Dict[str, Optional[str]]  # Define um tipo para o contato

def criar_contato(nome: str, telefone: str, email: str, favorito: bool) -> Contato:
    return {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }

def listar_contatos(contatos: List[Contato]) -> None:
    if not contatos:
        print("\nNenhum contato cadastrado.")
    else:
        print("\nLista de contatos:")
        for i, contato in enumerate(contatos, start=1):
            favorito_str = "Sim" if contato["favorito"] else "Não"
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {favorito_str}")

def adicionar_contato(contatos: List[Contato]) -> List[Contato]:
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    favorito = input("Favorito (s/n)? ").lower() == 's'
    novo_contato = criar_contato(nome, telefone, email, favorito)
    print("\nContato adicionado com sucesso!")
    return contatos + [novo_contato]

def editar_contato(contatos: List[Contato]) -> List[Contato]:
    listar_contatos(contatos)
    indice = int(input("\nEscolha o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
        contato_atualizado = criar_contato(
            nome=input(f"Nome ({contatos[indice]['nome']}): ") or contatos[indice]['nome'],
            telefone=input(f"Telefone ({contatos[indice]['telefone']}): ") or contatos[indice]['telefone'],
            email=input(f"Email ({contatos[indice]['email']}): ") or contatos[indice]['email'],
            favorito=contatos[indice]['favorito']
        )
        print("\nContato atualizado com sucesso!")
        return [contato_atualizado if i == indice else contato for i, contato in enumerate(contatos)]
    else:
        print("Contato inválido!")
        return contatos

def marcar_favorito(contatos: List[Contato]) -> List[Contato]:
    listar_contatos(contatos)
    indice = int(input("\nEscolha o número do contato para marcar/desmarcar como favorito: ")) - 1
    if 0 <= indice < len(contatos):
        contato = contatos[indice]
        contato_atualizado = {**contato, "favorito": not contato["favorito"]}
        status = "favorito" if contato_atualizado["favorito"] else "não favorito"
        print(f"\nContato marcado como {status}.")
        return [contato_atualizado if i == indice else contato for i, contato in enumerate(contatos)]
    else:
        print("Contato inválido!")
        return contatos

def listar_favoritos(contatos: List[Contato]) -> None:
    favoritos = list(filter(lambda c: c["favorito"], contatos))
    if not favoritos:
        print("\nNenhum contato favorito.")
    else:
        print("\nContatos favoritos:")
        listar_contatos(favoritos)

def apagar_contato(contatos: List[Contato]) -> List[Contato]:
    listar_contatos(contatos)
    indice = int(input("\nEscolha o número do contato que deseja apagar: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos[indice]
        print(f"\nContato '{removido['nome']}' apagado com sucesso!")
        return [contato for i, contato in enumerate(contatos) if i != indice]
    else:
        print("Contato inválido!")
        return contatos

def menu() -> None:
    contatos: List[Contato] = []
    opcoes: Dict[str, Callable[[List[Contato]], List[Contato]]] = {
        '1': adicionar_contato,
        '2': editar_contato,
        '3': marcar_favorito,
        '6': apagar_contato
    }
    
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Editar contato")
        print("3. Marcar/Desmarcar favorito")
        print("4. Listar contatos")
        print("5. Listar favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha in opcoes:
            contatos = opcoes[escolha](contatos)
        elif escolha == '4':
            listar_contatos(contatos)
        elif escolha == '5':
            listar_favoritos(contatos)
        elif escolha == '7':
            print("Saindo da aplicação...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
