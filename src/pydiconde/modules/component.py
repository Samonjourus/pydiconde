from pydicom import FileDataset
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag

class DICONDEComponent(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def componentName(self):
        """ The component name to be assigned to tag (0010,0010).

        The value is expected to be a name. The field is required, but can be
        zero-valued.
        """
        return self[Tag(0x0010, 0x0010)].value

    @property
    def componentIDNumber(self):
        """ The component ID to be assigned to tag (0010,0020).

        The value is expected to be an ID. The field is required, but can be
        zero-valued.
        """
        return self[Tag(0x0010, 0x0020)].value

    @property
    def otherComponentIDsSequence(self):
        return self._otherComponentIDsSequence

    @property
    def materialName(self):
        return self._materialName

    @property
    def materialGrade(self):
        return self._materialGrade

    @property
    def materialPropertiesDescription(self):
        return self._materialPropertiesDescription

    @property
    def materialNotes(self):
        return self._materialNotes

    @property
    def materialThickness(self):
        return self._materialThickness

    @property
    def componentShape(self):
        return self._componentShape

    @property
    def curvatureType(self):
        return self._curvatureType

    @property
    def outerDiameter(self):
        return self._outerDiameter

    @property
    def innerDiameter(self):
        return self._innerDiameter

    @materialName.setter
    def materialName(self, value):
        self._MaterialName = value

    @materialPropertiesDescription.setter
    def materialPropertiesDescription(self, value):
        self._materialPropertiesDescription = value

    @materialNotes.setter
    def materialNotes(self, value):
        self._materialNotes = value

    @materialThickness.setter
    def materialThickness(self, value):
        self._materialThickness = value

    @componentShape.setter
    def componentShape(self, value):
        self._componentShape = value

    @curvatureType.setter
    def curvatureType(self, value):
        self._curvatureType = value

    @outerDiameter.setter
    def outerDiameter(self, value):
        self._outerDiameter = value

    @innerDiameter.setter
    def innerDiameter(self, value):
        self._innerDiameter = value

    @componentName.setter
    def componentName(self, value:str):
        self.add_new(Tag(0x0010, 0x0010), "PN", value)

    @materialGrade.setter
    def materialGrade(self, value):
        self._materialGrade = value

    @componentIDNumber.setter
    def componentIDNumber(self, value):
        self._componentIDNumber = value

    @otherComponentIDsSequence.setter
    def otherComponentIDsSequence(self, value):
        self._otherComponentIDsSequence = value

    @componentIDNumber.setter
    def componentIDNumber(self, value):
        self.add_new(Tag(0x0010, 0x0020), "LO", value)


class otherComponentIDsSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def otherComponentNames(self):
        return self._otherComponentNames

    @property
    def componentManufacturingDate(self):
        return self._componentManufacturingDate

    @property
    def patientSex(self):
        return self._patientSex

    @property
    def componentNotes(self):
        return self._componentNotes

    @property
    def componentManufacturingProcedure(self):
        return self._componentManufacturingProcedure

    @property
    def componentManufacturer(self):
        return self._componentManufacturer

    @property
    def componentWelderIDs(self):
        return self._componentWelderIDs

    @otherComponentNames.setter
    def otherComponentNames(self, value):
        self._otherComponentNames = value

    @componentManufacturingDate.setter
    def componentManufacturingDate(self, value):
        self._componentManufacturingDate = value

    @patientSex.setter
    def patientSex(self, value):
        self._patientSex = value

    @componentNotes.setter
    def componentNotes(self, value):
        self._componentNotes = value

    @componentManufacturingProcedure.setter
    def componentManufacturingProcedure(self, value):
        self._componentManufacturingProcedure = value

    @componentWelderIDs.setter
    def componentWelderIDs(self, value):
        self._componentWelderIDs = value

    @componentManufacturer.setter
    def componentManufacturer(self, value):
        self._componentManufacturer = value

