"""Simple Vehicles Routing Problem (VRP).

   This is a sample using the routing library python wrapper to solve a VRP
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters.
"""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import MapsAPI

def create_data_model(num_vehicles, api_key, adress_list):
    
    data = MapsAPI.create_data(api_key, adress_list)
    data['distance_matrix'] = MapsAPI.create_distance_matrix(data)
    data['time_matrix'] = MapsAPI.create_time_matrix(data)
    data['num_vehicles'] = num_vehicles
    data['depot'] = 0
    return data

def create_adress_list():
    adresses = {}
    adresses['street_list'] = ['Rua Olivia Guedes Penteado', 'Av. Adolfo Pinheiro', 'Rua Simao Alvares', 'Rua Tuiuti', 'Rua H8B', 'Av. dos Esportes']
    adresses['number_list'] = [str(746), str(886), str(351), str(921), str(230), str(731)]
    adresses['city_list'] = ['Socorro', 'Santo Amaro', 'Pinheiros', 'Tatuape', 'Sao Jose dos Campos', 'Valinhos']
    adresses['CEP_list'] = ['04766-000', '04734-002', '05339-000', '03081-000', '12228-461', '13270-070']
    adress_list = []
    for i in range(len(adresses['street_list'])):
        adresses['CEP_list'][i] = adresses['CEP_list'][i].replace(" ","+")
        adresses['city_list'][i] = adresses['city_list'][i].replace(" ","+")
        adresses['number_list'][i] = adresses['number_list'][i].replace(" ","+")
        adresses['street_list'][i] = adresses['street_list'][i].replace(" ","+")
        adress_list = adress_list + [adresses['street_list'][i]+'+'+adresses['number_list'][i]+'+'+adresses['city_list'][i]+'+'+adresses['CEP_list'][i]]
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



def main():
    api_key = 'AIzaSyCsQr7dKJW_3V_YutYvVZjxl0zcAdRUb9A'
    num_vehicles = 2
    adress_list = create_adress_list()

    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(num_vehicles, api_key, adress_list)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    transit_callback_index = routing.RegisterTransitCallback(lambda from_node, to_node : distance_callback(from_node, to_node, manager, data))

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
    else:
        print('No solution found !')


if __name__ == '__main__':
    main()



