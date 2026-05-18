"""
Class Adapter (Using Inheritance)
This uses multiple inheritance.
Adapter inherits from:
Target interface
Adaptee
⚠ Less common in Python but possible.
"""

from abc import ABC, abstractmethod

# Step 1: Identify Target Interface
class RideService(ABC):
    @abstractmethod
    def book_ride(self, pickup, drop):
        pass

# Step 2: Identify Adaptee (Existing Class)
class ThirdPartyTaxiLogic:
    def create_trip(self, start, end):
        print(f"Trip created from {start} to {end}")

# Step 3: Create Adapter
class TaxiAdapter(RideService, ThirdPartyTaxiLogic):
    def book_ride(self, pickup, drop):
        self.create_trip(pickup, drop)


adapter = TaxiAdapter()
adapter.create_trip("Airport", "Hotel")