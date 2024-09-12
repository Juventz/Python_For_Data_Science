import time
from datetime import datetime

# Calculates the elapsed time in seconds since the epoch.
# epoch is defined in Unix as January 1, 1970
# elaspse_seconds = current_time - epoch_time and is a float
elapsed_seconds = time.time()

# current_date in the format like: 2021-09-01 12:00:00.000000
current_date = datetime.now()

# elapsed_seconds: .2e : 2 decimal places in scientific notation
scientifici_notation = f"{elapsed_seconds:.2e}"

# elapsed_second: .4f : 4 decimal places
# %b %d %Y : month day year in abbreviated form
print(
    f"Seconds since January 1, 1970: {elapsed_seconds:,.4f} "
    f"or {scientifici_notation} in scientific notation"
)
print(current_date.strftime("%b %d %Y"))
