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
        # sorted address
        entries = {
            0x00081048: ("PN", "1", "Inspecting Company Name", "", "InspectingCompanyName"),
            0x00100010: ("PN", "1", "Component Name", "", "ComponentName"),
            0x00100020: ("PN", "1", "Component ID Number", "", "ComponentIDNumber"),
            0x00100030: ("PN", "1", "Component Manufacturing Date", "", "ComponentManufacturingDate"),
            0x00100040: ("CS", "1", "Patient Sex", "", "PatientSex"),
            0x00101000: ("PN", "1-N", "Other Component IDs", "", "OtherComponentIDs"),
            0x00101001: ("PN", "1-N", "Other Component Names", "", "OtherComponentNames"),
            0x00101002: ("SQ", "1", "Other Component IDs Sequence", "", "OtherComponentIDsSequence"),
            0x00101001: ("PN", "1-N", "Other Component Names", "", "OtherComponentNames"),
            0x00104000: ("LT", "1", "Component Notes", "", "ComponentNotes"),
            0x00140025: ("PN", "1", "Component Manufacturing Procedure", "", "ComponentManufacturingProcedure"),
            0x00140028: ("PN", "1", "ComponentManufacturer", "", "Component Manufacturer"),
            0x00140042: ("PN", "1", "Material Grade", "", "MaterialGrade"),
            0x00140044: ("PN", "1", "Material Properties Description", "", "MaterialPropertiesDescription"),
            0x00140046: ("PN", "1", "Material Notes", "", "MaterialNotes"),
            0x00140030: ("PN", "1", "Material Thickness", "", "MaterialThickness"),
            0x00140032: ("PN", "1", "Material Pipe Diameter", "", "MaterialPipeDiameter"),
            0x00140034: ("PN", "1", "Material Isolation Diameter", "", "MaterialIsolationDiameter"),
            0x00140050: ("PN", "1", "Component Shape", "", "ComponentShape"),
            0x00140052: ("PN", "1", "Curvature type", "", "CurvatureType"),
            0x00140054: ("PN", "1", "Outer Diameter", "", "OuterDiameter"),
            0x00140056: ("PN", "1", "Inner Diameter", "", "InnerDiameter"),
            0x00140100: ("PN", "1", "Component Welder IDs", "", "ComponentWelderIDs"),
            0x00142160: ("SH", "1", "Material Name", "", "MaterialName"),
        }
        add_dict_entries(entries)
