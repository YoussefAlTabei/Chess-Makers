# config.py
import os
import sys

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to important folders
UI_DIR = os.path.join(BASE_DIR, "UI")
PIECES_DIR = os.path.join(BASE_DIR, "Pieces")
NETWORKING_DIR = os.path.join(BASE_DIR, "Networking")

# Add to sys.path
sys.path.append(UI_DIR)
sys.path.append(PIECES_DIR)
sys.path.append(NETWORKING_DIR)
