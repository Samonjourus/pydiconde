from pydicom.dataset import Dataset
from pydicom.tag import Tag
from datetime import datetime, time
from enum import Enum

class ApprovalStatus(Enum):
    APPROVED = 0
    NOTREVIEWED = 1
    REJECTED = 2
    NODISPOSITION = 3
    RETEST = 4
    REPAIR = 5
    FURTHERREVIEW = 6

class MultipleComponentApprovalElement(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def componentIDNumber(self) -> str:
        """ The component ID number to be assigned to tag (0010,0020).

        The value is expected to be a LO, but not required.
        """
        return self[Tag(0x0010,0x0020)].value

    @componentIDNumber.setter
    def componentIDNumber(self, value: str):
        self.add_new(Tag(0x0010,0x0020), "LO", value)

    @property
    def otherApprovalStatus(self) -> list[str]:
        """ The other approval status to be assigned to tag (0014,0107).

        The value is expected to be a code string, but not required.
        """
        return self[Tag(0x0014,0x0107)].value

    @otherApprovalStatus.setter
    def otherApprovalStatus(self, value: list[str | ApprovalStatus] | None):
        new_value = []

        if value is None:
            self.pop((0x0010,0x1007))
            return

        for val in value:
            if isinstance(val, str):
                if val.upper() in ["APPROVED", "NOTREVIEWED", "REJECTED", "NODISPOSITION", "RETEST", "REPAIR", "FURTHERREVIEW"]:
                    new_value.append(val.upper())
            elif isinstance(val, ApprovalStatus):
                if val == ApprovalStatus.APPROVED:
                    new_value.append("APPROVED")
                if val == ApprovalStatus.NOTREVIEWED:
                    new_value.append("NOTREVIEWED")
                if val == ApprovalStatus.REJECTED:
                    new_value.append("REJECTED")
                if val == ApprovalStatus.NODISPOSITION:
                    new_value.append("NODISPOSITION")
                if val == ApprovalStatus.RETEST:
                    new_value.append("RETEST")
                if val == ApprovalStatus.REPAIR:
                    new_value.append("REPAIR")
                if val == ApprovalStatus.FURTHERREVIEW:
                    new_value.append("FURTHERREVIEW")

        self.add_new(Tag(0x0010,0x1007), "CS", new_value)

    @property
    def otherComponentIDs(self) -> list[str]:
        """ The other component IDs to be assigned to tag (0010,1000).

        The value is expected to be a LO, but not required.
        """
        return self[Tag(0x0010,0x1000)].value

    @otherComponentIDs.setter
    def otherComponentIDs(self, value: list[str]):
        self.add_new(Tag(0x0014,0x0108), "LO", value)

    @property
    def otherSecondaryApprovalStatus(self) -> list[str]:
        """ The other secondary approval status to be assigned to tag (0014,0108).

        The value is expected to be a code string, but not required.
        """
        return self[Tag(0x0014,0x0108)].value

    @otherSecondaryApprovalStatus.setter
    def otherSecondaryApprovalStatus(self, value: list[str | ApprovalStatus] | None):
        new_value = []

        if value is None:
            self.pop((0x0010,0x1008))
            return

        for val in value:
            if isinstance(val, str):
                if val.upper() in ["APPROVED", "NOTREVIEWED", "REJECTED", "NODISPOSITION", "RETEST", "REPAIR", "FURTHERREVIEW"]:
                    new_value.append(val.upper())
            elif isinstance(val, ApprovalStatus):
                if val == ApprovalStatus.APPROVED:
                    new_value.append("APPROVED")
                if val == ApprovalStatus.NOTREVIEWED:
                    new_value.append("NOTREVIEWED")
                if val == ApprovalStatus.REJECTED:
                    new_value.append("REJECTED")
                if val == ApprovalStatus.NODISPOSITION:
                    new_value.append("NODISPOSITION")
                if val == ApprovalStatus.RETEST:
                    new_value.append("RETEST")
                if val == ApprovalStatus.REPAIR:
                    new_value.append("REPAIR")
                if val == ApprovalStatus.FURTHERREVIEW:
                    new_value.append("FURTHERREVIEW")

        self.add_new(Tag(0x0010,0x1008), "CS", new_value)
        
class DICONDENDEApproval(Dataset):
    def __init__(self):
        super().__init__()

    @property
    def approvalStatus(self) -> str:
        """ The approval status to be assigned to tag (300E,0002).

        The value is expected to be a unique identifier. The field is required.
        """
        return self[Tag(0x300E,0x0002)].value

    @approvalStatus.setter
    def approvalStatus(self, value: str | ApprovalStatus | None):
        if isinstance(value, str):
            if value.upper() in ["APPROVED", "NOTREVIEWED", "REJECTED", "NODISPOSITION", "RETEST", "REPAIR", "FURTHERREVIEW"]:
                self.add_new(Tag(0x300E,0x0002), "CS", value.upper())
        elif isinstance(value, ApprovalStatus):
            if value == ApprovalStatus.APPROVED:
                self.add_new(Tag(0x300E,0x0002), "CS", "APPROVED")
            if value == ApprovalStatus.NOTREVIEWED:
                self.add_new(Tag(0x300E,0x0002), "CS", "NOTREVIEWED")
            if value == ApprovalStatus.REJECTED:
                self.add_new(Tag(0x300E,0x0002), "CS", "REJECTED")
            if value == ApprovalStatus.NODISPOSITION:
                self.add_new(Tag(0x300E,0x0002), "CS", "NODISPOSITION")
            if value == ApprovalStatus.RETEST:
                self.add_new(Tag(0x300E,0x0002), "CS", "RETEST")
            if value == ApprovalStatus.REPAIR:
                self.add_new(Tag(0x300E,0x0002), "CS", "REPAIR")
            if value == ApprovalStatus.FURTHERREVIEW:
                self.add_new(Tag(0x300E,0x0002), "CS", "FURTHERREVIEW")
        elif value is None:
            self.pop((0x300E,0x0002))

    @property
    def reviewDate(self) -> datetime:
        """ The review date to be assigned to tag (300E,0004).

        The value is expected to be a unique identifier. The field is required.
        """
        return self[Tag(0x300E,0x0004)].value

    @reviewDate.setter
    def reviewDate(self, value: datetime):
        self.add_new(Tag(0x300E,0x0004), "DA", value)

    @property
    def reviewTime(self) -> time:
        """ The review time to be assigned to tag (300E,0005).

        The value is expected to be a unique identifier. The field is required.
        """
        return self[Tag(0x300E,0x0005)].value

    @reviewTime.setter
    def reviewTime(self, value: time):
        self.add_new(Tag(0x300E,0x0005), "TM", value)


    @property
    def reviewerName(self) -> str:
        """ The reviewer name to be assigned to tag (300E,0008).

        The value is expected to be a person name. The field is required.
        """
        return self[Tag(0x300E,0x0008)].value

    @reviewerName.setter
    def reviewerName(self, value: datetime):
        self.add_new(Tag(0x300E,0x0008), "PN", value)

    @property
    def secondaryApprovalStatus(self) -> str:
        """ The secondary approval status to be assigned to tag (0014,0101).

        The value is expected to be a code string. The field is required.
        """
        return self[Tag(0x0014,0x0101)].value

    @secondaryApprovalStatus.setter
    def secondaryApprovalStatus(self, value: str | ApprovalStatus | None):
        if isinstance(value, str):
            if value.upper() in ["APPROVED", "NOTREVIEWED", "REJECTED", "NODISPOSITION", "RETEST", "REPAIR", "FURTHERREVIEW"]:
                self.add_new(Tag(0x0014,0x0101), "CS", value.upper())
        elif isinstance(value, ApprovalStatus):
            if value == ApprovalStatus.APPROVED:
                self.add_new(Tag(0x0014,0x0101), "CS", "APPROVED")
            if value == ApprovalStatus.NOTREVIEWED:
                self.add_new(Tag(0x0014,0x0101), "CS", "NOTREVIEWED")
            if value == ApprovalStatus.REJECTED:
                self.add_new(Tag(0x0014,0x0101), "CS", "REJECTED")
            if value == ApprovalStatus.NODISPOSITION:
                self.add_new(Tag(0x0014,0x0101), "CS", "NODISPOSITION")
            if value == ApprovalStatus.RETEST:
                self.add_new(Tag(0x0014,0x0101), "CS", "RETEST")
            if value == ApprovalStatus.REPAIR:
                self.add_new(Tag(0x0014,0x0101), "CS", "REPAIR")
            if value == ApprovalStatus.FURTHERREVIEW:
                self.add_new(Tag(0x0014,0x0101), "CS", "FURTHERREVIEW")
        elif value is None:
            self.pop((0x0014,0x0101))

    @property
    def secondaryReviewDate(self) -> datetime:
        """ The secondary review date to be assigned to tag (0014,0102).

        The value is expected to be a date. The field is required.
        """
        return self[Tag(0x0014,0x0102)].value

    @secondaryReviewDate.setter
    def secondaryReviewDate(self, value: str):
        self.add_new(Tag(0x0014,0x0102), "DA", value)

    @property
    def secondaryReviewTime(self) -> time:
        """ The secondary review time to be assigned to tag (0014,0103).

        The value is expected to be a time. The field is required.
        """
        return self[Tag(0x0014,0x0103)].value

    @secondaryReviewTime.setter
    def secondaryReviewTime(self, value: time):
        self.add_new(Tag(0x0014,0x0103), "TM", value)

    @property
    def secondaryReviewerName(self) -> str:
        """ The reviewer name to be assigned to tag (0014,0104).

        The value is expected to be a person name. The field is required.
        """
        return self[Tag(0x0014,0x0104)].value

    @secondaryReviewerName.setter
    def secondaryReviewerName(self, value: datetime):
        self.add_new(Tag(0x0014,0x0104), "PN", value)

    @property
    def repairID(self) -> str:
        """ The repair ID to be assigned to tag (0014,0105).

        The value is expected to be a short text. The field is required.
        """
        return self[Tag(0x0014,0x0105)].value

    @repairID.setter
    def repairID(self, value: str):
        self.add_new(Tag(0x0014,0x0105), "ST", value)

    @property
    def multipleComponentApprovalSequence(self) -> list[MultipleComponentApprovalElement]:
        """ The multiple component approval sequence to be assigned to tag (0014,0106).

        The value is expected to be a sequence of multipleComponentApprovalElements. The field is required.
        """
        return self[Tag(0x0014,0x0106)].value

    @multipleComponentApprovalSequence.setter
    def multipleComponentApprovalSequence(self, value: list[MultipleComponentApprovalElement]):
        self.add_new(Tag(0x0014,0x0106), "SQ", value)
