import gymnasium as gym
import numpy as np
from gymnasium import spaces

class SmartIrrigationEnv(gym.Env):
    def __init__(self):
        super(SmartIrrigationEnv, self).__init__()

        # Actions: 0 = No water, 1 = Low irrigation, 2 = High irrigation
        self.action_space = spaces.Discrete(3)

        # Observation space (Soil moisture, Temperature, Rainfall)
        self.observation_space = spaces.Box(low=0, high=100, shape=(3,), dtype=np.float32)

        self.reset()

    def reset(self, seed=None, options=None):
        self.soil_moisture = np.random.randint(30, 70)  # Initial soil moisture level
        self.temperature = np.random.randint(20, 40)  # Temperature (°C)
        self.rainfall = np.random.randint(0, 20)  # Rainfall (mm)
        return np.array([self.soil_moisture, self.temperature, self.rainfall], dtype=np.float32), {}

    def step(self, action):
        # Define how much water is added
        if action == 0:
            water = 0  # No irrigation
        elif action == 1:
            water = 5  # Low irrigation
        else:
            water = 10  # High irrigation

        # Update soil moisture based on irrigation and natural effects
        self.soil_moisture += water
        self.soil_moisture -= np.random.randint(5, 15)  # Evaporation and absorption loss

        # Reward function (optimal moisture range: 40-60)
        if 40 <= self.soil_moisture <= 60:
            reward = 10  # Optimal watering
        else:
            reward = -abs(50 - self.soil_moisture)  # Penalty for too dry or too wet soil

        done = self.soil_moisture < 10 or self.soil_moisture > 90  # Crop failure

        return np.array([self.soil_moisture, self.temperature, self.rainfall], dtype=np.float32), reward, done, False, {}

    def render(self, mode="human"):
        print(f"Soil Moisture: {self.soil_moisture}, Temperature: {self.temperature}, Rainfall: {self.rainfall}")

    def close(self):
        pass
