# main.py
from RPS import player
from RPS_game import play, quincy, rando, reflect, cycle

print("🔹 Testing RPS Bot Performance 🔹\n")

# Run each match
play(player, quincy, 1000)
play(player, rando, 1000)
play(player, reflect, 1000)
play(player, cycle, 1000)

# Uncomment below line to run unit tests automatically
# import test_module; test_module.test()
