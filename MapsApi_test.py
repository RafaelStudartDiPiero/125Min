import MapsAPI
# Duas agencias modelo, uma que vai ser adiciona, atualizada, selecionada e removida e outra que nunca existira.


def test_create_data():
    api_key = 'AIzaSyCsQr7dKJW_3V_YutYvVZjxl0zcAdRUb9A'
    adress_list = ['R.+Nunes+Machado+977+Araras+13600-021','R.+Emilio+Cani+899+Botucatu+18606-730', 'Estr.+do+Tindiba+979+Rio+de+Janeiro+22740-361']
    data = MapsAPI.create_data(api_key, adress_list)

    assert data["API_key"] == api_key
    assert data["addresses"] == adress_list


def test_create_distance_matrix():
    api_key = 'AIzaSyCsQr7dKJW_3V_YutYvVZjxl0zcAdRUb9A'
    adress_list = ['R.+Nunes+Machado+977+Araras+13600-021', 'R.+Emilio+Cani+899+Botucatu+18606-730',
                   'Estr.+do+Tindiba+979+Rio+de+Janeiro+22740-361']
    data = MapsAPI.create_data(api_key, adress_list)
    distance_matrix = MapsAPI.create_distance_matrix(data)

    self_distances = 0
    for i, vector in enumerate(distance_matrix):
        self_distances += vector[i]
    assert self_distances == 0

    positive = 1
    for vector in distance_matrix:
        for dis in vector:
            if dis < 0:
                positive = 0
    assert positive == 1

    assert len(distance_matrix) == 3
    assert len(distance_matrix[0]) == 3


def test_create_time_matrix():
    api_key = 'AIzaSyCsQr7dKJW_3V_YutYvVZjxl0zcAdRUb9A'
    adress_list = ['R.+Nunes+Machado+977+Araras+13600-021', 'R.+Emilio+Cani+899+Botucatu+18606-730',
                   'Estr.+do+Tindiba+979+Rio+de+Janeiro+22740-361']
    data = MapsAPI.create_data(api_key, adress_list)
    time_matrix = MapsAPI.create_time_matrix(data)

    self_times = 0
    for i, vector in enumerate(time_matrix):
        self_times += vector[i]
    assert self_times == 0

    positive = 1
    for vector in time_matrix:
        for dis in vector:
            if dis < 0:
                positive = 0
    assert positive == 1

    assert len(time_matrix) == 3
    assert len(time_matrix[0]) == 3