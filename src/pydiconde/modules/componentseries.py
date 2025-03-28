from pydicom import FileDataset
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag
from datetime import datetime


class RelatedSeriesSequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def studyInstanceUID(self) -> str:
        """ The UID of the study to be assigned to tag (0020,000D).

        The value is expected to be a unique identifier and is required.
        """
        return self[Tag(0x0020,0x000D)].value

    @studyInstanceUID.setter
    def studyInstanceUID(self, value: list[str]):
        self.add_new(Tag(0x0020,0x000D), "UI", value)

    @property
    def seriesInstanceUID(self) -> str:
        """ The UID of the series to be assigned to tag (0020,000E).

        The value is expected to be a unique identifier, and is required.
        """
        return self[Tag(0x0020,0x000E)].value

    @seriesInstanceUID.setter
    def seriesInstanceUID(self, value: list[str]):
        self.add_new(Tag(0x0020,0x000E), "UI", value)

class DICONDEComponentSeries(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def modality(self) -> str:
        """ The modality to be assigned to tag (0008,0060).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0008, 0x0060)].value

    @modality.setter
    def modality(self, value: str):
        self.add_new(Tag(0x0008, 0x0060), "CS", value)

    @property
    def seriesInstanceUID(self) -> str:
        """ The series instance UID to be assigned to tag (0020,000D).

        The value is expected to be a unique identifier. The field is required.
        """
        return self[Tag(0x0010, 0x0010)].value

    @seriesInstanceUID.setter
    def seriesInstanceUID(self, value: str):
        self.add_new(Tag(0x0020, 0x000D), "UI", value)

    @property
    def seriesNumber(self) -> int:
        """ The series date to be assigned to tag (0020,000E).

        The value is expected to be a integer. The field is required.
        """ # validate this
        return self[Tag(0x0020, 0x000E)].value

    @seriesNumber.setter
    def seriesNumber(self, value: int):
        self.add_new(Tag(0x0020, 0x000E), "IS", value)

    @property
    def seriesDate(self) -> datetime:
        """ The series date to be assigned to tag (0008,0021).

        The value is expected to be a date. The field is required.
        """
        return self[Tag(0x0008, 0x0021)].value

    @seriesDate.setter
    def seriesDate(self, value: datetime):
        self.add_new(Tag(0x0008, 0x0021), "DA", value)

    @property
    def seriesTime(self) -> datetime:
        """ The study time to be assigned to tag (0008,0031).

        The value is expected to be a time. The field is required.
        """
        return self[Tag(0x0008, 0x0031)].value

    @seriesTime.setter
    def seriesTime(self, value: datetime):
        self.add_new(Tag(0x0008, 0x0031), "TM", value)

    @property
    def seriesDescription(self) -> str:
        """ The study description to be assigned to tag (0008,103E).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x103E)].value

    @seriesDescription.setter
    def seriesDescription(self, value: str):
        self.add_new(Tag(0x0008,0x103E), "LO", value)

    @property
    def inspectorName(self) -> str:
        """ The inspector name to be assigned to tag (0008,1050).

        The value is expected to be a person name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1050)].value

    @inspectorName.setter
    def inspectorName(self, value: str):
        self.add_new(Tag(0x0008,0x1050), "PN", value)

    @property
    def operatorName(self) -> str:
        """ The operator name to be assigned to tag (0008,1070).

        The value is expected to be a person name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1070)].value

    @operatorName.setter
    def operatorName(self, value: str):
        self.add_new(Tag(0x0008,0x1070), "PN", value)

    @property
    def relatedStudySequence(self) -> list[RelatedSeriesSequenceElement]:
        """ The referenced study sequence to be assigned to tag (0008,1110).

        The value is expected to be a sequence. The field is not required.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1250)].value

    @relatedStudySequence.setter
    def relatedStudySequence(self, value: list[RelatedSeriesSequenceElement]):
        self.add_new(Tag(0x0008,0x1250), "SQ", value)

    @property
    def environmentalConditions(self) -> str:
        """ The environmental conditions to be assigned to tag (0014,1040).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0014, 0x1040)].value

    @environmentalConditions.setter
    def environmentalConditions(self, value: str):
        self.add_new(Tag(0x0014,0x1040), "ST", value)

    @property
    def actualEnvironmentalConditions(self) -> str:
        """ The expiry date to be assigned to tag (0014,1010).

        The value is expected to be a date. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0014,0x1010)].value

    @actualEnvironmentalConditions.setter
    def actualEnvironmentalConditions(self, value: str):
        self.add_new(Tag(0x0014,0x1010), "ST", value)
