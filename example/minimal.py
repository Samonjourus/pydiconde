"""
This is the bare minimal diconde file. All required fields are defined, all 
required fields that can be "zero-valued" are set to such, and all non-required
fields are ignored.
""" 
from pydiconde import Diconde, TGImageStorage
from datetime import datetime, timezone
from pydicom import config
from pydicom.dataset import FileMetaDataset
import numpy as np
from pydicom.uid import ExplicitVRLittleEndian, generate_uid, CTImageStorage

from pydiconde.modules.componentseries import Modality

config.INVALID_KEYWORD_BEHAVIOR = "IGNORE" # we're adding non-DICOM fields
image_data = np.uint16(np.random.rand(128, 128) * 65535) # sample image data

# Optional: use Diconde naming
Diconde.use_diconde_names()

# create diconde file
diconde_file = Diconde()

# necessary file meta data information
file_meta = FileMetaDataset()
file_meta.SourceApplicationEntityTitle = "Ex Pydi script"
file_meta.MediaStorageSOPClassUID = TGImageStorage
file_meta.MediaStorageSOPInstanceUID = generate_uid()
file_meta.ImplementationClassUID = generate_uid()
file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

diconde_file.file_meta = file_meta

# fill out the component module
diconde_file.componentName = ""
diconde_file.componentIDNumber = ""
diconde_file.componentManufacturingDate = datetime.now()
diconde_file.patientSex = "O"
diconde_file.materialName = ""
diconde_file.SOPInstanceUID = CTImageStorage

# fill out component study module
diconde_file.studyInstanceUID = "1.2.840.49258.3.152.235.2.12.187636473" 
diconde_file.studyDate = datetime.now()
diconde_file.studyTime = datetime.now().time()
diconde_file.studyID = ""
diconde_file.accessionNumber = ""
diconde_file.componentOwnerName = ""
diconde_file.inspectingCompanyName = ""
diconde_file.certifyingInspectorName = ""
diconde_file.studyDescription = ""
diconde_file.examinationNotes = ""
diconde_file.expiryDate = datetime(1970, 1, 1, tzinfo=timezone.utc)

# fill out component series module
diconde_file.modality = Modality.THERMOGRAPHY
diconde_file.seriesInstanceUID= "1.2.840.49258.3.152.235.2.13.187636473" 
diconde_file.seriesNumber = 0

# fill out NDE equipment module
diconde_file.softwareVersions = ["DICONDE21"]
diconde_file.manufacturer = ""

# Nothing else is required for a compliant DICONDE file
# save to disk
diconde_file.save_as("./minimal.dcm", enforce_file_format=True)
print(diconde_file)
