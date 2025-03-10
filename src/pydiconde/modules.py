# from typing import List, Tuple
from pydicom import FileDataset

def set_component_welder_ids(file: FileDataset, id: str) -> FileDataset:
    """
    Sets the component welder ids according to ASTM E2339-21 table 2.
    This id can specify the person or machine.

    :param file: The file to set the version on.
    :param notes: Noteworthy comments about the component.
    :return: The modified DICONDE file data.
    """
    file[(0x0014, 0x0100)].value = id
    return file

def set_material_notes(file: FileDataset, notes: str) -> FileDataset:
    """
    Sets the material notes according to ASTM E2339-21 table 2.

    :param file: The file to set the version on.
    :param notes: Noteworthy comments about the material.
    :return: The modified DICONDE file data.
    """
    file[(0x0014, 0x0046)].value = notes
    return file

def set_component_notes(file: FileDataset, notes: str) -> FileDataset:
    """
    Sets the component notes according to ASTM E2339-21 table 2.

    :param file: The file to set the version on.
    :param notes: Noteworthy comments about the component.
    :return: The modified DICONDE file data.
    """
    file[(0x0010, 0x4000)].value = notes
    return file

def prepare_file(file: FileDataset) -> FileDataset:
    """
    Helper function to set tags that require minimal or no input.

    The function will:
    - set the file version
    - set Patient Sex to O.

    :param file: The file to set the version on.
    :return: The modified DICONDE file data.
    """

    file = specify_version(file)
    file[(0x0010, 0x0040)].value = "O"

    return file

def set_additional_part_id_names(file: FileDataset, entries:list[tuple[str, str]]) -> FileDataset:
    """
    Sets the additional names and ids accoridng to ASTM E2339-21 table 2.

    :param file: The file to set the version on.
    :param entries: [TODO:description]
    :return: The modified DICONDE file data.
    """
    names = []
    ids = []
    for entry in entries:
        names.append(entry[0])
        ids.append(entry[1])

    file[(0x0010, 0x1001)].value =  ids
    file[(0x0010, 0x1002)].value = names

    return file

def specify_version(file: FileDataset) -> FileDataset:
    """
    Sets the version number according to ASTM E2339-21 section 7.2.5

     This stores the DICONDE version number and the version of the
     library used to generate the file. The DICONDE version should
     always be first element.

    :param file: The file to set the version on.
    :return: The modified DICONDE file data.
    """
    file[(0x0018, 0x0020)].value = ["DICONDE21", "dicondeCDD_0.1.0"] 
    return file

def set_component_name(file: FileDataset, name: str) -> FileDataset:
    """
    Sets the component name according to table 2 record 1 of ASTM E2339.

    :param file: The file to set the component name on.
    :param name: The component name.
    :return: The modified DICONDE file data.
    """
    file[(0x0010, 0x0010)].value = name
    return file

def set_project(module: CDDProject, file: FileDataset) -> FileDataset:
    return file

def set_build(module: CDDBuild, file: FileDataset) -> FileDataset:
    file[(0x0014, 0x0028)].value = module.organization_id
    return file

def set_part_design(module: CDDBuiltPart, file: FileDataset) -> FileDataset:
    return file

def set_built_part(module: CDDBuiltPart, file: FileDataset) -> FileDataset:
    """
    Adds information from the CDD's built part module to the DICONDE file.

    :param module: CDD built part module information.
    :param file: The file with contents to be updated.
    :return: a modified file containing the built part information.
    """
    file.PatientID = module.built_part_id
    file[(0x0014, 0x0025)].value = module.built_part_process_sequence
    return file

def set_am_system(module: CDDAMSystem, file: FileDataset) -> FileDataset:
    return file

def set_material(module: CDDMaterial, file: FileDataset) -> FileDataset:
    file[(0x0010, 0x2160)].value = module.material_name
    file[(0x0014, 0x0042)].value = module.material_grade
    file[(0x0014, 0x0044)].value = module.material_product_specification
    return file

def set_process_control(module: CDDProcessControl, file: FileDataset) -> FileDataset:
    return file

def set_process_data(module: CDDProcessData, file: FileDataset) -> FileDataset:
    if module.am_process_end_time is not None:
        file[(0x0010, 0x0030)].value =  module.am_process_end_time.strftime("%Y%m%d")
    return file
