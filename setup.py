import datetime as dt

# Define the season start date - October of a given year it's a reasonable choice:
season_start = dt.date(2023, 10, 1)

# Placeholder values for columns we don't have data for yet:
default_result = "0-0"
winner = None  # Will correspond to NULL in SQL
default_game_time = dt.time(20, 30)
