temperatures = [8, 12, 15, 19.2, 25, 28, 29, 30, 40, 14]

print(min(temperatures))
print(max(temperatures))

def calc_temperatura_media(array_de_temperaturas):
    quantidade_de_temperaturas = 0
    soma_das_temperaturas = 0

    for temperature in array_de_temperaturas:
        quantidade_de_temperaturas += 1
        soma_das_temperaturas += temperature
    

    temperatura_media = soma_das_temperaturas / quantidade_de_temperaturas
    return print(f"A temperatura média é de: {temperatura_media}ºC")

if __name__ == "__main__":
    calc_temperatura_media(temperatures)
