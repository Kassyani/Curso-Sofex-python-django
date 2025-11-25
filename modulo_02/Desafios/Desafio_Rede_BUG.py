#Autor: Kassyani Mênedy 
#Data: 24/11/2025
#Função: Simulador de Rede Social - Tema Enfermagem


print("Bem-vindo ao Simulador de Rede Social!")



class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido


class Post:
    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono


class RedeSocial:
    def __init__(self):
        self.banco_de_posts = []

    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        print(f"   Post criado por {usuario_logado.apelido}!")

    def ver_meu_perfil(self, usuario_logado):
        print(f"\n       --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f"     Usuário: {usuario_logado.apelido}")
        print("-" * 30)

        encontrou_algo = False

        for post in self.banco_de_posts:
            if post.dono == usuario_logado:
                print(f"             {post.texto} (Postado por: {post.dono.apelido})")
                encontrou_algo = True

        if not encontrou_algo:
            print("   (Nenhum post encontrado)")

        print("-" * 30 + "\n")



usuario_principal = Usuario("Kassyani Menedy", "@enf.kassy")


usuario_secundario = Usuario("Dr. Gustavo", "@dr.guto")

minha_rede_social = RedeSocial()

minha_rede_social.criar_post("Plantão começando e eu já sonhando com a minha cama!", usuario_principal)
minha_rede_social.criar_post("Alguém sabe onde deixaram o oxímetro? Sumiu de novo!", usuario_secundario)
minha_rede_social.criar_post("A arte de parecer calma mesmo quando o monitor dispara  #Enfermagem", usuario_principal)
minha_rede_social.criar_post("Se eu sumir, estou pegando um café.", usuario_secundario)
minha_rede_social.criar_post("Quando o paciente diz 'enfermeira, rapidinho' eu já sei que não vai ser rapidinho ", usuario_principal)


print("\n--- TESTANDO SEU CÓDIGO ---")
minha_rede_social.ver_meu_perfil(usuario_principal)
