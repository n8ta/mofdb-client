# mofdb-client
![ci status badge](https://api.travis-ci.com/n8ta/mofdb-client.svg?branch=master)

A typed, fast, lightweight, client wrapping the [mofdb api](https://mof.tech.northwestern.edu/api). This client is the fastest way to access
mofdb since it utilizes the streaming bulk API. Using the regular paginated API will be slow for large page numbers.

### Installation

```shell
python3 -m pip install mofdb_client==0.9.0
```

### Example

![Example of mofdb-client IDE autocompletion](assets/screen0.png)

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

```python3
# Download adsorption data from MOFXDB using mof_client package
# https://github.com/n8ta/mofdb-client
# This is an exmaple to download CO2 adsorption isotherm data for MOFs from hMOF database

# load mofdb_client
from mofdb_client import fetch

# find mof with void fraction less than 0.5 (for example), in 'hMOF' database
for imof in fetch(vf_max=0.5, database='hMOF'):

    # loop over all available isotherms for imof 
    for iiso in imof.isotherms:
        
        # only care about CO2 isotherm
        if iiso.adsorbates[0].formula == 'CO2':
            
            # print matched MOF name
            print(imof.name)

            # print CO2 adsorption isotherm temperature in Kelvin
            print(iiso.temperature)

            # print pressure units
            print(iiso.pressureUnits)

            # print adsorption data units
            print(iiso.adsorptionUnits)
            
            # loop over all adsorption data points in the matched CO2 isotherm 
            # and print each adsorption data points in this isotherm
            for jdata in iiso.isotherm_data:
                print('adsorption data is {} at pressure {}'.format(jdata.total_adsorption, jdata.pressure))
```

```
hMOF-7
298
bar
mol/kg
adsorption data is 1.20398 at pressure 0.01
adsorption data is 3.16225 at pressure 0.1
adsorption data is 5.46213 at pressure 2.5
adsorption data is 2.48016 at pressure 0.05
adsorption data is 4.51262 at pressure 0.5
hMOF-5
298
bar
mol/kg
adsorption data is 0.300224 at pressure 0.01
adsorption data is 1.59719 at pressure 0.1
adsorption data is 2.23941 at pressure 2.5
adsorption data is 1.13122 at pressure 0.05
adsorption data is 2.01518 at pressure 0.5
...
```

### Parameters
*fetch* supports a number of arguments
- name: str
- pressure_unit: str
- loading_unit: str
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
- database: str
- limit: int
- telemetry: bool default true (see telemetry section)

For valid values of pressure_units go here [mof.tech.northwestern.edu/classifications.json](https://mof.tech.northwestern.edu/classifications.json). The mofdb_client will reject invalid
units/pressures and throw `InvalidUnit` exception.

### Design Note
`fetch` is lazy because mofDB is large. Be sure to loop over it with `for mof in fetch()` and NOT `for mof in list(fetch())` since 
building the list will download all the mofs before it starts processing and this will be very slow and may well run out of memory.

### Compatibility
[Tested](https://app.travis-ci.com/github/n8ta/mofdb-client) on Python 3.7 to 3.11. 

### Future Enhancements:
- [ ] Retries for transient network failures with exponential backoff
- [X] Support for unit conversions
- [ ] Only download some columns to save time/bandwidth?

### Telemetry
This package may phone home crash reports that happen in library code when the telemetry arg is true. This is done using 
[sentry](https://docs.sentry.io/). Nothing in addition to fetch params and data captured by default by sentry is ever
captured.

For example this could include:
- a stack trace including your code
- operating system version
- time
- python runtime version
- hostname
- anything else sentry captures by default

### Publishing a new version
Update pyproject.toml version

```
python3 -m build -n
python3 -m twine upload dist/*
```

### Change log


#### 0.9.0
Do not report mofdb exceptions like "InvalidUnit" to sentry error monitoring. These indicate user error.

#### 0.8.0
Fix for crashes on queries returning no mofs. Required a change to mofdb repo as well. Add a 204.response file to zip stream to signal empty response.
