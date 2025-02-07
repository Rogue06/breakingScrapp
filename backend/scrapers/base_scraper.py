from abc import ABC, abstractmethod
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os

class BaseScraper(ABC):
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.setup_browser()

    def setup_browser(self):
        try:
            self.browser = self.playwright.chromium.launch(
                headless=True,
                args=[
                    '--disable-gpu',
                    '--disable-dev-shm-usage',
                    '--disable-setuid-sandbox',
                    '--no-sandbox',
                ]
            )
            self.context = self.browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            )
            self.page = self.context.new_page()
            
        except Exception as e:
            print(f"Erreur lors de l'initialisation du navigateur: {e}")
            raise

    def fetch_page(self, url, wait_time=10):
        try:
            self.page.goto(url, wait_until='networkidle')
            self.page.wait_for_timeout(wait_time * 1000)  # Convertir en millisecondes
            return self.page.content()
        except Exception as e:
            print(f"Erreur lors du chargement de la page {url}: {e}")
            return None

    def __del__(self):
        try:
            if hasattr(self, 'browser'):
                self.browser.close()
            if hasattr(self, 'playwright'):
                self.playwright.stop()
        except Exception as e:
            print(f"Erreur lors de la fermeture du navigateur: {e}")

    @abstractmethod
    def scrape(self, date: datetime = None):
        pass

    @abstractmethod
    def parse_article(self, article_html):
        pass

    def clean_up(self):
        try:
            chrome_data_dir = os.path.join(os.getcwd(), 'chrome_data')
            if os.path.exists(chrome_data_dir):
                import shutil
                shutil.rmtree(chrome_data_dir)
        except Exception as e:
            print(f"Erreur lors du nettoyage: {e}") 