
#entrada de dados
#A entrada formato "yyyy-mm-dd" (exemplo: 2024-12-25). Saida formato "dd/mm/yyyy". 
# Se a entrada não estiver no formato correto, deve ser retornada a mensagem "Formato de data inválido.

#entrada de dados
#A entrada formato "yyyy-mm-dd" (exemplo: 2024-12-25). Saida formato "dd/mm/yyyy". 
# Se a entrada não estiver no formato correto, deve ser retornada a mensagem "Formato de data inválido."

data_input = input("Digite a data no formato yyyy-mm-dd: ")

def converter_para_dia_mes_ano(data_str):
    try:
        ano, mes, dia = data_str.split("-")
        return f"{dia}/{mes}/{ano}"
    except ValueError:
        return "Formato de data inválido"

if len(data_input) == 10 and data_input[4] == '-' and data_input[7] == '-':
    print(converter_para_dia_mes_ano(data_input))
else:
    print("Formato de data inválido")
    