# Title:   Properties.Section.Export()
# Desc:    Export the created 1D section to the XML file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Section.Export
# ---
from os import environ

Properties.Section.AddGeneral(strName="Section_1", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

path = environ["Temp"] + r"\TechnoStar\Section_Export_File.xml"

exporting_status = Properties.Section.Export(strPath = path)  # [hl]

JPT.Debugger(exporting_status)
