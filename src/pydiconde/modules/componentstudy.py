from pydicom import FileDataset
from pydicom.dataset import FileMetaDataset
from pydicom.tag import Tag
from datetime import datetime

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
    def studyID(self) -> str:
        """ The study ID to be assigned to tag (0020,0010).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """
        return self[Tag(0x0020, 0x0010)].value

    @studyID.setter
    def studyID(self, value: str):
        self.add_new(Tag(0x0020, 0x0010), "SH", value)

    @property
    def accessionNumber(self) -> str:
        """ The accession number to be assigned to tag (0008,0050).

        The value is expected to be a short text. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0050)].value

    @accessionNumber.setter
    def accessionNumber(self, value: str):
        self.add_new(Tag(0x0008,0x0050), "SH", value)

    @property
    def componentOwnerName(self) -> str:
        """ The component owner name to be assigned to tag (0008,0090).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0090)].value

    @componentOwnerName.setter
    def componentOwnerName(self, value: str):
        self.add_new(Tag(0x0008,0x0090), "PN", value)

    @property
    def inspectingCompanyName(self) -> str:
        """ The inspecting company name to be assigned to tag (0008,1048).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1048)].value

    @inspectingCompanyName.setter
    def inspectingCompanyName(self, value: str):
        self.add_new(Tag(0x0008,0x1048), "PN", value)

    @property
    def certifyingInspectorName(self) -> str:
        """ The certifying inspector name to be assigned to tag (0008,1060).

        The value is expected to be a patient name. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1060)].value

    @certifyingInspectorName.setter
    def certifyingInspectorName(self, value: str):
        self.add_new(Tag(0x0008,0x1060), "PN", value)
