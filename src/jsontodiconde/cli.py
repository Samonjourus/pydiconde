from pydiconde import Diconde, TGImageStorage
from pydicom import FileMetaDataset
from PIL import Image
# from datetime import datetime, timezone
from pydicom import config
from pydicom.dataset import FileMetaDataset
import numpy as np
from pydicom.uid import ExplicitVRLittleEndian, generate_uid, CTImageStorage

from pydiconde.modules.componentseries import Modality
import sys
import json

def main():
    config.INVALID_KEYWORD_BEHAVIOR = "IGNORE" # we're adding non-DICOM fields

    if len(sys.argv) < 2:
        print("missing JSON string")
        return

    data = None
    try:
        data = json.loads(sys.argv[1])
    except:
        try:
            data = json.load(open(sys.argv[1]))
        except:
            print("could not read the meta data as a json string or json file")
            return

    # initialize structures
    diconde_file = Diconde()
    file_meta = FileMetaDataset()

    # file metadata
    file_meta.SourceApplicationEntityTitle = "jsontodiconde"
    file_meta.MediaStorageSOPClassUID = TGImageStorage
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.ImplementationClassUID = generate_uid()
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    diconde_file.SOPInstanceUID = CTImageStorage
    diconde_file.file_meta = file_meta

    # image data
    pixel_scaling = [
        1.0,
        1.0,
        0.04
    ]
    diconde_file.FrameOfReferenceUID = generate_uid()
    image = Image.open(data["in_path"])
    image_array = np.array(image)
    diconde_file.Rows, diconde_file.Columns = image_array.shape
    bits = image_array.itemsize * 8
    diconde_file.BitsAllocated = bits
    diconde_file.BitsStored = bits
    diconde_file.ImageType = ["ORIGINAL", "PRIMARY", "AXIAL"]
    diconde_file.LossyImageCompression = "00"
    diconde_file.HighBit = bits - 1
    diconde_file.PixelData = image_array.tobytes()
    diconde_file.SliceThickness = pixel_scaling[2]
    diconde_file.ImagerPixelSpacing = [
        pixel_scaling[0],
        pixel_scaling[1],
    ]  # [row spacing, column spacing] (mm)
    diconde_file.InstanceNumber = 1  # Does not need to be set, could be left as None
    diconde_file.ImagePositionPatient = [0, 0, pixel_scaling[2]]
    diconde_file.ImageOrientationPatient = [1, 0, 0, 0, 1, 0]
    diconde_file.SamplesPerPixel = 1
    diconde_file.PhotometricInterpretation = "MONOCHROME2"
    diconde_file.PixelSpacing = [
        pixel_scaling[0],
        pixel_scaling[1],
    ]  # [row spacing, column spacing] (mm)
    diconde_file.RescaleIntercept = "0.0"
    diconde_file.RescaleSlope = "1.0"
    diconde_file.PixelRepresentation = 0

    # meta data
    for element in data["metadata"]:
        setattr(diconde_file, element["tag"], element["value"])

    # save
    diconde_file.save_as(data["out_path"], enforce_file_format=True)
    
