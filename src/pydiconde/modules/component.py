from pydicom import FileDataset
from pydicom.dataset import FileMetaDataset

class DICONDEComponent(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def componentName(self):
        """ The componentName to be assigned to tag (0010,0010).

        The value is expected to be a name. The field is required, but can be
        zero-valued.
        """
        return self._componentName

    @componentName.setter
    def componentName(self, value:str):
        self._componentName = value

    @property
    def componentIDNumber(self):
        return self._componentIDNumber

    @componentIDNumber.setter
    def componentIDNumber(self, value):
        self._componentIDNumber = value

    @property
    def otherComponentIDsSequence(self):
        return self._otherComponentIDsSequence

    @otherComponentIDsSequence.setter
    def otherComponentIDsSequence(self, value):
        self._otherComponentIDsSequence = value

    @property
    def otherComponentNames(self):
        return self._otherComponentNames

    @otherComponentNames.setter
    def otherComponentNames(self, value):
        self._otherComponentNames = value

    @property
    def componentManufacturingDate(self):
        return self._componentManufacturingDate

    @componentManufacturingDate.setter
    def componentManufacturingDate(self, value):
        self._componentManufacturingDate = value

    @property
    def patientSex(self):
        return self._patientSex

    @patientSex.setter
    def patientSex(self, value):
        self._patientSex = value

    @property
    def componentNotes(self):
        return self._componentNotes

    @componentNotes.setter
    def componentNotes(self, value):
        self._componentNotes = value

    @property
    def componentManufacturingProcedure(self):
        return self._componentManufacturingProcedure

    @componentManufacturingProcedure.setter
    def componentManufacturingProcedure(self, value):
        self._componentManufacturingProcedure = value

    @property
    def componentManufacturer(self):
        return self._componentManufacturer

    @componentManufacturer.setter
    def componentManufacturer(self, value):
        self._componentManufacturer = value

    @property
    def componentWelderIDs(self):
        return self._componentWelderIDs

    @componentWelderIDs.setter
    def componentWelderIDs(self, value):
        self._componentWelderIDs = value

    @property
    def materialName(self):
        return self._materialName

    @materialName.setter
    def materialName(self, value):
        self._MaterialName = value

    @property
    def materialGrade(self):
        return self._materialGrade

    @materialGrade.setter
    def materialGrade(self, value):
        self._materialGrade = value

    @property
    def materialPropertiesDescription(self):
        return self._materialPropertiesDescription

    @materialPropertiesDescription.setter
    def materialPropertiesDescription(self, value):
        self._materialPropertiesDescription = value

    @property
    def materialNotes(self):
        return self._materialNotes

    @materialNotes.setter
    def materialNotes(self, value):
        self._materialNotes = value

    @property
    def materialThickness(self):
        return self._materialThickness

    @materialThickness.setter
    def materialThickness(self, value):
        self._materialThickness = value

    @property
    def componentShape(self):
        return self._componentShape

    @componentShape.setter
    def componentShape(self, value):
        self._componentShape = value

    @property
    def curvatureType(self):
        return self._curvatureType

    @curvatureType.setter
    def curvatureType(self, value):
        self._curvatureType = value

    @property
    def outerDiameter(self):
        return self._outerDiameter

    @outerDiameter.setter
    def outerDiameter(self, value):
        self._outerDiameter = value

    @property
    def innerDiameter(self):
        return self._innerDiameter

    @innerDiameter.setter
    def innerDiameter(self, value):
        self._innerDiameter = value

