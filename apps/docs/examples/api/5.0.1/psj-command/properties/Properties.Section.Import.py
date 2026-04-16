# Title:   Properties.Section.Import()
# Desc:    Import 1D Section from the XML file into the section library
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Section.Import
# ---
from os import environ

Properties.Section.AddGeneral(strName="Section_1", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

path = environ["Temp"] + r"/TechnoStar/Section_Export_File.xml"

Properties.Section.Export(strPath = path)
Properties.Section.Delete(crlSections=[SectionGeneral(1)])

result = Properties.Section.Import(strPath=path)  # [hl]

JPT.Debugger(result)
