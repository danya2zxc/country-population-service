import aiohttp
from bs4 import BeautifulSoup


class StatTimesPopulationParser:
    URL = "https://statisticstimes.com/demographics/countries-by-population.php"

    async def get_data(self):
        async with aiohttp.ClientSession() as session, session.get(self.URL) as resp:
            html = await resp.text()
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", id="table_id")
        data = []
        for row in table.tbody.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) < 9:
                continue
            country_name = cols[0].text.strip()
            population = cols[1].text.strip().replace(",", "")
            region = cols[8].text.strip()
            try:
                population = int(population)
            except ValueError:
                continue
            data.append({"country_name": country_name, "region": region, "population": population})
        return data
