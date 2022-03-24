import unittest
import pathlib
import os
import sys
import json
from typing import Tuple, Dict

import responses
import urllib
from responses import matchers

def anything_matcher(url: str) -> Tuple[bool,  str]:
    return True, "everything matches!"

class BasicTests(unittest.TestCase):
    def stub(self, name: str, params: Dict[str,any]):
        params = urllib.parse.urlencode(params, doseq=False)
        file_path = pathlib.Path(__file__).parent.resolve()
        with open(os.path.join(file_path, "stubs", f"{name}.json")) as file:
            content = file.read()
            url = f"https://mof.tech.northwestern.edu/mofs.json?{params}"
            print("registering")
            print(url)
            responses.add(responses.GET, url,
                          body=content, status=200)

    @responses.activate
    def test_mof_fields(self):
        from mofdb_client import fetch
        self.stub("mofs_one_page", {})
        mofs = list(fetch())
        mof = mofs[0]
        self.assertEqual(mof.mofid, "[Eu].[O-]C(=O)C(=O)[O-].[O-]C(=O)C1=C([N]C=N1)C(=O)[O-].[O-]C(=O)C1=NC=N[C]1C(=O)[O-].[O-]C(=O)C1=N[C]N=C1C(=O)[O-].[Zn] MOFid-v1.ERROR.cat0")
        self.assertEqual(mof.mofkey, "ZnEu.MUBZPKHOEPUJKR.WQCVMVXXCVLMAN.YCIDFVDEIMPTRS.MOFkey-v1.ERROR")
        self.assertEqual(mof.name, "EVUNIT_clean_h")
        self.assertEqual(mof.void_fraction, 0.23)
        self.assertEqual(mof.surface_area_m2g, 0.0)
        self.assertEqual(mof.surface_area_m2cm3, 0.0)
        self.assertEqual(mof.pld, 2.63)
        self.assertEqual(mof.lcd, 4.37)
        self.assertEqual(mof.pxrd, None)
        self.assertEqual(mof.pore_size_distribution, None)
        self.assertEqual(mof.database, "CoREMOF 2014")
        self.assertEqual(mof.batch_number, None)
        self.assertEqual(mof.elements[0].symbol, "Eu")
        self.assertEqual(mof.elements[0].name, "Europium")
        self.assertEqual(mof.elements[1].symbol, "Zn")
        self.assertEqual(mof.elements[1].name, "Zinc")
        self.assertEqual(mof.cif, "data_EVUNIT_clean_h\r\n_audit_creation_date              2014-07-02\r\n_audit_creation_method            'Materials Studio'\r\n_symmetry_space_group_name_H-M    'P1'\r\n_symmetry_Int_Tables_number       1\r\n_symmetry_cell_setting            triclinic\r\nloop_\r\n_symmetry_equiv_pos_as_xyz\r\n  x,y,z\r\n_cell_length_a                    9.8438\r\n_cell_length_b                    13.2067\r\n_cell_length_c                    16.4919\r\n_cell_angle_alpha                 81.1208\r\n_cell_angle_beta                  72.6358\r\n_cell_angle_gamma                 68.1188\r\nloop_\r\n_atom_site_label\r\n_atom_site_type_symbol\r\n_atom_site_fract_x\r\n_atom_site_fract_y\r\n_atom_site_fract_z\r\n_atom_site_U_iso_or_equiv\r\n_atom_site_adp_type\r\n_atom_site_occupancy\r\nEu1    Eu    0.58145   0.61809   0.42715   0.01267  Uiso   1.00\r\nEu2    Eu    0.62669   0.88191   0.07285   0.01267  Uiso   1.00\r\nEu3    Eu    0.41855   0.38191   0.57285   0.01267  Uiso   1.00\r\nEu4    Eu    0.37331   0.11809   0.92715   0.01267  Uiso   1.00\r\nZn1    Zn    0.32462   0.11040   0.31778   0.01267  Uiso   1.00\r\nZn2    Zn    0.11411   0.16050   0.54572   0.01267  Uiso   1.00\r\nZn3    Zn    0.75280   0.38960   0.18222   0.01267  Uiso   1.00\r\nZn4    Zn    0.82033   0.33950   0.95428   0.01267  Uiso   1.00\r\nZn5    Zn    0.67538   0.88960   0.68222   0.01267  Uiso   1.00\r\nZn6    Zn    0.88589   0.83950   0.45428   0.01267  Uiso   1.00\r\nZn7    Zn    0.24720   0.61040   0.81778   0.01267  Uiso   1.00\r\nZn8    Zn    0.17967   0.66050   0.04572   0.01267  Uiso   1.00\r\nC1     C     0.42730   0.89740   0.40860   0.01267  Uiso   1.00\r\nC2     C     0.26870   0.91720   0.41180   0.01267  Uiso   1.00\r\nC3     C     0.17430   0.85670   0.43990   0.01267  Uiso   1.00\r\nC4     C     0.19130   0.74570   0.48030   0.01267  Uiso   1.00\r\nC5     C     0.05150   0.01360   0.38740   0.01267  Uiso   1.00\r\nC6     C     0.55190   0.42420   0.35740   0.01267  Uiso   1.00\r\nC7     C     0.52985   0.33240   0.32810   0.01267  Uiso   1.00\r\nC8     C     0.43324   0.27282   0.35830   0.01267  Uiso   1.00\r\nC9     C     0.31450   0.27030   0.43770   0.01267  Uiso   1.00\r\nC10    C     0.56950   0.22130   0.23310   0.01267  Uiso   1.00\r\nC11    C     0.73330   0.60260   0.09140   0.01267  Uiso   1.00\r\nC12    C     0.59770   0.58280   0.08820   0.01267  Uiso   1.00\r\nC13    C     0.47090   0.64330   0.06010   0.01267  Uiso   1.00\r\nC14    C     0.41730   0.75430   0.01970   0.01267  Uiso   1.00\r\nC15    C     0.45250   0.48640   0.11260   0.01267  Uiso   1.00\r\nC16    C     0.33350   0.07580   0.14260   0.01267  Uiso   1.00\r\nC17    C     0.19035   0.16760   0.17190   0.01267  Uiso   1.00\r\nC18    C     0.06436   0.22718   0.14170   0.01267  Uiso   1.00\r\nC19    C     0.02250   0.22970   0.06230   0.01267  Uiso   1.00\r\nC20    C     0.02390   0.27870   0.26690   0.01267  Uiso   1.00\r\nC21    C     0.57270   0.10260   0.59140   0.01267  Uiso   1.00\r\nC22    C     0.73130   0.08280   0.58820   0.01267  Uiso   1.00\r\nC23    C     0.82570   0.14330   0.56010   0.01267  Uiso   1.00\r\nC24    C     0.80870   0.25430   0.51970   0.01267  Uiso   1.00\r\nC25    C     0.94850   0.98640   0.61260   0.01267  Uiso   1.00\r\nC26    C     0.44810   0.57580   0.64260   0.01267  Uiso   1.00\r\nC27    C     0.47015   0.66760   0.67190   0.01267  Uiso   1.00\r\nC28    C     0.56676   0.72718   0.64170   0.01267  Uiso   1.00\r\nC29    C     0.68550   0.72970   0.56230   0.01267  Uiso   1.00\r\nC30    C     0.43050   0.77870   0.76690   0.01267  Uiso   1.00\r\nC31    C     0.26670   0.39740   0.90860   0.01267  Uiso   1.00\r\nC32    C     0.40230   0.41720   0.91180   0.01267  Uiso   1.00\r\nC33    C     0.52910   0.35670   0.93990   0.01267  Uiso   1.00\r\nC34    C     0.58270   0.24570   0.98030   0.01267  Uiso   1.00\r\nC35    C     0.54750   0.51360   0.88740   0.01267  Uiso   1.00\r\nC36    C     0.66650   0.92420   0.85740   0.01267  Uiso   1.00\r\nC37    C     0.80965   0.83240   0.82810   0.01267  Uiso   1.00\r\nC38    C     0.93564   0.77282   0.85830   0.01267  Uiso   1.00\r\nC39    C     0.97750   0.77030   0.93770   0.01267  Uiso   1.00\r\nC40    C     0.97610   0.72130   0.73310   0.01267  Uiso   1.00\r\nC41    C     0.68530   0.75000   0.25000   0.01267  Uiso   1.00\r\nC42    C     0.52710   0.75000   0.25000   0.01267  Uiso   1.00\r\nC43    C     0.31470   0.25000   0.75000   0.01267  Uiso   1.00\r\nC44    C     0.47290   0.25000   0.75000   0.01267  Uiso   1.00\r\nN1     N     0.19043   0.01594   0.37880   0.01267  Uiso   1.00\r\nN2     N     0.03654   0.91832   0.42420   0.01267  Uiso   1.00\r\nN3     N     0.61730   0.29770   0.24850   0.01267  Uiso   1.00\r\nN4     N     0.45964   0.20352   0.29740   0.01267  Uiso   1.00\r\nN5     N     0.58517   0.48406   0.12120   0.01267  Uiso   1.00\r\nN6     N     0.37906   0.58168   0.07580   0.01267  Uiso   1.00\r\nN7     N     0.16350   0.20230   0.25150   0.01267  Uiso   1.00\r\nN8     N     0.96056   0.29648   0.20260   0.01267  Uiso   1.00\r\nN9     N     0.80957   0.98406   0.62120   0.01267  Uiso   1.00\r\nN10    N     0.96346   0.08168   0.57580   0.01267  Uiso   1.00\r\nN11    N     0.38270   0.70230   0.75150   0.01267  Uiso   1.00\r\nN12    N     0.54036   0.79648   0.70260   0.01267  Uiso   1.00\r\nN13    N     0.41483   0.51594   0.87880   0.01267  Uiso   1.00\r\nN14    N     0.62094   0.41832   0.92420   0.01267  Uiso   1.00\r\nN15    N     0.83650   0.79770   0.74850   0.01267  Uiso   1.00\r\nN16    N     0.03944   0.70352   0.79740   0.01267  Uiso   1.00\r\nO1     O     0.47806   0.97228   0.37200   0.01267  Uiso   1.00\r\nO2     O     0.50565   0.81040   0.43950   0.01267  Uiso   1.00\r\nO3     O     0.31586   0.68178   0.49130   0.01267  Uiso   1.00\r\nO4     O     0.07269   0.72112   0.50190   0.01267  Uiso   1.00\r\nO5     O     0.64692   0.46344   0.30852   0.01267  Uiso   1.00\r\nO6     O     0.47528   0.46482   0.42962   0.01267  Uiso   1.00\r\nO7     O     0.27794   0.33388   0.49524   0.01267  Uiso   1.00\r\nO8     O     0.25351   0.19910   0.44128   0.01267  Uiso   1.00\r\nO9     O     0.74499   0.68894   0.30548   0.01267  Uiso   1.00\r\nO10    O     0.46778   0.69593   0.30891   0.01267  Uiso   1.00\r\nO11    O     0.82234   0.52772   0.12800   0.01267  Uiso   1.00\r\nO12    O     0.75555   0.68960   0.06050   0.01267  Uiso   1.00\r\nO13    O     0.48894   0.81822   0.00870   0.01267  Uiso   1.00\r\nO14    O     0.29571   0.77888   0.99810   0.01267  Uiso   1.00\r\nO15    O     0.41888   0.03656   0.19148   0.01267  Uiso   1.00\r\nO16    O     0.36972   0.03518   0.07038   0.01267  Uiso   1.00\r\nO17    O     0.10706   0.16612   0.00476   0.01267  Uiso   1.00\r\nO18    O     0.89389   0.30090   0.05872   0.01267  Uiso   1.00\r\nO19    O     0.73941   0.81106   0.19452   0.01267  Uiso   1.00\r\nO20    O     0.47262   0.80407   0.19109   0.01267  Uiso   1.00\r\nO21    O     0.52194   0.02772   0.62800   0.01267  Uiso   1.00\r\nO22    O     0.49435   0.18960   0.56050   0.01267  Uiso   1.00\r\nO23    O     0.68414   0.31822   0.50870   0.01267  Uiso   1.00\r\nO24    O     0.92731   0.27888   0.49810   0.01267  Uiso   1.00\r\nO25    O     0.35308   0.53656   0.69148   0.01267  Uiso   1.00\r\nO26    O     0.52472   0.53518   0.57038   0.01267  Uiso   1.00\r\nO27    O     0.72206   0.66612   0.50476   0.01267  Uiso   1.00\r\nO28    O     0.74649   0.80090   0.55872   0.01267  Uiso   1.00\r\nO29    O     0.25501   0.31106   0.69452   0.01267  Uiso   1.00\r\nO30    O     0.53222   0.30407   0.69109   0.01267  Uiso   1.00\r\nO31    O     0.17766   0.47228   0.87200   0.01267  Uiso   1.00\r\nO32    O     0.24445   0.31040   0.93950   0.01267  Uiso   1.00\r\nO33    O     0.51106   0.18178   0.99130   0.01267  Uiso   1.00\r\nO34    O     0.70429   0.22112   0.00190   0.01267  Uiso   1.00\r\nO35    O     0.58112   0.96344   0.80852   0.01267  Uiso   1.00\r\nO36    O     0.63028   0.96482   0.92962   0.01267  Uiso   1.00\r\nO37    O     0.89294   0.83388   0.99524   0.01267  Uiso   1.00\r\nO38    O     0.10611   0.69910   0.94128   0.01267  Uiso   1.00\r\nO39    O     0.26059   0.18894   0.80548   0.01267  Uiso   1.00\r\nO40    O     0.52738   0.19593   0.80891   0.01267  Uiso   1.00\r\nH1     H     0.96276   0.08716   0.36456   0.01267  Uiso   1.00\r\nH2     H     0.62273   0.17938   0.17002   0.01267  Uiso   1.00\r\nH3     H     0.41448   0.41284   0.13544   0.01267  Uiso   1.00\r\nH4     H     0.97212   0.32062   0.32998   0.01267  Uiso   1.00\r\nH5     H     0.37727   0.82062   0.82998   0.01267  Uiso   1.00\r\nH6     H     0.58552   0.58716   0.86456   0.01267  Uiso   1.00\r\nH7     H     0.02788   0.67938   0.67002   0.01267  Uiso   1.00\r\n",)
        self.assertEqual(mof.url, "/mofs/1.json")
        self.assertEqual(mof.adsorbates[0].name, "Nitrogen")
        self.assertEqual(mof.adsorbates[0].id, 80)
        self.assertEqual(mof.adsorbates[0].InChIKey, "IJGRMHOSHXDMSA-UHFFFAOYSA-N")
        self.assertEqual(mof.adsorbates[0].InChICode, "InChI=1S/N2/c1-2")
        self.assertEqual(mof.adsorbates[0].formula, "N2")

        iso = mof.isotherms[0]
        self.assertEqual(iso.id, 118)
        self.assertEqual(iso.batch_number, None)
        self.assertEqual(iso.adsorbates[0].id, 80)
        self.assertEqual(iso.adsorbates[0].formula, "N2")
        self.assertEqual(iso.digitizer, "Nathaniel Tracy-Amoroso")
        self.assertEqual(iso.simin, "SimulationType                MonteCarlo\nNumberOfCycles                7500\nNumberOfInitializationCycles  7500\nPrintEvery                    5000\nContinueAfterCrash            no\nForcefield                    UFF\nRemoveAtomNumberCodeFromLabel yes\nFramework 0\nFrameworkName EVUNIT_clean_h\nUnitCells 3 3 2\nHeliumVoidFraction 0.29\nExternalTemperature 77\nExternalPressure 10 80 200 500 1000 1500 2000 5000 20000 40000 60000 80000 99900\nComponent 0 MoleculeName             N2\nMoleculeDefinition       TraPPE\nTranslationProbability   0.5\nReinsertionProbability   0.5\nSwapProbability          0.5\nRotationProbabilty       0.5\nCreateNumberOfMolecules  0",)
        self.assertEqual(iso.DOI, "TBD-COREMOF2")
        self.assertEqual(iso.date, "2019-26-07")
        self.assertEqual(iso.temperature, 77.0)
        self.assertEqual(iso.adsorbent_forcefield, "UFF")
        self.assertEqual(iso.molecule_forcefield, "TraPPE")
        self.assertEqual(iso.adsorbent.id, 1)
        self.assertEqual(iso.adsorbent.name, "EVUNIT_clean_h")
        self.assertEqual(iso.category, "exp")
        self.assertEqual(iso.adsorptionUnits, "cm3(STP)/g")
        self.assertEqual(iso.pressureUnits, "Pa")
        self.assertEqual(iso.compositionType, "wt%")
        self.assertEqual(iso.isotherm_url, "/isotherms/118.json")
        datum = mof.isotherms[0].isotherm_data[1]
        self.assertEqual(len(mof.isotherms[0].isotherm_data), 13)
        self.assertEqual(datum.pressure, 60000.0)
        self.assertEqual(datum.total_adsorption, 57.5711)
        self.assertEqual(datum.species_data[0].InChIKey, "IJGRMHOSHXDMSA-UHFFFAOYSA-N")
        self.assertEqual(datum.species_data[0].name, "Nitrogen")
        self.assertEqual(datum.species_data[0].composition, 1.0)
        self.assertEqual(datum.species_data[0].adsorption, 57.5711)


    @responses.activate
    def test_limit(self):
        from mofdb_client import fetch
        self.stub("mofs_one_page", {})
        mofs = list(fetch(limit=3))
        self.assertEqual(len(mofs), 3)

    @responses.activate
    def test_mofid_match(self):
        from mofdb_client import fetch
        qahdua = "[O-]C(=O)C1=[C][C]=C([C]=[C]1)C(=O)[O-].[O-]C(=O)C1=[C][C]=C([C]=[C]1)C1=[C][C]=[C]C(=[C]1)C1=[C][C]=C([C]=[C]1)C(=O)[O-].[Zn][O]([Zn])([Zn])[Zn] MOFid-v1.UNKNOWN.cat2"
        self.stub("mofid", {'mofid': qahdua})
        mofs = list(fetch(mofid=qahdua))
        self.assertEqual(len(mofs), 1)
        self.assertEqual(mofs[0].name, 'QAHDUA_clean')

    @responses.activate
    def test_mofkey_match(self):
        from mofdb_client import fetch
        mofkey = "Zn.LRMYCMFGPUSZCE.RHFSRTQXETUEBB.MOFkey-v1.UNKNOWN"
        self.stub("mofid", {'mofkey': mofkey})
        mofs = list(fetch(mofkey=mofkey))
        self.assertEqual(len(mofs), 1)
        self.assertEqual(mofs[0].name, 'QAHDUA_clean')


    @responses.activate
    def test_vf_min(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'vf_min': prop})
        mofs = list(fetch(vf_min=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_vf_max(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'vf_max': prop})
        mofs = list(fetch(vf_max=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_lcd_min(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'lcd_min': prop})
        mofs = list(fetch(lcd_min=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_lcd_max(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'lcd_max': prop})
        mofs = list(fetch(lcd_max=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_pld_min(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'pld_min': prop})
        mofs = list(fetch(pld_min=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_pld_max(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'pld_max': prop})
        mofs = list(fetch(pld_max=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_sa_m2g_min(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'sa_m2g_min': prop})
        mofs = list(fetch(sa_m2g_min=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_sa_m2g_max(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'sa_m2g_max': prop})
        mofs = list(fetch(sa_m2g_max=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_sa_m2cm3_min(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'sa_m2cm3_min': prop})
        mofs = list(fetch(sa_m2cm3_min=prop))
        self.assertEqual(len(mofs), 100)

    @responses.activate
    def test_sa_m2cm3_max(self):
        from mofdb_client import fetch
        prop = 13.3
        self.stub("mofs_one_page", {'sa_m2cm3_max': prop})
        mofs = list(fetch(sa_m2cm3_max=prop))
        self.assertEqual(len(mofs), 100)




if __name__ == '__main__':

    # we won't need those 2 lines since we installed the pckge in dev mode
    # file_path = pathlib.Path(__file__).parent.parent.resolve()
    # sys.path.append(os.path.join(file_path, "src"))

    unittest.main()
