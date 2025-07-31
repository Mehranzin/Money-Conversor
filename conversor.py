import requests

def converter_moeda(valor, de, para):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de}&to={para}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("❌ Erro ao acessar a API.")
        return None, None

    dados = resposta.json()

    if 'rates' in dados and para in dados['rates']:
        taxa = dados['rates'][para]
        return taxa, dados['date']
    else:
        print("❌ Moeda inválida ou resposta inesperada.")
        return None, None

def main():
    print("=== Conversor de Moedas ===")
    try:
        valor = float(input("Valor a converter: "))
        de = input("De qual moeda? (ex: USD): ").strip().upper()
        para = input("Para qual moeda? (ex: BRL): ").strip().upper()

        resultado, data = converter_moeda(valor, de, para)

        if resultado is not None:
            print(f"\n✅ {valor:.2f} {de} = {resultado:.2f} {para} (Data: {data})")
            print(f"💱 Taxa usada: 1 {de} = {resultado / valor:.4f} {para}")
        else:
            print("Conversão falhou.")

    except ValueError:
        print("❌ Valor inválido. Use apenas números.")

if __name__ == "__main__":
    main()
