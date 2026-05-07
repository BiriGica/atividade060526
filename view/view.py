from controller import RegistroPublicoController
from database import inicializar_banco

class View:
    def __init__(self):
        self.controller = RegistroPublicoController()

    def exibir_menu(self):
        print("\n--- SISTEMA DE GESTÃO DE CINEMAS ---")
        print("Caso de Uso: Registrar Público")
        
        sid = input("ID da Sessão: ")
        qtd = input("Quantidade de novos espectadores: ")

        resposta = self.controller.registrar_publico(sid, qtd)
        
        if resposta["status"] == 200:
            print(f"\n[OK] {resposta['mensagem']}")
        else:
            print(f"\n[ERRO] {resposta['mensagem']}")

if __name__ == "__main__":
    inicializar_banco()
    
    tela = View()
    while True:
        tela.exibir_menu()
        if input("\nDeseja realizar outro registro? (s/n): ").lower() != 's':
            break