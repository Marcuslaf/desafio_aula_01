import json
import os
from typing import List, Dict, Union

class GerenciadorUsuarios:
    def __init__(self, arquivo: str = "usuarios.json"):
        self.arquivo = arquivo

    def _carregar_usuarios(self) -> List[Dict[str, Union[str, int]]]:
        """Carrega os usuários do arquivo JSON."""
        if not os.path.exists(self.arquivo):
            return []
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro: Arquivo JSON corrompido. Criando novo arquivo.")
            return []

    def _salvar_usuarios(self, usuarios: List[Dict[str, Union[str, int]]]) -> None:
        """Salva os usuários no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    def criar_arquivo(self) -> None:
        """Cria um novo arquivo JSON com dados iniciais."""
        if os.path.exists(self.arquivo):
            resposta = input("Arquivo já existe. Deseja sobrescrever? (s/n): ").lower()
            if resposta != 's':
                print("Operação cancelada.")
                return

        usuarios_iniciais = [
            {"nome": "João", "idade": 25, "email": "joao@email.com"},
            {"nome": "Maria", "idade": 30, "email": "maria@email.com"}
        ]
        self._salvar_usuarios(usuarios_iniciais)
        print("Arquivo JSON criado com sucesso!")

    def adicionar_usuario(self) -> None:
        """Adiciona um novo usuário ao arquivo."""
        usuarios = self._carregar_usuarios()

        try:
            nome = input("Digite o nome do usuário: ").strip()
            if not nome:
                raise ValueError("O nome não pode estar vazio.")

            idade = int(input("Digite a idade do usuário: "))
            if idade < 0 or idade > 150:
                raise ValueError("Idade inválida.")

            email = input("Digite o email do usuário: ").strip()
            if not "@" in email or not "." in email:
                raise ValueError("Email inválido.")

            # Verifica se o email já existe
            if any(usuario["email"] == email for usuario in usuarios):
                raise ValueError("Este email já está cadastrado.")

            novo_usuario = {
                "nome": nome,
                "idade": idade,
                "email": email
            }
            usuarios.append(novo_usuario)
            self._salvar_usuarios(usuarios)
            print("Usuário adicionado com sucesso!")

        except ValueError as e:
            print(f"Erro: {str(e)}")

    def exibir_usuarios(self) -> None:
        """Exibe todos os usuários cadastrados."""
        usuarios = self._carregar_usuarios()
        
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        print("\nUsuários registrados:")
        print("-" * 50)
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Email: {usuario['email']}")
            print("-" * 50)
        print(f"Total de usuários: {len(usuarios)}")

    def buscar_usuario(self) -> None:
        """Busca um usuário por nome ou email."""
        usuarios = self._carregar_usuarios()
        termo = input("Digite o nome ou email para buscar: ").strip().lower()
        
        encontrados = [
            usuario for usuario in usuarios
            if termo in usuario["nome"].lower() or termo in usuario["email"].lower()
        ]
        
        if encontrados:
            print("\nUsuários encontrados:")
            print("-" * 50)
            for usuario in encontrados:
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Email: {usuario['email']}")
                print("-" * 50)
        else:
            print("Nenhum usuário encontrado.")

    def remover_usuario(self) -> None:
        """Remove um usuário pelo nome."""
        usuarios = self._carregar_usuarios()
        nome = input("Digite o nome do usuário que deseja remover: ").strip()
        
        usuarios_com_mesmo_nome = [u for u in usuarios if u["nome"].lower() == nome.lower()]
        
        if not usuarios_com_mesmo_nome:
            print("Usuário não encontrado.")
            return
            
        if len(usuarios_com_mesmo_nome) > 1:
            print("\nForam encontrados múltiplos usuários com esse nome:")
            for i, usuario in enumerate(usuarios_com_mesmo_nome, 1):
                print(f"\n{i}.")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Email: {usuario['email']}")
            
            try:
                escolha = int(input("\nDigite o número do usuário que deseja remover (0 para cancelar): "))
                if escolha == 0:
                    print("Operação cancelada.")
                    return
                if escolha < 1 or escolha > len(usuarios_com_mesmo_nome):
                    print("Número inválido. Operação cancelada.")
                    return
                
                usuario_remover = usuarios_com_mesmo_nome[escolha - 1]
            except ValueError:
                print("Entrada inválida. Operação cancelada.")
                return
        else:
            usuario_remover = usuarios_com_mesmo_nome[0]
            confirmacao = input(f"Confirma a remoção do usuário {usuario_remover['nome']} "
                              f"({usuario_remover['email']})? (s/n): ").lower()
            if confirmacao != 's':
                print("Operação cancelada.")
                return
        
        usuarios = [u for u in usuarios if u != usuario_remover]
        self._salvar_usuarios(usuarios)
        print("Usuário removido com sucesso!")

def main():
    gerenciador = GerenciadorUsuarios()
    
    menu_opcoes = {
        "1": ("Criar arquivo JSON", gerenciador.criar_arquivo),
        "2": ("Adicionar usuário", gerenciador.adicionar_usuario),
        "3": ("Exibir usuários", gerenciador.exibir_usuarios),
        "4": ("Buscar usuário", gerenciador.buscar_usuario),
        "5": ("Remover usuário", gerenciador.remover_usuario),
        "6": ("Sair", None)
    }

    print("Bem-vindo ao Gerenciador de Usuários JSON!")
    
    while True:
        print("\nEscolha uma opção:")
        for key, (descricao, _) in menu_opcoes.items():
            print(f"{key}. {descricao}")

        opcao = input("\nDigite sua escolha: ").strip()

        if opcao not in menu_opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == "6":
            print("Saindo... Até mais!")
            break

        try:
            menu_opcoes[opcao][1]()
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    main()