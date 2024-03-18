class Carro:
    def __init__(self, nome, tipo, consumo, capacidade, preco, combustivel, tracao):
        self.nome = nome
        self.tipo = tipo
        self.consumo = consumo
        self.capacidade = capacidade
        self.preco = preco
        self.combustivel = combustivel
        self.tracao = tracao


carros_por_tipo = {
    "Híbrido": [
        Carro("Toyota Prius", "Híbrido", 25, 5, 30000, "Híbrido", "Frente"),

    ],
    "Sedan": [
        Carro("Honda Civic", "Sedan", 30, 5, 25000, "Gasolina", "Frente"),
        Carro("Nissan Altima", "Sedan", 27, 5, 27000, "Gasolina", "Frente"),

    ],
    "SUV": [
        Carro("Ford Explorer", "SUV", 20, 7, 40000, "Gasolina", "AWD"),
        Carro("Mazda CX-5", "SUV", 28, 5, 35000, "Gasolina", "AWD"),

    ],
    "Compacto": [
        Carro("Chevrolet Spark", "Compacto", 35, 4, 15000, "Gasolina", "Frente"),
        Carro("Volkswagen Golf", "Compacto", 32, 4, 20000, "Gasolina", "Frente"),

    ],

}


def calcular_aluguel(carro):
    return carro.preco * 0.02


def recomendar_carro(preferencias):
    carros_filtrados = []

    for lista_carros in carros_por_tipo.values():
        for carro in lista_carros:
            aluguel = calcular_aluguel(carro)
            if (
                (preferencias.get("tipo") is None or preferencias["tipo"].lower() == carro.tipo.lower())
                and (preferencias["consumo"] is None or preferencias["consumo"] >= carro.consumo)
                and (preferencias["capacidade"] is None or preferencias["capacidade"] == carro.capacidade)
                and (preferencias["combustivel"] is None or preferencias["combustivel"].lower() == carro.combustivel.lower())
                and (preferencias["tracao"] is None or preferencias["tracao"].lower() == carro.tracao.lower())
                and (preferencias.get("aluguel_max") is None or preferencias["aluguel_max"] >= aluguel)
            ):
                carro.aluguel = aluguel
                carros_filtrados.append(carro)

    return carros_filtrados



preferencias_usuario = {
    "tipo": None ,
    "aluguel_max": None,
    "consumo": None,
    "capacidade": None,
    "combustivel": None,
    "tracao": None,
}

resultados = recomendar_carro(preferencias_usuario)

if resultados:
    print("Carros Disponíveis:")
    for carro in resultados:
        print(f"\n{carro.nome} - Tipo: {carro.tipo}, Tração: {carro.tracao} Consumo: {carro.consumo} km/l, Combustível: {carro.combustivel}, Capacidade: {carro.capacidade}, Aluguel/Dia: ${carro.aluguel:.2f}")
else:
    print("Nenhum carro disponível.")