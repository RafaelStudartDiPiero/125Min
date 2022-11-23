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
from abc import ABC, abstractmethod
import datetime

class OtimizationResult():
    def __init__(self, path_list, total_cost, num_vehicles):
        self.path_list = path_list
        self.total_cost = total_cost
        self.date = datetime.datetime.now()
        self.num_vehicles = num_vehicles
    def print_report(self):
        print(f'Data da Otimização: {self.date.day}/{self.date.month}/{self.date.year}')
        print(f"Custo Total da Viagem: R${self.total_cost : .2f}")
        print(f'O número total de motoristas empregados foi: {self.num_vehicles}')
        print('O resumo por motorista pode ser visualizado abaixo:')
        for driver_path in self.path_list:
            driver_path.print_report()
    


class RouteStep(ABC):
    def __init__(self, type):
        self.type = type
    @abstractmethod
    def print_step(self):
        pass


class Maintance(RouteStep):
    def __init__(self, CEP, ID):
        super().__init__("Maintance")
        self.CEP = CEP
        self.ID = ID
    def print_step(self):
        print(f'Manutenção na Agência de CEP: {self.CEP} e ID: {self.ID}')


class Trip(RouteStep):
    def __init__(self, origin, destination):
        super().__init__("Trip")
        self.origin = origin
        self.destination = destination
    def print_step(self):
        print(f'Deslocamento de {self.origin} para {self.destination}')


class Sleep(RouteStep):
    def __init__(self, city):
        super().__init__("Sleep")
        self.city = city
    def print_step(self):
        print(f'Dorme em: {self.city}')


class DriverPath():
    def __init__(self, driver_id, route_time, route_cost, path) :
        self.route_time = route_time
        self.route_cost = route_cost
        self.path = path
        self.driver_id = driver_id

    def print_report(self):
        print(f'\n**************** Motorista {self.driver_id} *****************\n')
        print(f'Tempo Total da Rota: {self.route_time}s')
        print(f'Valor Estimado da Viagem: R${self.route_cost : .2f}')
        print('\nRota Sugerida:\n')
        for step in self.path:
            step.print_step()


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

"""
def print_solution(data, manager, routing, solution):
    #Prints solution on console.
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
"""

# Decides if driver will return to origin
def run_sleep_otimization(solution, data, manager, routing, selected_agency):
    config = Config()
    config.selectConfig()
    sleep_price = config.hospedagem  # in R$
    average_fuel_consuption = config.consumo_combustivel*1000  # convert from Km/L to m/L
    diesel_price = config.custo_gasolina  # in R$/L
    employee_sallary = config.salario_hora/(60*60)  # convert from R$/h to R$/s
    max_work_time = 12*60*60  # 12h
    average_maintaince_time = config.tempo_manutencao*60*60  # convert from h to s
    result = OtimizationResult([], 0, data['num_vehicles'])
    for vehicle_id in range(data['num_vehicles']):
        driver_path = DriverPath(vehicle_id + 1, 0, 0, [])
        current_travel_time = 0
        current_return_time = 0
        current_return_distance = 0
        new_return_time = 0
        new_return_distance = 0
        current_maintaince_time = 0
        start = routing.Start(vehicle_id)
        index = start
        start_agency =  selected_agency[manager.IndexToNode(index)] #vetor com id, numero, rua, cidade, cep
        agency = start_agency
        otimized_path = [manager.IndexToNode(index)] # is not used anymore -> delete on final project
        while not routing.IsEnd(index):
            previous_index = index
            previous_agency = agency
            index = solution.Value(routing.NextVar(index))
            agency = selected_agency[manager.IndexToNode(index)]
            current_return_time = new_return_time
            current_return_distance = new_return_distance
            new_return_time = time_callback(index, start, manager, data)
            new_return_distance = time_callback(index, start, manager, data)
            # Goes to next city, still having time to do the maintaince and return to origin
            if current_travel_time + current_maintaince_time + average_maintaince_time + time_callback(previous_index, index, manager, data) + new_return_time <= max_work_time:
                otimized_path += [manager.IndexToNode(index), 'maintance']
                driver_path.path += [Trip(previous_agency[3], agency[3]), Maintance(agency[4], agency[0])]
                current_maintaince_time += average_maintaince_time
                current_travel_time += time_callback(
                    previous_index, index, manager, data)
                driver_path.route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                driver_path.route_cost += (time_callback(previous_index, index, manager, data) + average_maintaince_time)*employee_sallary + \
                    distance_callback(
                        previous_index, index, manager, data)*diesel_price/average_fuel_consuption
            # sleeps after maintaince in next city
            elif current_travel_time + current_maintaince_time + average_maintaince_time + time_callback(previous_index, index, manager, data) <= max_work_time:
                otimized_path += [manager.IndexToNode(index), 'maintance', 'sleep']
                driver_path.path += [Trip(previous_agency[3], agency[3]), Maintance(agency[4], agency[0]), Sleep(agency[3])]
                current_maintaince_time = 0
                current_travel_time = 0
                driver_path.route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                driver_path.route_cost += sleep_price + (average_maintaince_time + time_callback(previous_index, index, manager, data))*employee_sallary + (
                    distance_callback(previous_index, index, manager, data))*diesel_price/average_fuel_consuption
            elif current_travel_time + current_maintaince_time + time_callback(previous_index, index, manager, data) <= max_work_time:
                # returns to origin so as to sleep
                if (current_return_time + new_return_time)*employee_sallary + (current_return_distance+new_return_distance)*diesel_price/average_fuel_consuption < sleep_price:  
                    otimized_path += [manager.IndexToNode(
                        start), 'sleep', manager.IndexToNode(index), 'maintance']
                    driver_path.path += [Trip(previous_agency[3], start_agency[3]), Sleep(start_agency[3]), Trip(start_agency[3], agency[3]), Maintance(agency[4], agency[0])]
                    current_maintaince_time = average_maintaince_time
                    current_travel_time = time_callback(
                        start, index, manager, data)
                    driver_path.route_time += average_maintaince_time + current_return_time + new_return_time
                    driver_path.route_cost += (average_maintaince_time + current_return_time + new_return_time)*employee_sallary + (
                        current_return_distance + new_return_distance)*diesel_price/average_fuel_consuption
                # sleeps in next city and starts day with maintance
                else:  
                    otimized_path += [manager.IndexToNode(index), 'sleep', 'maintance']
                    driver_path.path += [Trip(previous_agency[3], agency[3]), Sleep(agency[3]), Maintance(agency[4], agency[0])]
                    current_maintaince_time = average_maintaince_time
                    current_travel_time = 0
                    driver_path.route_time += average_maintaince_time + \
                        time_callback(previous_index, index, manager, data)
                    driver_path.route_cost += sleep_price + (average_maintaince_time + time_callback(previous_index, index, manager, data))*employee_sallary + (
                        distance_callback(previous_index, index, manager, data))*diesel_price/average_fuel_consuption
            # returns to origin so as to sleep
            elif (current_return_time + new_return_time)*employee_sallary + (current_return_distance+new_return_distance)*diesel_price/average_fuel_consuption < sleep_price:  
                otimized_path += [manager.IndexToNode(start), 'sleep',
                                  manager.IndexToNode(index), 'maintance']
                driver_path.path += [Trip(previous_agency[3], start_agency[3]), Sleep(start_agency[3]), Trip(start_agency[3], agency[3]), Maintance(agency[4], agency[0])]
                current_maintaince_time = average_maintaince_time
                current_travel_time = time_callback(
                    start, index, manager, data)
                driver_path.route_time += average_maintaince_time + current_return_time + new_return_time
                driver_path.route_cost += (average_maintaince_time + current_return_time + new_return_time)*employee_sallary + (
                    current_return_distance + new_return_distance)*diesel_price/average_fuel_consuption
            # sleeps in current city
            else:  
                otimized_path += ['sleep', manager.IndexToNode(index), 'maintance']
                driver_path.path += [Sleep(previous_agency[3]), Trip(previous_agency[3], agency[3]), Maintance(agency[4], agency[0])]
                current_maintaince_time = average_maintaince_time
                current_travel_time = time_callback(
                    previous_index, index, manager, data)
                driver_path.route_time += average_maintaince_time + \
                    time_callback(previous_index, index, manager, data)
                driver_path.route_cost += sleep_price + (time_callback(previous_index, index, manager, data) + average_maintaince_time) * \
                    employee_sallary + \
                    distance_callback(
                        previous_index, index, manager, data)*diesel_price/average_fuel_consuption

        result.total_cost += driver_path.route_cost
        result.path_list += [driver_path]
    return result


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
        #print_solution(data, manager, routing, solution)
        result_otimization = run_sleep_otimization(solution, data, manager, routing, selected_agency)
        result_otimization.print_report()
    else:
        print('No solution found !')