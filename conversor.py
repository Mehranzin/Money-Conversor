import requests

def converter_moeda(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API.")
        return None

    dados = resposta.json()
    print("DEBUG - Resposta da API:", dados)

    if 'rates' in dados and para in dados['rates']:
        return dados['rates'][para]
    else:
        print("Erro: moeda inválida ou resposta inesperada.")
        return None

def main():
    print("=== Conversor de Moedas ===")
    valor = float(input("Valor a converter: "))
    de = input("De qual moeda? (ex: USD): ").upper()
    para = input("Para qual moeda? (ex: BRL): ").upper()

    resultado = converter_moeda(valor, de, para)

    if resultado is not None:
        print(f"\n{valor:.2f} {de} = {resultado:.2f} {para}")
    else:
        print("Conversão falhou.")

if __name__ == "__main__":
    main()
