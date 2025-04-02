from .modules.component import DICONDEComponent
from .modules.componentseries import DICONDEComponentSeries
from .modules.componentstudy import DICONDEComponentStudy
from .modules.ndeequipment import DICONDENDEquipment
from .modules.ndegeometry import DICONDENDEGeometry
from .modules.ndeindication import DICONDENDEIndication
from pydicom.datadict import add_dict_entries

class Diconde(DICONDEComponent, DICONDEComponentSeries, DICONDEComponentStudy, DICONDENDEquipment, DICONDENDEGeometry, DICONDENDEIndication):
    def __init__(self):
        super().__init__()

    @staticmethod
    def use_diconde_names():
        """Use Diconde21 names for addresses"""
        entries = {
            0x00142160: ("SH", "1", "Material Name", "", "MaterialName"),
            0x00081048: ("PN", "1", "Inspecting Company Name", "", "InspectingCompanyName")
        }
        add_dict_entries(entries)
