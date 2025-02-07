from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import pytz
from scrapers.site_scrapers.coindesk_scraper import CoindeskScraper

router = APIRouter()

class NewsResponse(BaseModel):
    status: str
    data: list
    message: Optional[str] = None

@router.get("/news", response_model=NewsResponse)
async def get_news(date: Optional[str] = None):
    try:
        scraper = CoindeskScraper()
        parsed_date = None
        
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                parsed_date = parsed_date.replace(tzinfo=pytz.UTC)
            except ValueError as e:
                print(f"Erreur de parsing de date: {e}")
                raise HTTPException(
                    status_code=400,
                    detail="Format de date invalide. Utilisez YYYY-MM-DD"
                )
        
        news = scraper.scrape(parsed_date)
        
        if not news:
            return NewsResponse(
                status="success",
                data=[],
                message="Aucune actualité trouvée pour cette date"
            )
            
        return NewsResponse(status="success", data=news)
        
    except Exception as e:
        print(f"Erreur dans get_news: {str(e)}")
        return NewsResponse(
            status="error",
            data=[],
            message=f"Erreur lors de la récupération des actualités: {str(e)}"
        ) 