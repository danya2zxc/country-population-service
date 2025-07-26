# 🌍 Country Population Service

**Status:** 🚀 MVP released (`v1.0.0`)

This service fetches country population data from a web source, stores it in a PostgreSQL database, and prints aggregated regional statistics to the console. The entire application is containerized using Docker and orchestrated with Docker Compose.

---

## ✨ Features

- ⚡ **Asynchronous Processing:** Built with `asyncio`, `aiohttp`, and `asyncpg` for high performance.
- 🌐 **Multiple Data Sources:** Supports parsing from [Wikipedia](https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959) and [statisticstimes.com](https://statisticstimes.com/demographics/countries-by-population.php). The source can be switched via an environment variable.
- 🐳 **Dockerized:** All services (`db`, `get_data`, `print_data`) are managed by Docker Compose.
- 🏗️ **Clean Architecture:** Code is structured into layers (service, repository, parser).
- 📊 **Efficient Aggregation:** Uses a single SQL query with window functions to generate regional reports.

---

## 🛠️ Prerequisites

- 🐍 Docker
- 🐳 Docker Compose

---

## 🚦 How to Run

1.  📥 **Clone the repository:**
    ```bash
    git clone https://github.com/danya2zxc/country-population-service
    cd country-population-service
    ```

2.  ⚙️ **Create a `.env` file from the example:**
    ```bash
    cp .env.example .env
    ```
    You can edit `.env` to change the `POPULATION_SOURCE` (options: "wiki", "statstimes").

3.  📦 **Fetch and save data:**
    This command builds the Docker image, starts the database, and runs the `get_data` service to populate the database.
    ```bash
    docker-compose up get_data
    ```

4.  📊 **Print aggregated data:**
    After the `get_data` service finishes, run this command to see the results.
    ```bash
    docker-compose up print_data
    ```

---

## 🖨️ Example Output

```
Name of region: Africa
Total population of region: 1480770524
Largest country: Nigeria
Largest country population: 227882945
Smallest country: Saint Helena
Smallest country population: 5289

Name of region: Asia
Total population of region: 4778004490
...
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
