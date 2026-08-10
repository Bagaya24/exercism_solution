"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*arg):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *wagons ,=arg
    return wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    *wagons ,= each_wagons_id, missing_wagons
    [[first, second, third, *rest], last] = wagons
    *wagons ,= third, *last, *rest, first, second
    return wagons


def add_missing_stops(routing:dict, **kwarg):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stop_cities_list = []
    for key, value in kwarg.items():
        stop_cities_list.append(value)
    stop_cities_dict = dict(stops=stop_cities_list)
    stops_route = {**routing, **stop_cities_dict}
    return stops_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extend_route = {**route, **more_route_information}
    return extend_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(wagon) for wagon in zip(*wagons_rows)]
