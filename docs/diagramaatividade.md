@startuml
start
:Acessar sistema;

if (Qual operação deseja realizar?) then (Programar Sessão)
  :Selecionar filme e cinema;
  
  label input_hora
  :Definir data e hora;
  
  if (Conflito de horário?) then (Sim)
    :Exibir erro;
    goto input_hora
  else (Não)
    :Salvar sessão;
  endif

else (Registrar Público)
  :Selecionar sessão finalizada;

  label input_publico
  :Informar total de ingressos vendidos;
  
  if (Público > Capacidade?) then (Sim)
    :Exibir erro;
    goto input_publico
  else (Não)
    :Marcar registro;
    endif

endif

stop
@enduml


<img width="528" height="440" alt="image" src="https://github.com/user-attachments/assets/dc22636b-4f9d-4758-a178-654bc4ffe7a5" />
