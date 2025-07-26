import asyncio

from sqlalchemy import text

from src.database import async_session


async def main():
    query = text("""
    WITH ranked_countries AS (
        SELECT
            region,
            country_name,
            population,
            SUM(population) OVER (PARTITION BY region) as total_region_population,
            ROW_NUMBER() OVER (PARTITION BY region ORDER BY population DESC) as rn_desc,
            ROW_NUMBER() OVER (PARTITION BY region ORDER BY population ASC) as rn_asc
        FROM
            country_population
        WHERE
            region != ''
    )
    SELECT
        rc.region,
        rc.total_region_population,
        max_country.country_name as max_country_name,
        max_country.population as max_country_population,
        min_country.country_name as min_country_name,
        min_country.population as min_country_population
    FROM
        ranked_countries rc
    JOIN
        ranked_countries max_country ON rc.region = max_country.region AND max_country.rn_desc = 1
    JOIN
        ranked_countries min_country ON rc.region = min_country.region AND min_country.rn_asc = 1
    GROUP BY
        rc.region, rc.total_region_population, max_country_name, max_country_population, min_country_name, min_country_population
    ORDER BY
        rc.region;
    """)

    async with async_session() as session:
        result = await session.execute(query)
        for row in result.mappings().all():
            print(f"Name of region: {row['region']}")
            print(f"Total population of region: {row['total_region_population']}")
            print(f"Largest country: {row['max_country_name']}")
            print(f"Largest country population: {row['max_country_population']}")
            print(f"Smallest country: {row['min_country_name']}")
            print(f"Smallest country population: {row['min_country_population']}")
            print()  # Newline

if __name__ == "__main__":
    asyncio.run(main())
