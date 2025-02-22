# 🌱 RL-Based Smart Irrigation System for Agriculture

## 🎯 Project Overview
This project uses **Reinforcement Learning (RL)** to optimize **water irrigation** for crops in a simulated environment. The RL agent learns to balance soil moisture while minimizing water waste and maximizing crop health.

## 🚀 Features
- **AI-driven irrigation decisions** based on soil moisture, temperature, and rainfall.
- **Optimized water usage** to prevent overwatering and underwatering.
- **Uses Reinforcement Learning (PPO)** for decision-making.
- **Built with Gymnasium, Stable-Baselines3, and PyTorch**.
- **Easily train and test the model** using provided scripts.

---

## 🛠️ Installation
### **Step 1: Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/RL_SmartIrrigation.git
cd RL_SmartIrrigation
```

### **Step 2: Install dependencies**
```bash
pip install gymnasium stable-baselines3 numpy pandas matplotlib torch
```

---

## 📌 How It Works
### **Environment (SmartIrrigationEnv)**
- **Observation space:** `(soil moisture, temperature, rainfall)`
- **Action space:** `(0 = No irrigation, 1 = Low irrigation, 2 = High irrigation)`
- **Reward system:**
  - **+10** for maintaining **optimal moisture (40-60)**.
  - **Penalty** for **too dry or too wet** conditions.
  - **Game over if soil moisture < 10 or > 90** (crop failure).

### **Training Process**
The AI is trained using **Proximal Policy Optimization (PPO)** over **50,000 timesteps** to optimize irrigation decisions.

---

## 📌 Usage
### **Train the RL Model**
Run the following command to start training:
```bash
python train_irrigation.py
```

### **Test the Trained Model**
After training is complete, run the test script to see the AI making irrigation decisions:
```bash
python test_irrigation.py
```

---

## 📊 Results & Performance
- The RL agent learns to **maintain soil moisture** within the optimal range.
- It avoids **wasting water** while preventing **crop failures**.
- Performance improves significantly after ~30,000 timesteps.

---

## 🛠️ Technologies Used
- **Python**
- **Gymnasium (for RL environment)**
- **Stable-Baselines3 (for PPO training)**
- **PyTorch (for RL model backend)**
- **NumPy, Pandas (for data handling)**
- **Matplotlib (for visualization)**

---


