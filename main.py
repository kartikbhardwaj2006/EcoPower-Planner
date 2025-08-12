TOTAL_DEMAND = float(input("Enter the total power demand in MW: "))

RENEWABLE_TARGET = 0.9
SOLAR_COST = 4000
BATTERY_COST = 5500
GAS_COST = 7500

renewable_energy = TOTAL_DEMAND * RENEWABLE_TARGET
non_renewable_energy = TOTAL_DEMAND - renewable_energy

solar_energy = renewable_energy * (8/9)
battery_energy = renewable_energy * (1/9)

gas_energy = non_renewable_energy

total_cost = (solar_energy * SOLAR_COST) + (battery_energy * BATTERY_COST) + (gas_energy * GAS_COST)

print("\nEnergy Planning Optimization Results:")
print(f"Total Demand: {TOTAL_DEMAND:.2f} MW")
print(f"Solar Energy: {solar_energy:.2f} MW")
print(f"Battery Energy: {battery_energy:.2f} MW")
print(f"Gas Energy: {gas_energy:.2f} MW")
print(f"Total Cost: ₹{total_cost:.2f}")