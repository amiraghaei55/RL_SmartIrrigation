import gymnasium as gym
from stable_baselines3 import PPO
from irrigation_env import SmartIrrigationEnv
import time

# Load environment and trained model
env = SmartIrrigationEnv()
model = PPO.load("irrigation_model")

obs, _ = env.reset()
done = False

while not done:
    action, _ = model.predict(obs)
    obs, reward, done, _, _ = env.step(action)
    env.render()
    time.sleep(0.5)  # Delay for readability

env.close()
