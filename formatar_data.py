
#entrada de dados
#A entrada formato "yyyy-mm-dd" (exemplo: 2024-12-25). Saida formato "dd/mm/yyyy". 
# Se a entrada não estiver no formato correto, deve ser retornada a mensagem "Formato de data inválido.

def converter_data(data_iso):
    try:
        # Verifica se a entrada está no formato correto "yyyy-mm-dd"
        partes = data_iso.split('-')
        if len(partes) == 3 and len(partes[0]) == 4 and len(partes[1]) == 2 and len(partes[2]) == 2:
            # Reorganiza as partes para o formato "dd/mm/yyyy"
            data_convertida = f"{partes[2]}/{partes[1]}/{partes[0]}"
            return data_convertida
        else:
            return "Formato de data inválido"
    except:
        return "Formato de data inválido"

# Exemplo de uso
data = "2024-12-25"
data_formatada = converter_data(data)
print(data_formatada)  # Output: 25/12/2024

# Exemplo de entrada inválida
data_invalida = "2024-25-12"
resultado_invalido = converter_data(data_invalida)
print(resultado_invalido)  
