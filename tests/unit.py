import unittest

from mofdb_client import fetch, InvalidUnit


class BasicTests(unittest.TestCase):

    def test_e2e_headers(self):
        for mof in fetch(loading_unit="g/l", limit=10):
            for iso in mof.isotherms:
                self.assertEqual(iso.adsorptionUnits, "g/l")
        for mof in fetch(pressure_unit="atm", limit=10):
            for iso in mof.isotherms:
                self.assertEqual(iso.pressureUnits, "atm")
        for mof in fetch(pressure_unit="atm", loading_unit="g/l", limit=10):
            for iso in mof.isotherms:
                self.assertEqual(iso.pressureUnits, "atm")
                self.assertEqual(iso.adsorptionUnits, "g/l")

    def test_raises_for_bad_loading(self):
        def test_raises():
            for mof in fetch(loading_unit="lll", telemetry=False):
                print(mof.name)
        self.assertRaises(InvalidUnit, test_raises)

    def test_raises_for_bad_pressure(self):
        def test_raises():
            for mof in fetch(pressure_unit="123123", telemetry=False):
                print(mof.name)
        self.assertRaises(InvalidUnit, test_raises)

    def test_raises_for_bad_pressure_and_loading(self):
        def test_raises():
            for mof in fetch(pressure_unit="123123", loading_unit="123", telemetry=False):
                print(mof.name)
        self.assertRaises(InvalidUnit, test_raises)

    def test_multiple_pages(self):
        mofs = list(fetch(limit=30))
        self.assertEqual(30, len(mofs))

    def test_mof_fields(self):
        mofs = list(fetch(mofid="[O-]C(=O)c1ccc(cc1)C(=O)[O-].[Zn][O]([Zn])([Zn])[Zn] MOFid-v1.pcu.cat0", vf_max=0.799))
        mof = mofs[0]
        self.assertEqual(mof.mofid,"[O-]C(=O)c1ccc(cc1)C(=O)[O-].[Zn][O]([Zn])([Zn])[Zn] MOFid-v1.pcu.cat0")
        self.assertEqual(mof.mofkey.strip(), "Zn.KKEYFWRCBNTPAC.MOFkey-v1.pcu")
        self.assertEqual(mof.name, "hMOF-0")
        self.assertEqual(mof.void_fraction, 0.795539)
        specific_iso = None
        for iso in mof.isotherms:
            if iso.id == 5105121:
                specific_iso = iso
        self.assertEqual(specific_iso.adsorbates[0].id, 24)
        self.assertEqual(specific_iso.adsorbates[0].InChIKey, "CURLTUGMZLYLDI-UHFFFAOYSA-N")
        self.assertEqual(specific_iso.adsorbates[0].name, "CarbonDioxide")
        self.assertEqual(specific_iso.adsorbates[0].InChICode, "InChI=1S/CO2/c2-1-3")
        self.assertEqual(specific_iso.adsorbates[0].formula, "CO2")
        self.assertEqual(len(specific_iso.isotherm_data), 5)
        self.assertEqual(specific_iso.isotherm_data[0].pressure, 0.01)
        self.assertEqual(specific_iso.isotherm_data[0].total_adsorption, 0.0224065)
        self.assertEqual(len(specific_iso.isotherm_data[0].species_data), 1)

    def test_limit(self):
        mofs = list(fetch(limit=3))
        self.assertEqual(len(mofs), 3)

    def test_name(self):
        mofs = list(fetch(name="LEDJOU_clean"))
        for mof in mofs:
            self.assertEqual(mof.name, "LEDJOU_clean")
        self.assertEqual(1, len(mofs))

    # def test_mofkey_match(self):
    #     mofkey = "Zn.CDOWNLMZVKJRSC.OHLSHRJUBRUKAN.WWWSEKAIASUCDB.MOFkey-v1.pcu UNKNOWN"
    #     mofs = list(fetch(mofkey=mofkey))
    #     self.assertEqual(len(mofs), 1)
    #     self.assertEqual(mofs[0].name, 'hMOF-200')

    def test_vf_min(self):
        mofs = list(fetch(vf_min=0.1, limit=13))
        for mof in mofs:
            self.assertTrue(mof.void_fraction >= 0.1)

    def test_vf_max(self):
        mofs = list(fetch(vf_max=0.1, limit=13))
        for mof in mofs:
            self.assertTrue(mof.void_fraction <= 0.1)

    def test_lcd_min(self):
        mofs = list(fetch(lcd_min=10, limit=10))
        for mof in mofs:
            self.assertTrue(mof.lcd >= 10)

    def test_lcd_max(self):
        mofs = list(fetch(lcd_max=10, limit=10))
        for mof in mofs:
            self.assertTrue(mof.lcd <= 10)

    def test_pld_min(self):
        mofs = list(fetch(pld_min=10, limit=10))
        for mof in mofs:
            self.assertTrue(mof.pld >= 10)

    def test_pld_max(self):
        mofs = list(fetch(pld_max=10, limit=10))
        for mof in mofs:
            self.assertTrue(mof.pld <= 10)

    def test_sa_m2g_min(self):
        mofs = list(fetch(sa_m2g_min=1000, limit=10))
        for mof in mofs:
            self.assertTrue(mof.surface_area_m2g >= 1000)

    def test_sa_m2g_max(self):
        mofs = list(fetch(sa_m2g_max=1000, limit=10))
        for mof in mofs:
            self.assertTrue(mof.surface_area_m2g <= 1000)

    def test_sa_m2cm3_min(self):
        mofs = list(fetch(sa_m2cm3_min=1000, limit=10))
        for mof in mofs:
            self.assertTrue(mof.surface_area_m2cm3 >= 1000)

    def test_sa_m2cm3_max(self):
        mofs = list(fetch(sa_m2cm3_max=1000, limit=10))
        for mof in mofs:
            self.assertTrue(mof.surface_area_m2cm3 <= 1000)


if __name__ == '__main__':
    unittest.main()
