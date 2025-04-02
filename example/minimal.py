"""
This is the bare minimal diconde file. All required fields are defined, all 
required fields that can be "zero-valued" are set to such, and all non-required
fields are ignored.
""" 
from pydiconde import Diconde
from datetime import datetime, timezone
from pydicom import config

config.INVALID_KEYWORD_BEHAVIOR = "IGNORE"

# create diconde file
diconde_file = Diconde("./minimal.diconde", {})

# fill out the component module
diconde_file.componentName = ""
diconde_file.componentIDNumber = ""
diconde_file.componentManufacturingDate = datetime.now()
diconde_file.patientSex = "O"
diconde_file.materialName = ""

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
diconde_file.modality = "TG"
diconde_file.seriesInstanceUID= "1.2.840.49258.3.152.235.2.13.187636473" 
diconde_file.seriesNumber = 0

# fill out NDE equipment module
diconde_file.softwareVersions = ["DICONDE21"]
diconde_file.manufacturer = ""

# Nothing else is required for a compliant DICONDE file

# save to disk
diconde_file.save_as("./minimal.diconde")
