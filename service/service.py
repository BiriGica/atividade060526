from repository import RegistroPublicoRepository

class RegistroPublicoService:
    def __init__(self):
        self.repository = RegistroPublicoRepository()

    def processar_registro_publico(self, sessao_id, quantidade_nova):
        dados = self.repository.buscar_dados_sessao_e_cinema(sessao_id)
        
        if not dados:
            return {"sucesso": False, "mensagem": "Sessão não encontrada."}

        capacidade = dados["capacidade_maxima"]
        publico_atual = dados["publico_registrado"]
        total_apos_registro = publico_atual + quantidade_nova

        if total_apos_registro > capacidade:
            return {
                "sucesso": False, 
                "mensagem": f"Erro: Capacidade máxima ({capacidade}) seria excedida. Total atual: {publico_atual}"
            }

        if self.repository.atualizar_publico(sessao_id, total_apos_registro):
            return {"sucesso": True, "mensagem": f"Público atualizado! Total agora: {total_apos_registro}"}
        
        return {"sucesso": False, "mensagem": "Erro técnico ao acessar o banco."}