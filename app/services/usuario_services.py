from models.usuario_models import Usuario
from repositories.usuario_repositories import UsuarioRepositorie

class UsuarioService:
    def __init__(self, repository: UsuarioRepositorie):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str, cpf: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf)

            cadastrado = self.repository.pesquisar_usuario_por_cpf(cpf=usuario.cpf)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro: 
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")


    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuario()
    

    def excluir_usuario(self, usuario: Usuario):
        "Excluiu um usuário do banco de dados."
        try:
            self.repository.excluir_usuario(usuario)
            print("Usuário excluído com sucesso!")
        except Exception as erro:
            print(f"Erro ao excluir o usuário: {erro}")


    def pesquisar_usuario_por_cpf(self, cpf: str):
        "Pesquisa um usuário pelo CPF no banco de dados."
        try:
            usuario = self.repository.pesquisar_usuario_por_cpf(cpf)
            if usuario:
                print("Usuário localizado!")
                return usuario
            else:
                print("Usuário não encontrado!")
                return None
        except Exception as erro:
            print(f"Erro ao pesquisar o usuário: {erro}")
            return None


    def atualizar_usuario(self, cpf: str, nome: str = None, email: str = None, senha: str = None):
            "Atualiza os dados do usuário com o CPF fornecido."
            try:
                usuario = self.repository.pesquisar_usuario_por_cpf(cpf)
                if not usuario:
                    print("Usuário não encontrado!")
                    return

                # Atualização dos dados
                if nome:
                    usuario.nome = nome
                if email:
                    usuario.email = email
                if senha:
                    usuario.senha = senha

                # Salva as mudanças 
                self.repository.atualizar_usuario(usuario)
                print("Dados do usuário atualizados com sucesso!")
            except Exception as erro:
                print(f"Erro ao atualizar o usuário: {erro}")