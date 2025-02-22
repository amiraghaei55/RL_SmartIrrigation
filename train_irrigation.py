import gymnasium as gym
from stable_baselines3 import PPO
from irrigation_env import SmartIrrigationEnv

# Create the smart irrigation environment
env = SmartIrrigationEnv()

# Train using PPO (Proximal Policy Optimization)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=50000)  # Train for 50,000 steps

# Save the trained model
model.save("irrigation_model")
print("Training complete!")
