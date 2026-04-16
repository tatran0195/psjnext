# Title:   Home.ToImage()
# Desc:    Save the display window of Jupiter to an image file
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.ToImage
# ---
import re
from os import environ

Geometry.Part.Cube()
JPT.ViewFitToModel()

export_status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \  # [hl]
                                          "/TechnoStar/Cube.png")  # [hl]

JPT.Debugger(export_status)
