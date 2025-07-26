import aiohttp
from bs4 import BeautifulSoup


class WikiPopulationParser:
    URL = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"

    async def get_data(self):
        async with aiohttp.ClientSession() as session, session.get(self.URL) as resp:
            html = await resp.text()

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="wikitable")
        data = []
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue
            country_name = cols[0].text.strip()
            population = cols[2].text.strip().replace(",", "")
            region = cols[4].text.strip()
            if not region:
                continue
            try:
                population = int(population)
            except ValueError:
                continue
            data.append(
                {
                    "country_name": country_name,
                    "population": population,
                    "region": region,
                }
            )
        return data
