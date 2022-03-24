# from ..mofdb import fetch

# since the package is installed in developement
# mode (`pip list`) as a symbole link to /src, we can now
# import it like so:  

from mofdb_client import fetch

print(list(fetch(mofid="mofid")))

# list(fetch(mofid="mofid"))[0].isotherms[0].isotherm_data[0].species_data[0]