"""
This module contains the repository for the vehicle application.
"""
from abc import ABC, abstractmethod

from typing import List
from vehicle.domain.entities.vehicle import Vehicle
from vehicle.domain.entities.vehicle_brand import VehicleBrand

class VehicleRepository(ABC):
    """
    This class contains the repository for the vehicle application.
    """
    @abstractmethod
    def save(self, vehicle: Vehicle) -> Vehicle:
        """
        This method saves a vehicle to the database.
        """
        pass

    @abstractmethod
    def update(self, vehicle_id: int, vehicle: Vehicle) -> Vehicle:
        """
        This method updates a vehicle in the database.
        """
        pass

    @abstractmethod
    def get(self, vehicle_id: int) -> Vehicle:
        """
        This method gets a vehicle from the database.
        """
        pass

    @abstractmethod
    def get_all_available(self) -> List[Vehicle]:
        """
        This method gets all available vehicles from the database.
        """
        pass

    @abstractmethod
    def mark_vehicle_as_sold(self, vehicle_id: int, user_id: str) -> None:
        """
        This method marks a vehicle as sold in the database.
        """
        pass

    @abstractmethod
    def get_brand(self, brand_name: str) -> VehicleBrand | None:
        """
        This method gets a brand from the database.
        """
        pass

    @abstractmethod
    def create_brand(self, brand_name: str) -> VehicleBrand:
        """
        This method creates a brand in the database.
        """
        pass
