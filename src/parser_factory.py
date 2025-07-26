from src.config import config
from src.parsers.statstimes import StatTimesPopulationParser
from src.parsers.wiki import WikiPopulationParser


def get_parser():
    if config.population_source == "wiki":
        return WikiPopulationParser()
    elif config.population_source == "statstimes":
        return StatTimesPopulationParser()
    else:
        raise ValueError(f"Unknown POPULATION_SOURCE: {config.population_source}")
