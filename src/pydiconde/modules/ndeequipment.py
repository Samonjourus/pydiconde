from pydicom import FileDataset
from pydicom.dataset import FileMetaDataset
from pydicom.tag import Tag
from datetime import datetime

class DICONDENDEquipment(FileDataset):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)

    @property
    def softwareVersions(self) -> list[str]:
        """ The software versions to be assigned to tag (0018,1020).

        The value is expected to be a long string. The field is required.
        """
        return self[Tag(0x0018, 0x1020)].value

    @softwareVersions.setter
    def softwareVersions(self, value: list[str]):
        self.add_new(Tag(0x0018, 0x1020), "LO", value)

    @property
    def manufacturer(self) -> str | None:
        """ The manufacturer to be assigned to tag (0008,0070).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0070)].value

    @manufacturer.setter
    def manufacturer(self, value: str | None):
        self.add_new(Tag(0x0008,0x0070), "LO", value)

    @property
    def companyName(self) -> str:
        """ The company name to be assigned to tag (0008,0080).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0080)].value

    @companyName.setter
    def companyName(self, value: str):
        self.add_new(Tag(0x0008,0x0080), "LO", value)

    @property
    def companyAddress(self) -> str:
        """ The company address to be assigned to tag (0008,0081).

        The value is expected to be a short string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x0081)].value

    @companyAddress.setter
    def companyAddress(self, value: str):
        self.add_new(Tag(0x0008,0x0081), "ST", value)

    @property
    def stationName(self) -> str:
        """ The station name to be assigned to tag (0008,1010).

        The value is expected to be a short string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1010)].value

    @stationName.setter
    def stationName(self, value: str):
        self.add_new(Tag(0x0008,0x1010), "ST", value)

    @property
    def departmentName(self) -> str:
        """ The department name to be assigned to tag (0008,1040).

        The value is expected to be a short string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1040)].value

    @departmentName.setter
    def departmentName(self, value: str):
        self.add_new(Tag(0x0008,0x1040), "LO", value)

    @property
    def manufacturersModelName(self) -> str:
        """ The manufacturer's model name to be assigned to tag (0008,1090).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0008, 0x1090)].value

    @manufacturersModelName.setter
    def manufacturersModelName(self, value: str):
        self.add_new(Tag(0x0008,0x1090), "LO", value)

    @property
    def deviceSerialNumber(self) -> str:
        """ The device serial number to be assigned to tag (0018,1000).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0018, 0x1000)].value

    @deviceSerialNumber.setter
    def deviceSerialNumber(self, value: str):
        self.add_new(Tag(0x0018,0x1000), "LO", value)

    @property
    def scannerID(self) -> str:
        """ The ID of the scanner to be assigned to tag (0018,1008).

        The value is expected to be a long string. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0018, 0x1008)].value

    @scannerID.setter
    def scannerID(self, value: str):
        self.add_new(Tag(0x0018,0x1008), "LO", value)

    @property
    def spatialResolution(self) -> float:
        """ The spatial resolution of the scanner to be assigned to tag (0018,1050).

        The value is expected to be a decimal. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0018, 0x1050)].value

    @spatialResolution.setter
    def spatialResolution(self, value: str):
        self.add_new(Tag(0x0018,0x1050), "DS", value)

    @property
    def dateOfLastCalibration(self) -> list[datetime]:
        """ The last calibration date to be assigned to tag (0018,1200).

        The value is expected to be a date. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0018, 0x1200)].value

    @dateOfLastCalibration.setter
    def dateOfLastCalibration(self, value: list[datetime]):
        self.add_new(Tag(0x0018,0x1200), "DA", value)

    @property
    def timeOfLastCalibration(self) -> list[datetime]:
        """ The last calibration time to be assigned to tag (0018,1201).

        The value is expected to be a time. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0018, 0x1201)].value

    @timeOfLastCalibration.setter
    def timeOfLastCalibration(self, value: list[datetime]):
        self.add_new(Tag(0x0018,0x1201), "TM", value)

    @property
    def pixelPaddingValue(self) -> int:
        """ The pixel padding value to be assigned to tag (0028,0120).

        The value is expected to be a short. The field is required, but can be zero-valued.
        """ # TODO: verify requirement
        return self[Tag(0x0028, 0x0120)].value

    @pixelPaddingValue.setter
    def pixelPaddingValue(self, value: int):
        # WARN: this property is shady...
        self.add_new(Tag(0x0028,0x0120), "SS", value)

