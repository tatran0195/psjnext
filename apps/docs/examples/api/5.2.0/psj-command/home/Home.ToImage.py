# Title:   Home.ToImage()
# Desc:    Save the display window of Jupiter to an image file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ToImage
# ---
import re
from os import environ

Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

export_status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                          "/TechnoStar/Cube.png")  # [hl]

JPT.Debugger(export_status)

export_status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl:start]
                                          "/TechnoStar/Cube_minimize.png",
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])  # [hl:end]

JPT.Debugger(export_status)
