# ⚡ Energy Planning Optimization

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> 📊 A simple yet powerful tool to optimize energy distribution between **Solar**, **Battery**, and **Gas** sources while meeting renewable energy targets.  

---

## 🚀 Features
- 📥 Takes **total power demand** as input (MW).
- 🌞 Ensures **90% renewable energy** (solar + battery).
- 🔋 Splits renewable energy between **solar (8 parts)** and **battery (1 part)**.
- 🛢 Remaining demand is met with **gas energy**.
- 💰 Calculates **total cost** based on per MW prices.
- 📄 Clean, user-friendly output.

---

## 🧮 How It Works

1. **Calculate Renewable Energy**  
renewable_energy = TOTAL_DEMAND × RENEWABLE_TARGET

markdown
Copy
Edit

2. **Split into Solar & Battery**  
solar_energy = renewable_energy × (8/9)
battery_energy = renewable_energy × (1/9)

markdown
Copy
Edit

3. **Gas Energy for the Rest**  
gas_energy = TOTAL_DEMAND − renewable_energy

markdown
Copy
Edit

4. **Total Cost**  
total_cost = (solar_energy × SOLAR_COST) +
(battery_energy × BATTERY_COST) +
(gas_energy × GAS_COST)

yaml
Copy
Edit

---

## 📦 Requirements
- Python **3.x** installed

---

## 🖥️ Usage
```bash
# Clone the repository
git clone https://github.com/your-username/energy-planning-optimization.git

# Navigate into the folder
cd energy-planning-optimization

# Run the program
python energy_planner.py
💡 Example Output
yaml
Copy
Edit
Enter the total power demand in MW: 100

Energy Planning Optimization Results:
Total Demand: 100.00 MW
Solar Energy: 80.00 MW
Battery Energy: 10.00 MW
Gas Energy: 10.00 MW
Total Cost: ₹430000.00
📈 Future Improvements
🎯 Make solar-to-battery ratio user-adjustable.

🔢 Allow renewable target percentage customization.

🛠 Add more non-renewable sources for comparison.

📊 Visualize results with charts & graphs.

🛠 **Made with ❤️ by Kartik Bhardwaj**
👨‍💻 Author
Kartik Bhardwaj
💼 Aspiring Generative AI Engineer | Full Stack Developer | Data Scientist
