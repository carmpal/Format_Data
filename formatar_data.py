from datetime import datetime

def format_date():
    date_str = input("Digite a data no formato AAAA-MM-DD: ")
    try:
        # Converte a string de data para um objeto datetime
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Formata o objeto datetime para uma string no formato desejado
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        return "Data inválida"

# Exemplo de uso
print(format_date())
