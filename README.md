# mofdb-client

A typed lightweight client wrapping the [mofdb api](https://mof.tech.northwestern.edu/api).

### Example
```python3
from mofdb_client import fetch
for mof in fetch(vf_min=0.5, vf_max=0.99):
    print(f"Mof {mof.name} has {len(mof.isotherms)} isotherms and elements {[str(e) for e in mof.elements]}")
    print(f"This mof's cif file starts with: '{mof.cif.splitlines()[1]}'")
```

```
Mof UTEWUM_clean has 2 isotherms and elements ['Cu', 'H', 'C', 'N']
This mof's cif file starts with: '_audit_creation_date              2014-07-02'
Mof ZECKID_clean has 1 isotherms and elements ['Cu', 'H', 'C', 'N', 'O']
This mof's cif file starts with: '_audit_creation_date              2014-07-02'
Mof AQOMAW_clean has 2 isotherms and elements ['N', 'C', 'H', 'Co', 'Cl', 'O']
This mof's cif file starts with: '_cell_length_a       18.8345'
Mof AQOLOJ_clean has 2 isotherms and elements ['N', 'C', 'H', 'Co', 'Cl']
This mof's cif file starts with: '_cell_length_a       18.794'
Mof SENWOZ_clean has 2 isotherms and elements ['Zn', 'H', 'C', 'O']
This mof's cif file starts with: '_audit_creation_date              2014-07-02'
Mof IYUCIQ_clean has 2 isotherms and elements ['Dy', 'O', 'N', 'C', 'H']
This mof's cif file starts with: '_cell_length_a       29.162'
Mof ORUKET_clean has 2 isotherms and elements ['P', 'O', 'N', 'C', 'H', 'Mg']
This mof's cif file starts with: '_cell_length_a       18.571'
...
```

### Parameters
*fetch* supports a number of arguements
- mofid: str 
- mofkey: str 
- vf_min: float 
- vf_max: float 
- lcd_min: float 
- lcd_max: float 
- pld_min: float 
- pld_max: float 
- sa_m2g_min: float 
- sa_m2g_max: float 
- sa_m2cm3_min: float 
- sa_m2cm3_max: float 
- limit: int

### Design Note
`fetch` is lazy because mofDB is large. Be sure to loop over it with `for mof in fetch()` and NOT `for mof in list(fetch())` since 
building the list will download all the mofs before it starts processing and this will be very slow and may well run out of memory.

### Future Enhancements:
- Retries for transient network failures with exponential backoff
