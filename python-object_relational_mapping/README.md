# Python - Object-relational mapping

This project covers Object-Relational Mapping (ORM) using Python with MySQL databases.

## Description

This project demonstrates how to connect Python scripts to MySQL databases using two different approaches:

1. Using the MySQLdb module to connect directly to a MySQL database
2. Using SQLAlchemy ORM (Object-Relational Mapping) to abstract the storage layer

## Technologies

- Python 3.8.5
- MySQL 8.0
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- Ubuntu 20.04 LTS

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files use the pycodestyle (version 2.7.\*)
- All files must be executable
- All modules, classes, and functions have proper documentation

## Files

### MySQLdb Scripts

- `0-select_states.py` - Lists all states from the database
- `1-filter_states.py` - Lists all states with a name starting with N
- `2-my_filter_states.py` - Displays all values in the states table where name matches the argument
- `3-my_safe_filter_states.py` - Safe from MySQL injections version
- `4-cities_by_state.py` - Lists all cities from the database
- `5-filter_cities.py` - Lists all cities of a state

### SQLAlchemy Scripts

- `model_state.py` - Contains the class definition of State
- `model_city.py` - Contains the class definition of City
- `7-model_state_fetch_all.py` - Lists all State objects
- `8-model_state_fetch_first.py` - Prints the first State object
- `9-model_state_filter_a.py` - Lists all State objects that contain the letter a
- `10-model_state_my_get.py` - Prints the State object with the name passed as argument
- `11-model_state_insert.py` - Adds the State object "Louisiana" to the database
- `12-model_state_update_id_2.py` - Changes the name of a State object
- `13-model_state_delete_a.py` - Deletes all State objects with a name containing the letter a
- `14-model_city_fetch_by_state.py` - Prints all City objects from the database

## Author

Holberton School Project
