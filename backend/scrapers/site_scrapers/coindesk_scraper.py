from ..base_scraper import BaseScraper
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

class CoindeskScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.coindesk.com/markets"

    def scrape(self, date: datetime = None):
        try:
            html = self.fetch_page(self.base_url, wait_time=10)
            if not html:
                return []
                
            soup = BeautifulSoup(html, 'html.parser')
            articles = soup.find_all(['article', 'div'], class_=lambda x: x and ('article' in x.lower() or 'story' in x.lower()))
            
            news = []
            for article in articles:
                try:
                    news_item = self.parse_article(article)
                    if news_item:
                        if date:
                            article_date = datetime.strptime(news_item['date'], "%Y-%m-%d").date()
                            if article_date == date.date():
                                news.append(news_item)
                        else:
                            news.append(news_item)
                except Exception as e:
                    print(f"Erreur lors du parsing de l'article: {e}")
                    continue
                    
            return news
            
        except Exception as e:
            print(f"Erreur lors du scraping: {e}")
            return []

    def parse_article(self, article_html):
        try:
            # Chercher le titre
            title_element = article_html.find(['h1', 'h2', 'h3', 'h4'], class_=lambda x: x and ('title' in x.lower() or 'headline' in x.lower()))
            if not title_element:
                return None
            
            title = title_element.text.strip()
            
            # Chercher le lien
            link_element = title_element.find_parent('a') or article_html.find('a')
            if not link_element:
                return None
                
            link = link_element.get('href', '')
            if not link.startswith('http'):
                link = f"https://www.coindesk.com{link}"
            
            # Chercher l'image
            image = None
            img_element = article_html.find('img')
            if img_element:
                image = img_element.get('src', '')
            
            # Date par défaut (aujourd'hui)
            current_date = datetime.now(pytz.UTC).strftime("%Y-%m-%d")
            
            return {
                'title': title,
                'link': link,
                'image': image,
                'date': current_date,
                'source': 'Coindesk'
            }
            
        except Exception as e:
            print(f"Erreur dans parse_article: {e}")
            return None 