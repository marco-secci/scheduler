# scheduler

## Files

- `scheduler.py`: The main file. It creates a game schedule for the specified season with teams and arenas taken from the database.
- `functions.py`: Two functions that are used in the `scheduler.py` file. They are stored in this file to keep the repository better organized.
- `setup.py`: Global variables used in the `scheduler.py` file, stored here for the same reason described for `functions.py`.
- `LBA_management.sql`: A sample database that will be used in the scripts. By running it, it will create on your MySQL connection a database containing data of the 16 teams in the 2023-24 Italian LBA and their respective arenas. 
- `requirements.txt`: File containing all requirements to run the script. See below for instructions on how to use it.
- `.env`: Environment variables, you need to modify username and password! `localhost` and the default database name are already in it, but you can change them of course to your needs.
- `README.md`: This file!

## Instructions

After downloading, modify the `.env` file with your `MySQL` environment connection data and run `LBA_management.sql`. Then, proceed by running `scheduler.py`. If requirements are not met, run the following prompt:

`pip install -r requirements.txt`
There are literally just two packages that need installation but to avoid problems just use the prompt above.

The creation of a virtual environment is not necessary but highly recommended to ensure functionality.



###### by Marco Secci
