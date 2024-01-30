import requests

def obter_previsao_tempo(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}"

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        return dados
    else:
        print(f"Falha na solicitação. Código de status: {resposta.status_code}")
        return None

def exibir_previsao_tempo(previsao):
    if previsao:
        temperatura_kelvin = previsao["main"]["temp"]
        temperatura_celsius = temperatura_kelvin - 273.15
        descricao = previsao["weather"][0]["description"]

        print(f"Temperatura: {temperatura_celsius:.2f}°C")
        print(f"Descrição: {descricao}")
    else:
        print("Não foi possível obter a previsão do tempo.")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    chave_api = input("Digite sua chave de API do OpenWeatherMap: ")

    previsao = obter_previsao_tempo(cidade, chave_api)
    exibir_previsao_tempo(previsao)