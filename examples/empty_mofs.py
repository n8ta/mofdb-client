from mofdb_client import fetch

try:
    for mof in fetch(vf_min=0.001, vf_max=0.1):
        print(f"{mof.name} has a void fraction of {mof.void_fraction}. The cif is {len(mof.cif)} bytes")
except Exception as e:
    print("example caught it!")