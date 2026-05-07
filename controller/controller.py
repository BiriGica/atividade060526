from service import RegistroPublicoService

class RegistroPublicoController:
    def __init__(self):
        self.service = RegistroPublicoService()

    def registrar_publico(self, sessao_id_raw, quantidade_raw):
        try:
            s_id = int(sessao_id_raw)
            qtd = int(quantidade_raw)
            
            if qtd <= 0:
                return {"status": 400, "mensagem": "A quantidade deve ser positiva."}

            resultado = self.service.processar_registro_publico(s_id, qtd)
            return {"status": 200 if resultado["sucesso"] else 400, "mensagem": resultado["mensagem"]}
        
        except ValueError:
            return {"status": 400, "mensagem": "Erro: Digite  números inteiros."}