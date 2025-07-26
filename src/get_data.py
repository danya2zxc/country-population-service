import asyncio

from src.service import PopulationService


async def main():
    service = PopulationService()
    await service.load_and_save()
    print("Population data loaded into DB!")

if __name__ == "__main__":
    asyncio.run(main())
