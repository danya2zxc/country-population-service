from sqlalchemy import text

from src.database import async_session
from src.models import CountryPopulation


class PopulationRepository:
    async def clear_table(self):
        async with async_session() as session:
            await session.execute(text("DELETE FROM country_population"))
            await session.commit()

    async def save_countries(self, countries):
        async with async_session() as session:
            objs = [
                CountryPopulation(country_name=c["country_name"], region=c["region"], population=c["population"])
                for c in countries
            ]
            session.add_all(objs)
            await session.commit()
