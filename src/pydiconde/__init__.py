from .modules.component import DICONDEComponent
from .modules.componentseries import DICONDEComponentSeries
from .modules.componentstudy import DICONDEComponentStudy
from .modules.ndeequipment import DICONDENDEquipment
from .modules.ndegeometry import DICONDENDEGeometry
from .modules.ndeindication import DICONDENDEIndication

from pydicom.dataset import FileMetaDataset

class Diconde(DICONDEComponent, DICONDEComponentSeries, DICONDEComponentStudy, DICONDENDEquipment, DICONDENDEGeometry, DICONDENDEIndication):
    def __init__(self, file_path, object, file_meta=FileMetaDataset()):
        super().__init__(file_path, object, file_meta=file_meta)
