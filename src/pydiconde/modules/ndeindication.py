from pydicom import Dataset, FileDataset
from pydicom.dataset import FileMetaDataset
from pydicom.tag import Tag

class DICONDEIndication(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def evaluatorSequence(self) -> list[EvaluatorSequenceElement]:
        """ The elevator sequence to be assigned to tag (0014,2002).

        The value is expected to be a long string. The field is required.
        """
        return self[Tag(0x0018, 0x1020)].value

    @evaluatorSequence.setter
    def evaluatorSequence(self, value: list[EvaluatorSequenceElement]):
        self.add_new(Tag(0x0014, 0x2002), "SQ", value)
