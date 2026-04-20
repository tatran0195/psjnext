# Title:   Home.ImportMesh.TSVPre()
# Desc:    Convert a old TSV-Pre/Designer file into one or more jtdb files.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportMesh.TSVPre
# ---
import os

VDB_file_path = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    "SampleData/PSJ/PSJ-Utility/VDBSample/sample.vdb")

export_file_path = os.environ["Temp"] + "/TechnoStar/"
Home.ImportMesh.TSVPre(strImportPath=VDB_file_path, strExportPath=export_file_path)  # [hl]
