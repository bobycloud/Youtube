# Travel Agency - Checking for Any Available Flights

flights = {"Flight 1": False, "Flight 2": False, "Flight 3": False, "Flight 4": True}

# Before
# available = False
# for flight in flights.values():
#     if flight:
#         available = True
#         break

# After
available = any(flights.values())

print(available)
