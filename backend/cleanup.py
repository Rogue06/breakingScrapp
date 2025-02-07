import os
import shutil

def cleanup_chrome_data():
    try:
        chrome_data_dir = os.path.join(os.getcwd(), 'chrome_data')
        if os.path.exists(chrome_data_dir):
            shutil.rmtree(chrome_data_dir)
            print("Nettoyage des données Chrome effectué")
    except Exception as e:
        print(f"Erreur lors du nettoyage: {e}")

if __name__ == "__main__":
    cleanup_chrome_data() 