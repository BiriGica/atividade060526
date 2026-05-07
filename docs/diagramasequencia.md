@startuml
actor "Funcionário" as Funcionario
participant "Interface" as V
participant "Controller" as C
participant "Service" as S
participant "Repository" as R

Funcionario -> V: Insere público da Sessão (Ex: 150)
V -> C: registrarPublico(sessaoId, quantidade)

' O Controller repassa a responsabilidade para o Service
C -> S: processarRegistroPublico(sessaoId, quantidade)

' O Service busca os dados atuais para validar a regra de negócio
S -> R: buscarDadosSessaoECinema(sessaoId)
R --> S: retorna Dados (capacidadeMaxima, etc)

note over S: Verifica se quantidade <= capacidadeMaxima

' Persistência de dados
S -> R: atualizarPublico(sessaoId, quantidade)
R --> S: confirmacaoDeSucesso

' Retorno do fluxo para o usuário
S --> C: registroProcessadoComSucesso
C --> V: status(200 OK)
V --> Funcionario: Exibe mensagem "Público salvo com sucesso!"
@enduml

<img width="1142" height="500" alt="image" src="https://github.com/user-attachments/assets/091cd18f-b392-4770-bc6b-6d76671e0c09" />
