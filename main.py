from database import inicializar_banco
from view import View

def main():
    print("Iniciando o Sistema de Gestão de Cinemas...")
    
    inicializar_banco()
    
    tela = View()
    
    while True:
        tela.exibir_menu()
        
        continuar = input("\nDeseja realizar outro registro? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nEncerrando o sistema. Até logo!")
            break

if __name__ == "__main__":
    main()