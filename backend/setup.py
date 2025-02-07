import subprocess
import sys

def setup_environment():
    print("Installation des dépendances...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Installation des navigateurs Playwright...")
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    
    print("Configuration terminée!")

if __name__ == "__main__":
    setup_environment() 