# Solicitando a quantidade de desastres
quantidade_desastres = int(input("Digite a quantidade de desastres registrados: "))

# Inicializando a listas para armazenar informações sobre os desastres
tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
qt_pessoas_afetadas = []

# Quantidade de pessoas afetadas por categoria
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

# Coletando as informações de cada desastre
for i in range(quantidade_desastres):
    print(f"\nDesastre {i + 1}:")
    tipo = input("Tipo de desastre (ex: incêndio, enchente, etc.): ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")
    total_afetadas = int(input("Quantidade total de pessoas afetadas: "))

    # Coletando a quantidade de pessoas por categoria
    n_criancas = int(input("Quantidade de crianças afetadas: "))
    n_adultos = int(input("Quantidade de adultos afetados: "))
    n_idosos = int(input("Quantidade de idosos afetados: "))
    n_mobilidade_reduzida = int(input("Quantidade de pessoas com mobilidade reduzida afetadas: "))
    n_feridos = int(input("Quantidade de feridos: "))

    # Calculando a soma das categorias para validação
    soma_categorias = n_criancas + n_adultos + n_idosos + n_mobilidade_reduzida + n_feridos
    if soma_categorias > total_afetadas:
        print("A quantidade total de pessoas afetadas não pode ser menor que a soma das categorias.")
        continue

    # Armazena as informações nas listas respectivas
    tipos_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    qt_pessoas_afetadas.append(total_afetadas)
    criancas.append(n_criancas)
    adultos.append(n_adultos)
    idosos.append(n_idosos)
    mobilidade_reduzida.append(n_mobilidade_reduzida)
    feridos.append(n_feridos)

# Exibe as informações coletadas
for i in range(quantidade_desastres):
    print(f"\nRelatório do Desastre {i + 1}:")
    print(f"Tipo: {tipos_desastres[i]}")
    print(f"Localização: {ruas[i]}, {bairros[i]}, {cidades[i]}, {paises[i]}")
    print(f"Pessoas afetadas: {qt_pessoas_afetadas[i]}")
    print(f"Crianças: {criancas[i]}, Adultos: {adultos[i]}, Idosos: {idosos[i]}")
    print(f"Pessoas com mobilidade reduzida: {mobilidade_reduzida[i]}, Feridos: {feridos[i]}")

#A - Total de desastres registrados
print(quantidade_desastres, "desastres registrados.")

#Total de pessoas afetadas por desastre
soma = sum(qt_pessoas_afetadas)
print("\nTotal de pessoas afetadas por desastre: ", soma)


# Calcula a soma total de cada categoria
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)


# Exibe a soma total de cada categoria
print("\nSoma total de pessoas em cada categoria:")
print(f"Crianças: {total_criancas}")
print(f"Adultos: {total_adultos}")
print(f"Idosos: {total_idosos}")
print(f"Pessoas com mobilidade reduzida: {total_mobilidade_reduzida}")
print(f"Feridos: {total_feridos}")

# Identifica a categoria mais afetada
categorias_totais = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Mobilidade Reduzida": total_mobilidade_reduzida,
    "Feridos": total_feridos
}

categoria_mais_afetada = max(categorias_totais, key=categorias_totais.get)
print("\nCategoria mais afetada no geral:", categoria_mais_afetada)


# Descobre o desastre com o maior número de afetados
maior_desastre_indice = qt_pessoas_afetadas.index(max(qt_pessoas_afetadas))
local_maior_desastre = f"{ruas[maior_desastre_indice]}, {bairros[maior_desastre_indice]}, {cidades[maior_desastre_indice]}, {paises[maior_desastre_indice]}"
print(f"Desastre com maior número de afetados localiza-se em: {local_maior_desastre}")

# Exibe o relatório geral
print(f"\nRelatório Geral:")
print(f"Quantidade total de desastres: {quantidade_desastres}")
print("\nQuantidade de pessoas em cada categoria:\n")
print(f"Crianças: {total_criancas}, Adultos: {total_adultos}, Idosos: {total_idosos}")
print(f"Pessoas com mobilidade reduzida: {total_mobilidade_reduzida}, Feridos: {total_feridos}")
print(f"categoria mais afetada: {categoria_mais_afetada}")
print(f"\nQuantidade total de pessoas afetadas: {soma}")
print(f"local com maior número de afetados: {local_maior_desastre}")
