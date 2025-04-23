from pydicom.dataset import Dataset
from pydicom.tag import Tag
from enum import Enum

class DataSetMapping(Enum):
    ROW = 0
    COLUMN = 1
    FRAME = 2

class AxisType(Enum):
    SCAN = 0
    INDEX = 1
    GIMBLE = 2
    SWIVEL = 3
    ROTATION = 4
    FIXED = 5

class AxisUnits(Enum):
    COUNTS = 0
    MM = 1
    DEGREES = 2

class CoordinateSystemAxesSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def coordinateSystemAxisDescription(self) -> str:
        """ The description of the axis to be assigned to tag (0014,2206).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0014, 0x2206)].value

    @coordinateSystemAxisDescription.setter
    def coordinateSystemAxisDescription(self, value: str):
        self.add_new(Tag(0x0014, 0x2206), "ST", value)

    @property
    def coordinateSystemDataSetMapping(self) -> str:
        """ The axis's data set mapping to be assigned to tag (0014,2206).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0014, 0x2208)].value

    @coordinateSystemDataSetMapping.setter
    def coordinateSystemDataSetMapping(self, value: str | DataSetMapping | None):
        if isinstance(value, str):
            if value.upper() in ["ROW", "COLUMN", "FRAME"]:
                self.add_new(Tag(0x0014,0x2228), "CS", value.upper())
        elif isinstance(value, DataSetMapping):
            if value == DataSetMapping.ROW:
                self.add_new(Tag(0x0014,0x2228), "CS", "ROW")
            if value == DataSetMapping.COLUMN:
                self.add_new(Tag(0x0014,0x2228), "CS", "COLUMN")
            if value == DataSetMapping.FRAME:
                self.add_new(Tag(0x0014,0x2228), "CS", "FRAME")
        elif value is None:
            self.pop((0x0014,0x2228))

    @property
    def coordinateSystemAxisNumber(self) -> int:
        """ The index of the coordinate system to be assigned to tag (0014,220A).

        The value is expected to be a integer. The field is required.
        """
        return self[Tag(0x0014, 0x220A)].value

    @coordinateSystemAxisNumber.setter
    def coordinateSystemAxisNumber(self, value: int):
        self.add_new(Tag(0x0014, 0x220A), "IS", value)

    @property
    def coordinateSystemAxisType(self) -> str:
        """ The index of the coordinate system to be assigned to tag (0014,220C).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0014, 0x220C)].value

    @coordinateSystemAxisType.setter
    def coordinateSystemAxisType(self, value: str):
        self.add_new(Tag(0x0014, 0x220C), "CS", value)

    @property
    def coordinateSystemAxisUnits(self) -> str:
        """ The index of the coordinate system to be assigned to tag (0014,220E).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0014, 0x220E)].value

    @coordinateSystemAxisUnits.setter
    def coordinateSystemAxisUnits(self, value: str | AxisUnits | None):
        if isinstance(value, str):
            if value.upper() in ["MM", "COUNTS", "DEGREES"]:
                self.add_new(Tag(0x0014,0x220E), "CS", value.upper())
        elif isinstance(value, AxisUnits):
            if value == AxisUnits.MM:
                self.add_new(Tag(0x0014,0x220E), "CS", "MM")
            if value == AxisUnits.COUNTS:
                self.add_new(Tag(0x0014,0x220E), "CS", "COUNTS")
            if value == AxisUnits.DEGREES:
                self.add_new(Tag(0x0014,0x220E), "CS", "DEGREES")
        elif value is None:
            self.pop((0x0014,0x220E))

    @property
    def coordinateSystemAxisValue(self):
        """ The index of the coordinate system to be assigned to tag (0014,2210).

        The value is expected to be a object. The field is required.
        """
        return self[Tag(0x0014, 0x2210)].value

    @coordinateSystemAxisValue.setter
    def coordinateSystemAxisValue(self, value):
        self.add_new(Tag(0x0014, 0x2210), "OB", value)

class CoordinateSystemTransformSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def transformDescription(self) -> str:
        """ The description of the transform to be assigned to tag (0014,2222).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0014, 0x2222)].value

    @transformDescription.setter
    def transformDescription(self, value: str):
        self.add_new(Tag(0x0014, 0x2222), "ST", value)

    @property
    def transformNumberOfAxes(self) -> int:
        """ The number of transform axis to be assigned to tag (0014,2224).

        The value is expected to be an integer. The field is required.
        """
        return self[Tag(0x0014, 0x2224)].value

    @transformNumberOfAxes.setter
    def transformNumberOfAxes(self, value: str):
        self.add_new(Tag(0x0014, 0x2224), "ST", value)

    @property
    def transformOrderOfAxes(self) -> list[int]:
        """ The order of transform axis to be assigned to tag (0014,2226).

        The value is expected to be an integer. The field is required.
        """
        return self[Tag(0x0014, 0x2226)].value

    @transformOrderOfAxes.setter
    def transformOrderOfAxes(self, value: str):
        self.add_new(Tag(0x0014, 0x2226), "ST", value)

    @property
    def transformedAxisUnits(self) -> list[int]:
        """ The order of transform axis to be assigned to tag (0014,2228).

        The value is expected to be an code string. The field is required.
        """
        return self[Tag(0x0014, 0x2228)].value

    @transformedAxisUnits.setter
    def transformedAxisUnits(self, value: str | AxisUnits | None):
        if isinstance(value, str):
            if value.upper() in ["MM", "COUNTS", "DEGREES"]:
                self.add_new(Tag(0x0014,0x2228), "CS", value.upper())
        elif isinstance(value, AxisUnits):
            if value == AxisUnits.MM:
                self.add_new(Tag(0x0014,0x2228), "CS", "MM")
            if value == AxisUnits.COUNTS:
                self.add_new(Tag(0x0014,0x2228), "CS", "COUNTS")
            if value == AxisUnits.DEGREES:
                self.add_new(Tag(0x0014,0x2228), "CS", "DEGREES")
        elif value is None:
            self.pop((0x0014,0x2228))

    @property
    def coordinateSystemRotationAndScaleMatrix(self) -> list[int]:
        """ The order of transform axis to be assigned to tag (0014,222A).

        The value is expected to be an datatset. The field is required.
        """
        return self[Tag(0x0014, 0x222A)].value

    @coordinateSystemRotationAndScaleMatrix.setter
    def coordinateSystemRotationAndScaleMatrix(self, value: str):
        self.add_new(Tag(0x0014, 0x222A), "DS", value)

    @property
    def coordinateSystemTranslationMatrix(self) -> list[int]:
        """ The order of transform axis to be assigned to tag (0014,222C).

        The value is expected to be an dataset. The field is required.
        """
        return self[Tag(0x0014, 0x222C)].value

    @coordinateSystemTranslationMatrix.setter
    def coordinateSystemTranslationMatrix(self, value: str):
        self.add_new(Tag(0x0014, 0x222C), "DS", value)


class DICONDENDEGeometry(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def coordinateSystemNumberOfAxis(self) -> int:
        """ The count of axes in the coordinate system to be assigned to tag (0014,2202).

        The value is expected to be a integer. The field is required.
        """
        return self[Tag(0x0014, 0x2202)].value

    @coordinateSystemNumberOfAxis.setter
    def coordinateSystemNumberOfAxis(self, value: int):
        self.add_new(Tag(0x0014, 0x2202), "IS", value)

    @property
    def coordinateSystemAxesSequence(self) -> int:
        """ The sequence of coordinate system axes to be assigned to tag (0014,2204).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0014, 0x2204)].value

    @coordinateSystemAxesSequence.setter
    def coordinateSystemAxesSequence(self, value: int):
        self.add_new(Tag(0x0014, 0x2204), "SQ", value)

    @property
    def coordinateSystemTransformSequence(self) -> int:
        """ The sequence of coordinate system axes transforms to be assigned to tag (0014,2220).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0014, 0x2220)].value

    @coordinateSystemTransformSequence.setter
    def coordinateSystemTransformSequence(self, value: int):
        self.add_new(Tag(0x0014, 0x2220), "SQ", value)
