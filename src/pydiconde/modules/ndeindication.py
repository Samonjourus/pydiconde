from pydicom import Dataset
from pydicom.tag import Tag
from enum import Enum

class IndicationROIGeometricTypeEnum(Enum):
    POINT = 0
    MULITPOINT = 1
    POLYLINE = 2
    CIRCLE = 3
    ELLIPSE = 3

class PropertyUnitsCodeSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def codeValue(self) -> str:
        """ The code value to be assigned to tag (0008,0100).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0008,0x0100)].value

    @codeValue.setter
    def codeValue(self, value: str):
        self.add_new(Tag(0x0008,0x0100), "SH", value)

    @property
    def codeSchemeDesignator(self) -> str:
        """ The code scheme designator to be assigned to tag (0008,0102).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0008,0x0102)].value

    @codeSchemeDesignator.setter
    def codeSchemeDesignator(self, value: str):
        self.add_new(Tag(0x0008,0x0102), "SH", value)

    @property
    def codeSchemeVersion(self) -> str:
        """ The code scheme version to be assigned to tag (0008,0103).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0008,0x0103)].value

    @codeSchemeVersion.setter
    def codeSchemeVersion(self, value: str):
        self.add_new(Tag(0x0008,0x0103), "SH", value)

    @property
    def codeMeaning(self) -> str:
        """ The code meaning to be assigned to tag (0008,0104).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0008,0x0104)].value

    @codeMeaning.setter
    def codeMeaning(self, value: str):
        self.add_new(Tag(0x0008,0x0104), "LO", value)

class IndicationPhysicalPropertySequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def propertyLabel(self) -> str:
        """ The property label to be assigned to tag (0014,2032).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0014,0x2032)].value

    @propertyLabel.setter
    def propertyLabel(self, value: str):
        self.add_new(Tag(0x0014,0x2032), "SH", value)

    @property
    def propertyValue(self) -> str:
        """ The property value to be assigned to tag (0040,A30A).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0040,0xA30A)].value

    @propertyValue.setter
    def propertyValue(self, value: str):
        self.add_new(Tag(0x0040,0xA30A), "SH", value)

    @property
    def propertyUnitsCodeSequence(self) -> list[PropertyUnitsCodeSequenceElement]:
        """ The property value to be assigned to tag (0040,08EA).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0040,0x08EA)].value

    @propertyUnitsCodeSequence.setter
    def propertyUnitsCodeSequence(self, value: list[PropertyUnitsCodeSequenceElement]):
        self.add_new(Tag(0x0014,0x08EA), "SQ", value)

class IndicationTypeEnum(Enum):
    VOID = 0
    CRACK = 1
    POROSITY = 2
    INCLUSION = 3

class IndicationROISequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def indicationROIGeometricType(self) -> IndicationROIGeometricTypeEnum:
        """ The indication region of interest geometric type to be assigned to tag (0070,0023).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0070, 0x0023)].value

    @indicationROIGeometricType.setter
    def indicationROIGeometricType(self, value: IndicationROIGeometricTypeEnum):
        self.add_new(Tag(0x0070, 0x0023), "CS", value)

    @property
    def indicationROIValueType(self) -> str:
        """ The indication region of interest value type to be assigned to tag (0040,A040).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0040, 0xA040)].value

    @indicationROIValueType.setter
    def indicationROIValueType(self, value: list[IndicationPhysicalPropertySequenceElement]):
        self.add_new(Tag(0x0040, 0xA040), "CS", value)

    @property
    def numberOfROIContourPoints(self) -> int:
        """ The number of region of interest contour points to be assigned to tag (0070,0021).

        The value is expected to be an unsigned short. The field is required.
        """
        return self[Tag(0x0070, 0x0021)].value

    @numberOfROIContourPoints.setter
    def numberOfROIContourPoints(self, value: int):
        self.add_new(Tag(0x0070, 0x0021), "US", value)

    @property
    def indicationROIContourData(self) -> Dataset:
        """ The indication region of interest contour data to be assigned to tag (0070,0022).

        The value is expected to be a dataset. The field is required.
        """
        return self[Tag(0x0070, 0x0022)].value

    @indicationROIContourData.setter
    def indicationROIContourData(self, value: Dataset):
        self.add_new(Tag(0x0070, 0x0022), "DS", value)

class IndicationSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def SOPInstanceUID(self) -> str:
        """ The SOP instance UID to be assigned to tag (0008,0018).

        The value is expected to be a UID. The field is required.
        """
        return self[Tag(0x0008, 0x0018)].value

    @SOPInstanceUID.setter
    def SOPInstanceUID(self, value: int):
        self.add_new(Tag(0x0008, 0x0018), "UI", value)

    @property
    def indicationNumber(self) -> int:
        """ The indication number to be assigned to tag (0014,2014).

        The value is expected to be an integer. The field is required.
        """
        return self[Tag(0x0014, 0x2014)].value

    @indicationNumber.setter
    def indicationNumber(self, value: int):
        self.add_new(Tag(0x0014, 0x2014), "IS", value)

    @property
    def indicationLabel(self) -> str:
        """ The indication label to be assigned to tag (0014,2016).

        The value is expected to be an short string. The field is required.
        """
        return self[Tag(0x0014, 0x2016)].value

    @indicationLabel.setter
    def indicationLabel(self, value: str):
        self.add_new(Tag(0x0014, 0x2014), "SH", value)

    @property
    def indicationDescription(self) -> str:
        """ The indication desccription to be assigned to tag (0014,2018).

        The value is expected to be an short text. The field is required.
        """
        return self[Tag(0x0014, 0x2018)].value

    @indicationDescription.setter
    def indicationDescription(self, value: str):
        self.add_new(Tag(0x0014, 0x2018), "ST", value)

    @property
    def indicationType(self) -> IndicationTypeEnum:
        """ The indication label to be assigned to tag (0014,2016).

        The value is expected to be an IndicationTypeEnum. The field is required.
        """
        return self[Tag(0x0014, 0x201A)].value

    @indicationType.setter
    def indicationType(self, value: IndicationTypeEnum):
        self.add_new(Tag(0x0014, 0x201A), "CS", value)

    @property
    def indicationDisposition(self) -> str:
        """ The indication disposition to be assigned to tag (0014,201C).

        The value is expected to be an code string. The field is required.
        """
        return self[Tag(0x0014, 0x201C)].value

    @indicationDisposition.setter
    def indicationDisposition(self, value: str):
        self.add_new(Tag(0x0014, 0x201C), "CS", value)

    @property
    def indicationPhysicalPropertySequence(self) -> list[IndicationPhysicalPropertySequenceElement]:
        """ The indication physical property sequence to be assigned to tag (0014,2030).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0014, 0x2030)].value

    @indicationLabel.setter
    def indicationLabel(self, value: list[IndicationPhysicalPropertySequenceElement]):
        self.add_new(Tag(0x0014, 0x2030), "SQ", value)

    @property
    def indicationROIGeometricType(self) -> IndicationROIGeometricTypeEnum:
        """ The indication region of interest geometric type to be assigned to tag (0070,0023).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0070, 0x0023)].value

    @indicationROIGeometricType.setter
    def indicationROIGeometricType(self, value: IndicationROIGeometricTypeEnum):
        self.add_new(Tag(0x0070, 0x0023), "CS", value)

    @property
    def indicationROIValueType(self) -> str:
        """ The indication region of interest value type to be assigned to tag (0040,A040).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0040, 0xA040)].value

    @indicationROIValueType.setter
    def indicationROIValueType(self, value: list[IndicationROIValueTypeEnum | str] | None):
        new_value = []

        if value is None:
            self.pop((0x0040,0xA040))
            return

        for val in value:
            if isinstance(val, str):
                if val.upper() in ["SCOORD3D", "SCOORD"]:
                    new_value.append(val.upper())
            elif isinstance(val, IndicationROIValueTypeEnum):
                if val == IndicationROIValueTypeEnum.SCOORD:
                    new_value.append("SCOORD")
                if val == IndicationROIValueTypeEnum.SCOORD3D:
                    new_value.append("SCOORD3D")

        self.add_new(Tag(0x0040,0xA040), "CS", new_value)

    @property
    def numberOfROIContourPoints(self) -> int:
        """ The number of region of interest contour points to be assigned to tag (0070,0021).

        The value is expected to be an unsigned short. The field is required.
        """
        return self[Tag(0x0070, 0x0021)].value

    @numberOfROIContourPoints.setter
    def numberOfROIContourPoints(self, value: int):
        self.add_new(Tag(0x0070, 0x0021), "US", value)

    @property
    def indicationROIContourData(self) -> Dataset:
        """ The indication region of interest contour data to be assigned to tag (0070,0022).

        The value is expected to be a dataset. The field is required.
        """
        return self[Tag(0x0070, 0x0022)].value

    @indicationROIContourData.setter
    def indicationROIContourData(self, value: Dataset):
        self.add_new(Tag(0x0070, 0x0022), "DS", value)

    @property
    def indicationROISequence(self) -> list[IndicationROISequenceElement]:
        """ The indication region of interest sequence to be assigned to tag (0014,201E).

        The value is expected to be a Sequence. The field is required.
        """
        return self[Tag(0x0014, 0x201E)].value

    @indicationROIContourData.setter
    def indicationROIContourData(self, value: list[IndicationROISequenceElement]):
        self.add_new(Tag(0x0014, 0x201E), "SQ", value)

class EvaluatorSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def evaluatorNumber(self) -> int:
        """ The elevator number to be assigned to tag (0014,2004).

        The value is expected to be an int. The field is required.
        """
        return self[Tag(0x0014, 0x2004)].value

    @evaluatorNumber.setter
    def evaluatorNumber(self, value: int):
        self.add_new(Tag(0x0014, 0x2004), "IS", value)

    @property
    def evaluatorName(self) -> str:
        """ The elevator name to be assigned to tag (0014,2006).

        The value is expected to be a person name. The field is required.
        """
        return self[Tag(0x0014, 0x2006)].value

    @evaluatorName.setter
    def evaluatorName(self, value: str):
        self.add_new(Tag(0x0014, 0x2006), "PN", value)

    @property
    def evaluationAttempt(self) -> int:
        """ The elevation attempt to be assigned to tag (0014,2008).

        The value is expected to be an integer. The field is required.
        """
        return self[Tag(0x0014, 0x2008)].value

    @evaluatorName.setter
    def evaluatorName(self, value: int):
        self.add_new(Tag(0x0014, 0x2008), "IS", value)

    @property
    def indicationSequence(self) -> list[IndicationSequenceElement]:
        """ The indication sequence to be assigned to tag (0014,2012).

        The value is expected to be an sequence. The field is required.
        """
        return self[Tag(0x0014, 0x2012)].value

    @indicationSequence.setter
    def indicationSequence(self, value: list[IndicationSequenceElement]):
        self.add_new(Tag(0x0014, 0x2012), "SQ", value)

class DICONDENDEIndication(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def evaluatorSequence(self) -> list[EvaluatorSequenceElement]:
        """ The elevator sequence to be assigned to tag (0014,2002).

        The value is expected to be a long string. The field is required.
        """
        return self[Tag(0x0014, 0x2002)].value

    @evaluatorSequence.setter
    def evaluatorSequence(self, value: list[EvaluatorSequenceElement]):
        self.add_new(Tag(0x0014, 0x2002), "SQ", value)
