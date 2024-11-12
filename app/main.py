from services.usuario_services import UsuarioService
from repositories.usuario_repositories import UsuarioRepositorie
from config.database import Session
import os 

def main():
    session = Session()
    repository = UsuarioRepositorie(session)
    service = UsuarioService(repository)
    
    # Tabela com números   
    print("=== SENAI SOLUTION ===")
    print("\n1 - Adicionar usuário")
    print("\n2 - Pesquisar um usuário")
    print("\n3 - Atualizar dados de um usuário")
    print("\n4 - Excluir um usuário")
    print("\n5 - Exibir todos os usuários cadastrados") 
    print("\n0 - Sair")
        
    escolha = input("Selecione um número: ")
    while escolha != "0":

        # Solicitando dados do usuário.
        if escolha == "1":
            print("\nAdicionando usuário: ")
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")
            cpf = input("Digite o CPF do usuário: ")

            service.criar_usuario(nome=nome, email=email, senha=senha, cpf=cpf)
            print("Usuário adicionado com sucesso.")

        # Pesquisando usuario por cpf
        elif escolha == "2":
            pesquisar_cpf = input("Digite o CPF de quem deseja buscar: ")
            usuario_procurado = repository.pesquisar_usuario_por_cpf(pesquisar_cpf)

            if usuario_procurado is None:
                print("Usuário não encontrado no sistema.")
            else:
                print(f"\nNome: {usuario_procurado.nome} \nEmail: {usuario_procurado.email} \nSenha: {usuario_procurado.senha}")
                print("Usuário encontrado.") 

        # Atualizar dados do usuario
        elif escolha == "3":
            cpf = input("Digite o CPF do usuário que deseja atualizar: ")
            nome = input("Digite o novo nome do usuário (ou deixe em branco para não alterar): ")
            email = input("Digite o novo email do usuário (ou deixe em branco para não alterar): ")
            senha = input("Digite a nova senha do usuário (ou deixe em branco para não alterar): ")

            service.atualizar_usuario(cpf=cpf, nome=nome if nome else None, email=email if email else None, senha=senha if senha else None)
        

        # Removendo usuário
        elif escolha == "4":
            while True:
                remover = input(f"\nDeseja remover algum usuário? (sim/não): ")
                if remover == "sim":
                    nome_usuario = input("Digite o nome do usuário que deseja remover: ")

                    # Buscar e remover o usuário pelo nome
                    usuario_para_remover = repository.pesquisar_usuario_por_nome(nome_usuario)
                    if usuario_para_remover:
                        service.excluir_usuario(usuario_para_remover)  
                        print("\nUsuário removido com sucesso.")
                    else:
                        print("\nUsuário não encontrado.")
                else:
                    print("\nFinalizando as remoções.")
                    break

            # Exibindo a lista de usuários após a remoção para confirmação
            print("\nListando usuários após a remoção: ")
            lista_usuario = service.listar_todos_usuarios()
            for usuario in lista_usuario:
                print(f"\nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")

        elif escolha == "5":
            # Exibindo todos os usuários cadastrados.
            print("\nListando usuários cadastrados: ")
            lista_usuario = service.listar_todos_usuarios()
            for usuario in lista_usuario:
                print(f"\nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha} \nCPF: {usuario.cpf}")
        
        # Finalizar programa
        elif escolha == "0":
            break
        
        else:
            print("Opção inválida. Tente novamente.")

        print("\n=== SENAI SOLUTION ===")
        print("\n1 - Adicionar usuário")
        print("\n2 - Pesquisar um usuário")
        print("\n3 - Atualizar dados de um usuário")
        print("\n4 - Excluir um usuário")
        print("\n5 - Exibir todos os usuários cadastrados") 
        print("\n0 - Sair")
        
        escolha = input("Selecione um número: ")
        

if __name__ == "__main__":
    os.system("cls || clear")
    main()

