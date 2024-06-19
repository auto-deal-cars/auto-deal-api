""" This module contains the service for the vehicle application """
from typing import List
from sqlalchemy.orm.exc import NoResultFound

from vehicle.domain.entities.vehicle import Vehicle
from vehicle.application.ports.vehicle_repository import VehicleRepository

class VehicleService:
    """ This class contains the service for the vehicle application """
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def register_vehicle(self, vehicle_data: dict) -> Vehicle:
        """ Register a new Vehicle """
        vehicle = Vehicle(**vehicle_data)

        vehicle = self.vehicle_repository.save(vehicle)

        return vehicle

    def update_vehicle(self, vehicle_id: int, vehicle_data: dict) -> Vehicle:
        """ Update a Vehicle """
        vehicle = self.vehicle_repository.get(vehicle_id)
        if vehicle is None:
            raise NoResultFound(f"Vehicle with ID {vehicle_id} not found")

        vehicle = Vehicle(**vehicle_data)

        vehicle = self.vehicle_repository.update(vehicle_id, vehicle)

        return vehicle

    def get(self, vehicle_id: int) -> Vehicle:
        """ Get a Vehicle by its ID """
        vehicle = self.vehicle_repository.get(vehicle_id)
        if vehicle is None:
            raise NoResultFound(f"Vehicle with ID {vehicle_id} not found")

        return vehicle

    def get_all_available(self) -> List[Vehicle]:
        """ Get all available Vehicles """
        return self.vehicle_repository.get_all_available()

    def mark_vehicle_as_sold(self, vehicle_id: int, user_id: str) -> None:
        """ Mark a Vehicle as sold """
        vehicle = self.get(vehicle_id)
        if vehicle is None:
            raise NoResultFound(f"Vehicle with ID {vehicle_id} not found")

        self.vehicle_repository.mark_vehicle_as_sold(vehicle_id, user_id)
