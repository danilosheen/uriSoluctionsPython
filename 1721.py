from math import radians, sin, cos, sqrt, atan2

# Função para calcular a distância entre dois pontos na Terra usando a fórmula de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6378  # raio da Terra em quilômetros

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance

# Função para encontrar a distância entre um ponto e a linha equidistante
def distance_to_equidistant_line(lat_a, lon_a, lat_b, lon_b, lat_m, lon_m):
    distance_AM = haversine(lat_a, lon_a, lat_m, lon_m)
    distance_BM = haversine(lat_b, lon_b, lat_m, lon_m)
    distance_AB = haversine(lat_a, lon_a, lat_b, lon_b)

    # Se a distância AB for zero, então a distância para a linha equidistante é a distância AM
    if distance_AB == 0:
        return distance_AM

    # Calcular a distância para a linha equidistante
    cos_theta = (distance_AM**2 + distance_AB**2 - distance_BM**2) / (2 * distance_AM * distance_AB)
    distance_to_line = distance_AM * sqrt(1 - cos_theta**2)

    return distance_to_line

# Função principal para processar os casos
def process_cases(locations, cases):
    result = []

    for case in cases:
        A, B, M = case
        latitudes = {}
        longitudes = {}

        for location in locations:
            name, lat, lon = location
            latitudes[name] = lat
            longitudes[name] = lon

        if A in latitudes and B in latitudes and M in latitudes:
            lat_a, lon_a = latitudes[A], longitudes[A]
            lat_b, lon_b = latitudes[B], longitudes[B]
            lat_m, lon_m = latitudes[M], longitudes[M]

            distance = round(distance_to_equidistant_line(lat_a, lon_a, lat_b, lon_b, lat_m, lon_m))

            result.append(f"{M} is {distance} km off {A}/{B} equidistance.")
        else:
            result.append(f"{M} is ? km off {A}/{B} equidistance.")

    return result

# Função para ler a entrada
def read_input():
    locations = []
    cases = []
    reading_locations = True

    while True:
        line = input().strip()
        if line == "#":
            reading_locations = False
        elif reading_locations:
            if line == "#":
                reading_locations = False
            else:
                name, lat, lon = line.split()
                locations.append((name, float(lat), float(lon)))
        else:
            if line == "#":
                break
            case = line.split()
            cases.append((case[0], case[1], case[2]))

    return locations, cases

# Main
if __name__ == "__main__":
    locations, cases = read_input()
    result = process_cases(locations, cases)
    for line in result:
        print(line)
