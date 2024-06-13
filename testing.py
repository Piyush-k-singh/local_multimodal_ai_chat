import ctypes
import os

import platform
print(platform.architecture())


# Ensure the correct path to your DLL
dll_path = os.path.abspath(r"C:\Users\GI0103\Anaconda3\envs\llm\lib\site-packages\llama_cpp\llama.dll")

# Load the DLL
try:
    your_dll = ctypes.CDLL(dll_path)
    print("DLL loaded successfully.")
except OSError as e:
    print(f"Failed to load DLL: {e}")
