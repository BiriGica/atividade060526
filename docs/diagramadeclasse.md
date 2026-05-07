@startuml

skinparam ClassAttributeIconSize 0

    class Cinema {
        nome
        capacidadeMaxima
        cidade
        estado
        enderecoCompleto
    }

    class Filme {
        titulo
        duracaoMinutos
        genero
        statusEmCartaz
    }

    class Sessao {
        data
        horario
        publicoRegistrado
    }

    class Ator {
        nome
        biografia
    }



Cinema "1" -- "*" Sessao : realiza >
Filme "1" -- "*" Sessao : exibido em >
Filme "*" -- "*" Ator : possui elenco >

@enduml


<img width="375" height="328" alt="image" src="https://github.com/user-attachments/assets/926c079e-aab3-4392-8ffc-7d3b526f953b" />
