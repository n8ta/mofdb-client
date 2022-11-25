from mofdb_client import fetch
# Fetch all mofs with void fraction >= 0.5 and <= 0.99
# Convert all isotherm loading units to mmol/g and all pressures to atmospheres
for mof in fetch(vf_min=0.5, vf_max=0.99, loading_unit="mmol/g", pressure_unit="atm"):
    print(f"Mof {mof.name} has {len(mof.isotherms)} isotherms and elements {[str(e) for e in mof.elements]}")
    print(f"This mof's cif file starts with: '{mof.cif.splitlines()[1]}'")