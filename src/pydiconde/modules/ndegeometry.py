from pydicom import Dataset, FileDataset
from pydicom.dataset import FileMetaDataset
from pydicom.tag import Tag

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
    def coordinateSystemDataSetMapping(self, value: str):
        self.add_new(Tag(0x0014, 0x2208), "CS", value)

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
    def coordinateSystemAxisUnits(self, value: str):
        self.add_new(Tag(0x0014, 0x220E), "CS", value)

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
    def transformedAxisUnits(self, value: str):
        self.add_new(Tag(0x0014, 0x2228), "CS", value)

    @property
    def coordinateSystemRotationAndScaleMatrix(self) -> list[int]:
        """ The order of transform axis to be assigned to tag (0014,222A).

        The value is expected to be an code string. The field is required.
        """
        return self[Tag(0x0014, 0x222A)].value

    @transformedAxisUnits.setter
    def transformedAxisUnits(self, value: str):
        self.add_new(Tag(0x0014, 0x222A), "CS", value)

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

    @coordinateSystemAxesSequence.setter
    def coordinateSystemTransformSequence(self, value: int):
        self.add_new(Tag(0x0014, 0x2220), "SQ", value)
