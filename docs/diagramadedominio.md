classDiagram
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


    %% Relacionamentos
    Cinema "1" -- "*" Sessao : realiza >
    Filme "1" -- "*" Sessao : exibido em >
    Filme "*" -- "*" Ator : possui elenco >
