"""Simple Vehicles Routing Problem (VRP).

   This is a sample using the routing library python wrapper to solve a VRP
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters.
   Time is measured in seconds.
"""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import MapsAPI
from models.config import Config


def create_data_model(num_vehicles, api_key, adress_list):

    data = MapsAPI.create_data(api_key, adress_list)
    data['distance_matrix'] = MapsAPI.create_distance_matrix(data)
    data['time_matrix'] = MapsAPI.create_time_matrix(data)
    data['num_vehicles'] = num_vehicles
    data['depot'] = 0
    return data


def create_adress_list(selected_agency):
    adresses = {}
    adresses['street_list'] = [row[1] for row in selected_agency]
    adresses['number_list'] = [row[2] for row in selected_agency]
    adresses['city_list'] = [row[3] for row in selected_agency]
    adresses['CEP_list'] = [row[4] for row in selected_agency]
    adress_list = []
    for i in range(len(adresses['street_list'])):
        adresses['CEP_list'][i] = adresses['CEP_list'][i].replace(" ", "+").replace("ã", "a").replace("á", "a").replace(
            "â", "a").replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("é", "e").replace("í", "i")
        adresses['city_list'][i] = adresses['city_list'][i].replace(" ", "+").replace("ã", "a").replace("á", "a").replace(
            "â", "a").replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("é", "e").replace("í", "i")
        adresses['street_list'][i] = adresses['street_list'][i].replace(" ", "+").replace("ã", "a").replace("á", "a").replace(
            "â", "a").replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("é", "e").replace("í", "i")
        adress_list = adress_list + [adresses['street_list'][i]+'+'+adresses['number_list']
                                     [i]+'+'+adresses['city_list'][i]+'+'+adresses['CEP_list'][i]]
    return adress_list


def distance_callback(from_index, to_index, manager, data):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]


def time_callback(from_index, to_index, manager, data):
    """Returns the time distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['time_matrix'][from_node][to_node]


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_time = 0
        while not routing.IsEnd(index):
            plan_output += ' {} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_time += time_callback(previous_index, index, manager, data)
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Time of the route: {}s\n'.format(route_time)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
    print('Maximum of the route distances: {}m'.format(max_route_distance))


# Decides if driver will return to origin
def run_sleep_otimization(solution, data, manager, routing):
    # must be user input -> change in near future
    config = Config()
    config.selectConfig()
    sleep_price = config.hospedagem  # sleep_price = 100
    average_fuel_consuption = config.consumo_combustivel*1000  # 8 Km/L
    diesel_price = config.custo_gasolina  # R$/L # diesel_price = 5 # R$/L
    employee_sallary = config.salario_hora/(60*60)  # R$ 80,00 / h
    max_work_time = 12*60*60  # 12h
    average_maintaince_time = config.tempo_manutencao*60*60  # 4h
    otimized_path_matrix = []
    total_price = 0
    for vehicle_id in range(data['num_vehicles']):
        route_time = 0
        route_price = 0
        current_travel_time = 0
        current_return_time = 0
        current_return_distance = 0
        new_return_time = 0
        new_return_distance = 0
        current_maintaince_time = 0
        start = routing.Start(vehicle_id)
        index = start
        otimized_path = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            current_return_time = new_return_time
            current_return_distance = new_return_distance
            new_return_time = time_callback(index, start, manager, data)
            new_return_distance = time_callback(index, start, manager, data)
            if current_travel_time + current_maintaince_time + average_maintaince_time + time_callback(previous_index, index, manager, data) + new_return_time <= max_work_time:
                otimized_path += [manager.IndexToNode(index)]
                current_maintaince_time += average_maintaince_time
                current_travel_time += time_callback(
                    previous_index, index, manager, data)
                route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                route_price += (time_callback(previous_index, index, manager, data) + average_maintaince_time)*employee_sallary + \
                    distance_callback(
                        previous_index, index, manager, data)*diesel_price/average_fuel_consuption
            # sleeps after maintaince in next city
            elif current_travel_time + current_maintaince_time + average_maintaince_time + time_callback(previous_index, index, manager, data) <= max_work_time:
                otimized_path += [manager.IndexToNode(index)]
                current_maintaince_time = 0
                current_travel_time = 0
                route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                route_price += sleep_price + (average_maintaince_time + time_callback(previous_index, index, manager, data))*employee_sallary + (
                    distance_callback(previous_index, index, manager, data))*diesel_price/average_fuel_consuption
            elif current_travel_time + current_maintaince_time + time_callback(previous_index, index, manager, data) <= max_work_time:
                if (current_return_time + new_return_time)*employee_sallary + (current_return_distance+new_return_distance)*diesel_price/average_fuel_consuption < sleep_price:  # returns to origin
                    otimized_path += [manager.IndexToNode(
                        start), manager.IndexToNode(index)]
                    current_maintaince_time = average_maintaince_time
                    current_travel_time = time_callback(
                        start, index, manager, data)
                    route_time += average_maintaince_time + current_return_time + new_return_time
                    route_price += (average_maintaince_time + current_return_time + new_return_time)*employee_sallary + (
                        current_return_distance + new_return_distance)*diesel_price/average_fuel_consuption
                else:  # sleeps in next city and starts day with maintance
                    otimized_path += [manager.IndexToNode(index)]
                    current_maintaince_time = average_maintaince_time
                    current_travel_time = 0
                    route_time += average_maintaince_time + \
                        time_callback(previous_index, index, manager, data)
                    route_price += sleep_price + (average_maintaince_time + time_callback(previous_index, index, manager, data))*employee_sallary + (
                        distance_callback(previous_index, index, manager, data))*diesel_price/average_fuel_consuption
            elif (current_return_time + new_return_time)*employee_sallary + (current_return_distance+new_return_distance)*diesel_price/average_fuel_consuption < sleep_price:  # returns to origin
                otimized_path += [manager.IndexToNode(start),
                                  manager.IndexToNode(index)]
                current_maintaince_time = average_maintaince_time
                current_travel_time = time_callback(
                    start, index, manager, data)
                route_time += average_maintaince_time + current_return_time + new_return_time
                route_price += (average_maintaince_time + current_return_time + new_return_time)*employee_sallary + (
                    current_return_distance + new_return_distance)*diesel_price/average_fuel_consuption
            else:  # sleeps in city
                otimized_path += [manager.IndexToNode(index)]
                current_maintaince_time = average_maintaince_time
                current_travel_time = time_callback(
                    previous_index, index, manager, data)
                route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                route_price += sleep_price + (time_callback(previous_index, index, manager, data) + average_maintaince_time) * \
                    employee_sallary + \
                    distance_callback(
                        previous_index, index, manager, data)*diesel_price/average_fuel_consuption

        total_price += route_price
        otimized_path_matrix = otimized_path_matrix + [otimized_path]
        print(f'Route {vehicle_id} Time: {route_time}s')
        print(f'Route {vehicle_id} Price: R${route_price : .2f}')
    print(otimized_path_matrix)
    print(f'Total Price: R${total_price : .2f}')


def run_otimization(selected_agency):
    api_key = 'AIzaSyCsQr7dKJW_3V_YutYvVZjxl0zcAdRUb9A'
    config = Config()
    config.selectConfig()
    num_vehicles = config.numero_motoristas
    adress_list = create_adress_list(selected_agency)

    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(num_vehicles, api_key, adress_list)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    transit_callback_index = routing.RegisterTransitCallback(
        lambda from_node, to_node: distance_callback(from_node, to_node, manager, data))

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    #dimension_name = 'Time'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        1000000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)
        run_sleep_otimization(solution, data, manager, routing)
    else:
        print('No solution found !')
