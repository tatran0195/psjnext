# Title:   JPT.GetPythonAPILog()
# Desc:    Get the text existing on the Python API window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetPythonAPILog
# ---
# Prepare model to write all text on Python API log
Geometry.Part.Cube(strName="Cube_5", iPartColor=7463537)
Geometry.Part.Cube(strName="Cube_6", iPartColor=7434735)
Geometry.Part.Cube(strName="Cube_7", iPartColor=14903267)
Geometry.Part.Cube(strName="Cube_8", iPartColor=15658599)
Geometry.Part.Cube(strName="Cube_9", iPartColor=7961077)
Geometry.Part.Cube(strName="Cube_10", iPartColor=7829501)
JPT.ViewFitToModel()

# Get the printed text in Python API window
log = JPT.GetPythonAPILog()  # [hl]
JPT.Debugger(log)
