"""
Object Adapter (Most Common in Python)
This uses composition.
Adapter wraps the adaptee object.
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
class TaxiAdapter(RideService):
    def __init__(self, taxi_logic):
        self.taxi_logic = taxi_logic

    def book_ride(self, pickup, drop):
        self.taxi_logic.create_trip(pickup, drop)

# Step 4: Client Code
def client_code(service: RideService):
    service.book_ride("Airport", "Hotel")


third_party = ThirdPartyTaxiLogic()
adapter = TaxiAdapter(third_party)

client_code(adapter)


"""
📌 Why This Is Called Object Adapter?
Because:
self.taxi_sdk = taxi_sdk
We are wrapping an object.
✔ Flexible
✔ Can adapt multiple classes
✔ Preferred in Python
"""