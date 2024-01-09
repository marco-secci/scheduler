import mysql.connector
from itertools import combinations
import datetime as dt
import os
from dotenv import load_dotenv

# Internal files:
from functions import get_next_game_date, rotate_teams
from setup import *

# ======================================= LOGGING STUFF ================================= #
import logging as log

# Checking the existence of the logs folder in the parent folder:
log_directory = "../logs/"
if not os.path.exists(log_directory):
    # If it does not exist, create it:
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "scheduler.log")
log.basicConfig(
    filename=log_file_path,
    level=log.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ======================================= LOGGING STUFF ================================= #

# ======================================= ENVIRONMENT SETUP ================================= #

# Logging in database:
load_dotenv()

# Database connection parameters
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}

# ======================================= ENVIRONMENT SETUP ================================= #

# ======================================= DATABASE CONNECTION SETUP ================================= #

# Connecting to db:
# Logging:
log.info(f"{dt.datetime.now()}: Connecting to database...")
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    log.info(f"{dt.datetime.now()}: Connection established successfully. ")
except mysql.connector.Error as e:
    log.error(
        f"{dt.datetime.now()}: There was an error establishing connection to the database. {e}"
    )
    raise ConnectionError("Connection failed. ")

# ======================================= DATABASE CONNECTION SETUP ================================= #

# ======================================= SCHEDULE CREATION ================================= #

# Fetching all the tuples composed of team name and arena name from DB:
cursor.execute(
    """
    SELECT s.codice_società, s.nome, i.codice_impianto 
    FROM società s
    JOIN impianto i ON s.codice_società = i.cod_proprietario
"""
)
team_with_arena_tuples = cursor.fetchall()
# Logging:
log.info(
    f"{dt.datetime.now()}: Fetched all the tuples composed of team name and team's arena. "
)

# Initialize a dictionary to track when each team last played:
when_team_last_played_dict = {
    team[0]: season_start - dt.timedelta(weeks=1) for team in team_with_arena_tuples
}

# Generating the schedule using a Round-robin algorithm:
schedule = []

# Logging:
log.info(f"{dt.datetime.now()}: Generating schedule... ")

# Schedule for each pair of teams, two games, home and away:
for first_team, second_team in combinations(team_with_arena_tuples, 2):
    # First game - First team at home:
    first_game_date = get_next_game_date(when_team_last_played_dict[first_team[0]])
    if first_game_date:
        schedule.append(
            (
                first_team[2],
                first_team[0],
                second_team[0],
                first_game_date,
                default_game_time,
                default_result,
                winner,
            )
        )
        # Updating dictionary:
        when_team_last_played_dict[first_team[0]] = first_game_date
        when_team_last_played_dict[second_team[0]] = first_game_date

    # Second game - Second team at home:
    second_game_date = get_next_game_date(when_team_last_played_dict[second_team[0]])
    if second_game_date:
        schedule.append(
            (
                second_team[2],
                second_team[0],
                first_team[0],
                second_game_date,
                default_game_time,
                default_result,
                winner,
            )
        )
        # Updating dictionary:
        when_team_last_played_dict[second_team[0]] = second_game_date
        when_team_last_played_dict[first_team[0]] = second_game_date

# Logging:
log.info(f"{dt.datetime.now()}: Schedule created successfully. ")

# Inserting games into the games' table:
for game in schedule:
    try:
        cursor.execute(
            """
            INSERT INTO partita (codice_impianto, codice_casa, codice_trasferta, data, orario, risultato_finale, codice_vincitrice)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            game,
        )
        # Logging:
        log.info(
            f"{dt.datetime.now()}: Schedule inserted into the database successfully. "
        )
    except mysql.connector.Error as e:
        # Logging:
        log.error(f"{dt.datetime.now()}: Error inserting game's data: {game}")
        raise ConnectionError(f"Error inserting game into database: {e}")

# ======================================= SCHEDULE CREATION ================================= #

# Closing connection:
conn.commit()
cursor.close()
conn.close()
# Logging:
log.info(f"{dt.datetime.now()}: Connection closed. ")
