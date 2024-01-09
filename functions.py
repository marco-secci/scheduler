import datetime as dt
import logging as log
import os
import datetime as dt

# Checking the existence of the logs folder in the parent folder:
log_directory = "../logs/"
if not os.path.exists(log_directory):
    # If it does not exist, create it:
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "functions.log")
log.basicConfig(
    filename=log_file_path,
    level=log.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# =========================== #
# GET NEXT GAME DATE FUNCTION #
# =========================== #
def get_next_game_date(last_game_date):
    """
    Takes the last game date as input and returns the
    next week's game date.
    """
    log.info(f"{dt.datetime.now()}: Called get_next_game_date(). ")
    return last_game_date + dt.timedelta(weeks=1)


# ===================== #
# ROTATE TEAMS FUNCTION #
# ===================== #
def rotate_teams(teams):
    """Rotate the team list, keeping the first team fixed."""
    log.info(f"{dt.datetime.now()}: Called rotate_teams(). ")
    return [teams[0]] + teams[-1:] + teams[1:-1]
