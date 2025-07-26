from sqlalchemy import BigInteger, Column, Integer, String

from src.database import Base


class CountryPopulation(Base):
    """
    Represents the population data for a country.
    """
    __tablename__ = "country_population"

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String, index=True)
    population = Column(BigInteger, nullable=False)
    region = Column(String, index=True, nullable=False)

    def __repr__(self):
        return f"<CountryPopulation(country_name={self.country_name}, population={self.population})>"
