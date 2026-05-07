@startuml
left to right direction

actor Funcionario
actor Espectador

rectangle "Redes de Cinema" {

  Funcionario -- (Cadastrar filme)
  Funcionario -- (Programar sessão)
  Funcionario -- (Cadastrar unidade de cinema)
  Funcionario -- (Registrar ingressos vendidos)



  Espectador -- (Consultar filme em cartaz atualmente)
  (Consultar filme em cartaz atualmente) ..> (Verificar informações) : <<include>>


}
@enduml



![alt text](image.png)