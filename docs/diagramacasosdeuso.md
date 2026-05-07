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
<img width="725" height="435" alt="image" src="https://github.com/user-attachments/assets/0486215e-7a06-4f25-bedb-4e94f3033070" />



