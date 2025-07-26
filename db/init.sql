
CREATE TABLE IF NOT EXISTS country_population (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    population BIGINT NOT NULL,
    region VARCHAR(100) NOT NULL
);
