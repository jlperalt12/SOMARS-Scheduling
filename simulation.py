from eventprocessor import EventProcessor
from event import Event, PassengerEvent
from models import Aircraft, PassengerDemand, Passenger
import random

class Simulation:
    def __init__(self, vertiports, aircraft, passenger_demand, transport_times, ground_transport_schedule):
        self.vertiports = vertiports
        self.aircraft_list = aircraft
        self.passenger_demand = passenger_demand
        self.transport_times = transport_times
        self.ground_transport_schedule = ground_transport_schedule
        self.event_processor = EventProcessor(vertiports, transport_times, ground_transport_schedule)
    
    def graph_passenger_demand(self):
        for route in self.passenger_demand:
            route.graph()
    
    def add_all_passenger_events(self):
        for route in self.passenger_demand:
            for i in range(len(route.demand)):
                demand = route.demand[i]
                for passenger_i in range(demand):
                    unit_time_min = (60*route.unit_time) 
                    start_time = unit_time_min * i
                    random_time = random.uniform(start_time, start_time + unit_time_min)
                    passenger = Passenger(route.src, route.dest)

                    passenger_event = PassengerEvent(self.event_processor.get_next_event_id(), random_time, "add_passenger_to_vertiport", passenger)
                    self.event_processor.add_passenger_event(passenger_event)

    def add_init_aircraft_state(self):
        for aircraft in self.aircraft_list:
            self.event_processor.init_aircraft(aircraft)

    def print_vertiport_states(self):
        for vertiport in self.vertiports:
            vertiport.display_info()

    def print_vertiport_aircraft(self):
        for vertiport in self.vertiports:
            vertiport.display_aircraft()

    def print_simulation_state(self):
        print("None")
    
    def print_simulation_initialization(self):
        print("Vertiports:")
        for vp in self.vertiports:
            vp.display_info()
        print("\nAircraft:")
        for a in self.aircraft_list:
            a.display_info()
        print("\nPassenger Demands:")
        for demand in self.passenger_demand:
            demand.display_info()
        print("\nTransport Times:")
        for transport in self.transport_times:
            transport.display_info()
        print("\nGround Transport Schedules:")
        for t in self.ground_transport_schedule:
            t.display_info()
