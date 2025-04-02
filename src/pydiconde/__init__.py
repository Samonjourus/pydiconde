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
            0x00080020: ("DA", "1", "Study Date", "", "StudyDate"),
            0x00080021: ("DA", "1", "Series Date", "", "SeriesDate"),
            0x00080030: ("TM", "1", "Study Time", "", "StudyTime"),
            0x00080031: ("TM", "1", "Series Time", "", "SeriesTime"),
            0x00080050: ("SH", "1", "Accession Number", "", "AccessionNumber"),
            0x00080060: ("CS", "1", "Modality", "", "Modality"),
            0x00080090: ("PN", "1", "Component Owner Name", "", "ComponentOwnerName"),
            0x00081048: ("PN", "1-N", "Inspecting Company Name", "", "InspectingCompanyName"),
            0x00081030: ("LO", "1", "Study Description", "", "StudyDescription"),
            0x0008103E: ("LO", "1", "Series Description", "", "SeriesDescription"),
            0x00081050: ("PN", "1-N", "Inspector Name", "", "InspectorName"),
            0x00081060: ("PN", "1-N", "Certifying Inspector Name", "", "CertifyingInspectorName"),
            0x00081070: ("PN", "1-N", "Operator Name", "", "OperatorName"),
            0x00081110: ("SQ", "1", "Referenced Study Sequence", "", "ReferencedStudySequence"),
            0x00081250: ("SQ", "1-N", "Related Series Sequence", "", "RelatedSeriesSequence"),
            0x00100010: ("PN", "1", "Component Name", "", "ComponentName"),
            0x00100020: ("LO", "1", "Component ID Number", "", "ComponentIDNumber"),
            0x00100030: ("DA", "1", "Component Manufacturing Date", "", "ComponentManufacturingDate"),
            0x00100040: ("CS", "1", "Patient Sex", "", "PatientSex"),
            0x00101000: ("LO", "1-N", "Other Component IDs", "", "OtherComponentIDs"),
            0x00101001: ("PN", "1-N", "Other Component Names", "", "OtherComponentNames"),
            0x00101002: ("SQ", "1", "Other Component IDs Sequence", "", "OtherComponentIDsSequence"),
            0x00101001: ("PN", "1-N", "Other Component Names", "", "OtherComponentNames"),
            0x00104000: ("LT", "1", "Component Notes", "", "ComponentNotes"),
            0x00140025: ("ST", "1", "Component Manufacturing Procedure", "", "ComponentManufacturingProcedure"),
            0x00140028: ("ST", "1", "Component Manufacturer", "", "Component Manufacturer"),
            0x00140042: ("SH", "1", "Material Grade", "", "MaterialGrade"),
            0x00140044: ("ST", "1", "Material Properties Description", "", "MaterialPropertiesDescription"),
            0x00140046: ("LT", "1", "Material Notes", "", "MaterialNotes"),
            0x00140030: ("DS", "1", "Material Thickness", "", "MaterialThickness"),
            0x00140032: ("DS", "1", "Material Pipe Diameter", "", "MaterialPipeDiameter"),
            0x00140034: ("DS", "1", "Material Isolation Diameter", "", "MaterialIsolationDiameter"),
            0x00140050: ("CS", "1", "Component Shape", "", "ComponentShape"),
            0x00140052: ("CS", "1", "Curvature Type", "", "CurvatureType"),
            0x00140054: ("DS", "1", "Outer Diameter", "", "OuterDiameter"),
            0x00140056: ("DS", "1", "Inner Diameter", "", "InnerDiameter"),
            0x00140100: ("LO", "1", "Component Welder IDs", "", "ComponentWelderIDs"),
            0x00141010: ("ST", "1", "Actual Environmental Conditions", "", "ActualEnvironmentalConditions"),
            0x00141020: ("DA", "1", "Expiry Date", "", "ExpiryDate"),
            0x00141040: ("ST", "1", "Environmental Conditions", "", "EnvironmentalConditions"),
            0x00142160: ("SH", "1", "Material Name", "", "MaterialName"),
            0x0020000D: ("UI", "1", "Study Instance UID", "", "StudyInstanceUID"),
            0x00200010: ("SH", "1", "Study ID", "", "StudyID"),
            0x0020000D: ("UI", "1", "Study Instance UID", "", "StudyInstanceID"),
            0x0020000E: ("UI", "1", "Series Instance UID", "", "SeriesInstanceID"),
            0x00200011: ("IS", "1", "Series Number", "", "SeriesNumber"),
            0x00324000: ("LT", "1", "Examination Notes", "", "ExaminationNotes"),
        }
        add_dict_entries(entries)
