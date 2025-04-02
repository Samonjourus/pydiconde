from pydicom import FileDataset
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag
from datetime import datetime


class ReferencedStudySequenceElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def studyInstanceUID(self) -> str:
        """ The UID of the study to be assigned to tag (0020,000D).

        The value is expected to be a unique identifier, but not required.
        """
        return self[Tag(0x0020,0x000D)].value

    @studyInstanceUID.setter
    def studyInstanceUID(self, value: str):
        self.add_new(Tag(0x0020,0x000D), "UI", value)

    @property
    def seriesInstanceUID(self) -> str:
        """ The UID of the series to be assigned to tag (0020,000E).

        The value is expected to be a unique identifier, but not required.
        """
        return self[Tag(0x0020,0x000E)].value

    @seriesInstanceUID.setter
    def seriesInstanceUID(self, value: str):
        self.add_new(Tag(0x0020,0x000E), "UI", value)

class DICONDEComponentStudy(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def studyInstanceUID(self) -> str:
        """ The Study Instance UID to be assigned to tag (0020,000D).

        The value is expected to be a unique identifier. The field is required.
        """
        return self[Tag(0x0010, 0x0010)].value

    @studyInstanceUID.setter
    def studyInstanceUID(self, value: str):
        self.add_new(Tag(0x0020, 0x000D), "PN", value)

    @property
    def studyDate(self) -> datetime:
        """ The study date to be assigned to tag (0008,0020).

        The value is expected to be a date. The field is required.
        """
        return self[Tag(0x0008, 0x0020)].value

    @studyDate.setter
    def studyDate(self, value: datetime):
        self.add_new(Tag(0x0008, 0x0020), "DA", value)

    @property
    def studyTime(self) -> datetime:
        """ The study time to be assigned to tag (0008,0030).

        The value is expected to be a time. The field is required.
        """
        return self[Tag(0x0008, 0x0030)].value

    @studyTime.setter
    def studyTime(self, value: datetime):
        self.add_new(Tag(0x0008, 0x0030), "TM", value)

    @property
    def studyID(self) -> str | None:
        """ The study ID to be assigned to tag (0020,0010).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """
        return self[Tag(0x0020, 0x0010)].value

    @studyID.setter
    def studyID(self, value: str | None):
        self.add_new(Tag(0x0020, 0x0010), "SH", value)

    @property
    def accessionNumber(self) -> str | None:
        """ The accession number to be assigned to tag (0008,0050).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0050)].value

    @accessionNumber.setter
    def accessionNumber(self, value: str | None):
        self.add_new(Tag(0x0008,0x0050), "SH", value)

    @property
    def componentOwnerName(self) -> str | None:
        """ The component owner name to be assigned to tag (0008,0090).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0090)].value

    @componentOwnerName.setter
    def componentOwnerName(self, value: str | None):
        self.add_new(Tag(0x0008,0x0090), "PN", value)

    @property
    def inspectingCompanyName(self) -> str | None:
        """ The inspecting company name to be assigned to tag (0008,1048).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1048)].value

    @inspectingCompanyName.setter
    def inspectingCompanyName(self, value: str | None):
        self.add_new(Tag(0x0008,0x1048), "PN", value)

    @property
    def certifyingInspectorName(self) -> str | None:
        """ The certifying inspector name to be assigned to tag (0008,1060).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1060)].value

    @certifyingInspectorName.setter
    def certifyingInspectorName(self, value: str | None):
        self.add_new(Tag(0x0008,0x1060), "PN", value)

    @property
    def studyDescription(self) -> str | None:
        """ The study description to be assigned to tag (0008,1030).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1030)].value

    @studyDescription.setter
    def studyDescription(self, value: str | None):
        self.add_new(Tag(0x0008,0x1030), "LO", value)

    @property
    def referencedStudySequence(self) -> list[ReferencedStudySequenceElement] | None:
        """ The referenced study sequence to be assigned to tag (0008,1110).

        The value is expected to be a sequence. The field is not required.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1110)].value

    @referencedStudySequence.setter
    def referencedStudySequence(self, value: list[ReferencedStudySequenceElement] | None):
        self.add_new(Tag(0x0008,0x1110), "SQ", value)

    @property
    def examinationNotes(self) -> str | None:
        """ The examination notes to be assigned to tag (0032,4000).

        The value is expected to be a long text. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1060)].value

    @examinationNotes.setter
    def examinationNotes(self, value: str | None):
        self.add_new(Tag(0x0008,0x1060), "LT", value)

    @property
    def expiryDate(self) -> datetime | None:
        """ The expiry date to be assigned to tag (0014,1020).

        The value is expected to be a date. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0014,0x1020)].value

    @expiryDate.setter
    def expiryDate(self, value: datetime | None):
        self.add_new(Tag(0x0014,0x1020), "DA", value)
