# config.py
import os
import sys

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to important folders
UI_DIR = os.path.join(BASE_DIR, "UI")
PIECES_DIR = os.path.join(BASE_DIR, "Pieces")
NETWORKING_DIR = os.path.join(BASE_DIR, "Networking")
DRAW_LEGAL_MOVES_DIR = os.path.join(UI_DIR, "Draw_legal_moves")
MOVEMENT_DIR = os.path.join(BASE_DIR, "Movement")
GAME_LOGIC_DIR = os.path.join(BASE_DIR, "Game_logic")  # Added Game_logic directory
COLOR_DIR = os.path.join(GAME_LOGIC_DIR, "Color")
# Add to sys.path
sys.path.append(UI_DIR)
sys.path.append(PIECES_DIR)
sys.path.append(NETWORKING_DIR)
sys.path.append(DRAW_LEGAL_MOVES_DIR)
sys.path.append(GAME_LOGIC_DIR)
sys.path.append(MOVEMENT_DIR)
sys.path.append(COLOR_DIR)
