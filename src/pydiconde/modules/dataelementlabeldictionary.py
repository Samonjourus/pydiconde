from pydicom import FileDataset
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag

class DataElementLabelItemElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def dataElement(self) -> tuple[int, int]:
        """ The data element to be assigned to tag (0014,0202).

        The value is expected to be a hex identifier, but not required.
        """
        return self[Tag(0x0014,0x0202)].value

    @dataElement.setter
    def dataElement(self, value: tuple[int, int]):
        self.add_new(Tag(0x0014,0x0202), "AT", value)

    @property
    def dataElementName(self) -> str:
        """ The data element name to be assigned to tag (0014,0203).

        The value is expected to be a long text, but not required.
        """
        return self[Tag(0x0014,0x0203)].value

    @dataElementName.setter
    def dataElementName(self, value: str):
        self.add_new(Tag(0x0014,0x0203), "LO", value)

    @property
    def dataElementDescription(self) -> str:
        """ The data element description to be assigned to tag (0014,0204).

        The value is expected to be a long text, but not required.
        """
        return self[Tag(0x0014,0x0204)].value

    @dataElementName.setter
    def dataElementName(self, value: str):
        self.add_new(Tag(0x0014,0x0204), "LO", value)

    @property
    def dataElementConditionality(self) -> str:
        """ The data element conditionality to be assigned to tag (0014,0205).

        The value is expected to be a long text, but not required.
        """
        return self[Tag(0x0014,0x0205)].value

    @dataElementConditionality.setter
    def dataElementConditionality(self, value: str):
        self.add_new(Tag(0x0014,0x0205), "LO", value)

    @property
    def dataElementMinimumCharacters(self) -> int:
        """ The data element minimum characters to be assigned to tag (0014,0206).

        The value is expected to be an integer, but not required.
        """
        return self[Tag(0x0014,0x0206)].value

    @dataElementMinimumCharacters.setter
    def dataElementMinimumCharacters(self, value: int):
        self.add_new(Tag(0x0014,0x0206), "IS", value)

    @property
    def dataElementMaximumCharacters(self) -> int:
        """ The data element maximum characters to be assigned to tag (0014,0207).

        The value is expected to be an integer, but not required.
        """
        return self[Tag(0x0014,0x0207)].value

    @dataElementMaximumCharacters.setter
    def dataElementMaximumCharacters(self, value: int):
        self.add_new(Tag(0x0014,0x0207), "IS", value)

class DataElementLabelElement(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def dataElementLabelItemSequence(self) -> list[DataElementLabelItemElement]:
        """ The data element label item sequence to be assigned to tag (0014,0201).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0014, 0x0201)].value

    @dataElementLabelItemSequence.setter
    def dataElementLabelItemSequence(self, value: list[DataElementLabelItemElement]):
        self.add_new(Tag(0x0014, 0x0201), "SQ", value)

class DataElementLabelSequence(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def dataElementLabelSequence(self) -> list[DataElementLabelElement]:
        """ The data element label sequence to be assigned to tag (0014,0200).

        The value is expected to be a sequence. The field is required.
        """
        return self[Tag(0x0014, 0x0200)].value

    @dataElementLabelSequence.setter
    def dataElementLabelSequence(self, value: list[DataElementLabelElement]):
        self.add_new(Tag(0x0014, 0x0200), "SQ", value)
