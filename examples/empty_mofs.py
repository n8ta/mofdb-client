from mofdb_client import fetch

try:
    for mof in fetch(vf_min=0.001, vf_max=0.1):
        # print(f"{mof.name} has a void fraction of {mof.void_fraction}. The cif is {len(mof.cif)} bytes")
        if mof.void_fraction < 0.001 or mof.void_fraction > 0.1:
            print(mof.void_fraction, mof.name)
            raise Exception("bad mof")
except Exception as e:
    print(e)
    print("example caught it!")