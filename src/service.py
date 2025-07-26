from src.parser_factory import get_parser
from src.repository import PopulationRepository


class PopulationService:
    def __init__(self):
        self.parser = get_parser()
        self.repo = PopulationRepository()

    async def load_and_save(self):
        data = await self.parser.get_data()
        await self.repo.clear_table()
        await self.repo.save_countries(data)
