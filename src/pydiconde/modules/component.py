from pydicom import FileDataset
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag
from datetime import datetime
from enum import Enum

class ComponentShape(Enum):
    FLAT = 0
    HOLLOWCYLINDER = 1
    SOLIDCYLINDER = 2
    HOLLOWSPHERE = 3
    SOLIDSPHERE = 4
    COMPOUNDCURVATURE = 5

class CurvatureType(Enum):
    CONCAVE = 0
    CONVEX = 1
    COMPOUND = 2

class otherComponentIDsSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def otherComponentNames(self) -> list[str]:
        """ The component names to be assigned to tag (0010,1001).

        The value is expected to be a person name, but not required.
        """
        return self[Tag(0x0010, 0x1001)].value

    @otherComponentNames.setter
    def otherComponentNames(self, value: list[str]):
        self.add_new(Tag(0x0010, 0x1001), "PN", value)

class DICONDEComponent(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def componentName(self) -> str:
        """ The component name to be assigned to tag (0010,0010).

        The value is expected to be a name. The field is required, but can be
        zero-valued.
        """
        return self[Tag(0x0010, 0x0010)].value

    @property
    def componentIDNumber(self) -> str:
        """ The component ID to be assigned to tag (0010,0020).

        The value is expected to be an ID. The field is required, but can be
        zero-valued.
        """
        return self[Tag(0x0010, 0x0020)].value

    @property
    def otherComponentIDsSequence(self) -> list[otherComponentIDsSequenceElement]:
        """ Sequence of other components within the file, assigned to tag (0010,1002).

        The value is expected to be a list of otherComponentIDsSequenceElements, but not required.
        """
        return self[Tag(0x0010, 0x1002)].value

    @property
    def materialName(self) -> str:
        """ The material name, assigned to tag (0010,2160).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """
        return self[Tag(0x0010, 0x2160)].value

    @property
    def materialGrade(self) -> str:
        """ The material grade, assigned to tag (0014,0042).

        The value is expected to be a short text. The field is not required.
        """
        return self[Tag(0x0014, 0x0042)].value

    @property
    def materialPropertiesDescription(self) -> str:
        """ The material properties description, assigned to tag (0014,0044).

        The value is expected to be a short text. The field is not required.
        """
        return self[Tag(0x0014, 0x0044)].value

    @property
    def materialNotes(self) -> str:
        """ The material notes, assigned to tag (0014,0044).

        The value is expected to be a long text. The field is not required.
        """
        return self[Tag(0x0014, 0x0046)].value

    @property
    def materialThickness(self) -> float:
        """ The material thickness, assigned to tag (0014,0030).

        The value is expected to be a decimal string. The field is not required.
        """
        return self[Tag(0x0014, 0x0030)].value

    @property
    def componentShape(self) -> ComponentShape:
        """ The material thickness, assigned to tag (0014,0050).

        The value is expected to be a ComponentShape. The field is not required.
        """
        return self[Tag(0x0014,0x0050)].value

    @property
    def curvatureType(self) -> CurvatureType:
        """ The material thickness, assigned to tag (0014,0052).

        The value is expected to be a CurvatureType. The field is not required.
        """
        return self[Tag(0x0014,0x0050)].value

    @property
    def outerDiameter(self):
        """ The outer diameter of the specimen in mm, assigned to tag (0014,0054).

        The value is expected to be a decimal string. The field is not required.
        """
        return self[Tag(0x0014,0x0054)].value

    @property
    def innerDiameter(self):
        """ The inner diameter of the specimen in mm, assigned to tag (0014,0055).

        The value is expected to be a decimal string. The field is not required.
        """
        return self[Tag(0x0014,0x0056)].value

    @property
    def componentManufacturingDate(self) -> datetime | None:
        """ The component manufacturing date to be assigned to tag (0010,0030).

        The value is expected to be a date. The value is required, but can be zero-valued.
        """
        return self[Tag(0x0010, 0x0030)].value

    @property
    def patientSex(self) -> str | None:
        """ The patient sex to be assigned to tag (0010,0040).

        The value is required to be a code string, but should be set to 'O'.
        """
        return self[Tag(0x0010, 0x0040)].value

    @property
    def componentNotes(self) -> str | None:
        """ The component notes to be assigned to tag (0010,4000).

        This field is optional, but if defined, should be a long text.
        """
        return self[Tag(0x0010, 0x4000)].value

    @property
    def componentManufacturingProcedure(self) -> str | None:
        """ The component manufacturing procedure to be assigned to tag (0014,0025).

        This field is optional, but if defined, should be a short text.
        """
        return self[Tag(0x0014, 0x0025)].value

    @property
    def componentManufacturer(self) -> str | None:
        """ The component manufacturer to be assigned to tag (0014,0028).

        This field is optional, but if defined, should be a short text.
        """
        return self[Tag(0x0014,0x0028)].value

    @property
    def componentWelderIDs(self) -> str | None:
        """ The component welder IDs to be assigned to tag (0014,0100).

        This field is optional, but if defined, should be long text.
        """
        return self[Tag(0x0014,0x0100)].value

    @materialName.setter
    def materialName(self, value: str):
        self.add_new(Tag(0x0014,0x2160), "SH", value)

    @materialPropertiesDescription.setter
    def materialPropertiesDescription(self, value: str):
        self.add_new(Tag(0x0014,0x0044), "ST", value)

    @materialNotes.setter
    def materialNotes(self, value: str):
        self.add_new(Tag(0x0014,0x0046), "LT", value)

    @materialThickness.setter
    def materialThickness(self, value: float):
        self.add_new(Tag(0x0014,0x0030), "DS", value)

    @componentShape.setter
    def componentShape(self, value: str):
        self.add_new(Tag(0x0014,0x0050), "CS", value)

    @curvatureType.setter
    def curvatureType(self, value: str):
        self.add_new(Tag(0x0014,0x0052), "CS", value)

    @outerDiameter.setter
    def outerDiameter(self, value: str):
        self.add_new(Tag(0x0014,0x0054), "DS", value)

    @innerDiameter.setter
    def innerDiameter(self, value: float):
        self.add_new(Tag(0x0014,0x0056), "DS", value)

    @componentName.setter
    def componentName(self, value: str):
        self.add_new(Tag(0x0010, 0x0010), "PN", value)

    @materialGrade.setter
    def materialGrade(self, value: str):
        self.add_new(Tag(0x0014,0x0042), "ST", value)

    @componentIDNumber.setter
    def componentIDNumber(self, value: str):
        self.add_new(Tag(0x0010,0x0020), "LO", value)

    @otherComponentIDsSequence.setter
    def otherComponentIDsSequence(self, value:list[otherComponentIDsSequenceElement]):
        self.add_new(Tag(0x0010, 0x1002), "SQ", value)

    @componentIDNumber.setter
    def componentIDNumber(self, value: str):
        self.add_new(Tag(0x0010, 0x0020), "LO", value)

    @componentManufacturingDate.setter
    def componentManufacturingDate(self, value: datetime | None):
        self.add_new(Tag(0x0010, 0x0030), "DA", value)

    @patientSex.setter
    def patientSex(self, value: str | None):
        self.add_new(Tag(0x0010, 0x0040), "CS", value)

    @componentNotes.setter
    def componentNotes(self, value: str | None):
        self.add_new(Tag(0x0010, 0x4000), "LT", value)

    @componentManufacturingProcedure.setter
    def componentManufacturingProcedure(self, value: str | None):
        self.add_new(Tag(0x0014, 0x0025), "ST", value)

    @componentWelderIDs.setter
    def componentWelderIDs(self, value: str | None):
        self.add_new(Tag(0x0014, 0x0100), "ST", value)

    @componentManufacturer.setter
    def componentManufacturer(self, value: str | None):
        self.add_new(Tag(0x0014, 0x0028), "ST", value)
