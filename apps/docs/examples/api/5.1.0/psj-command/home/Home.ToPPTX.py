# Title:   Home.ToPPTX()
# Desc:    Save the display window of Jupiter to an image file in pptx.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ToPPTX
# ---
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy_paste = Home.ToPPTX()

JPT.Debugger(copy_paste)

export_status = Home.ToPPTX(bAutoCapture=True,   # [hl]
                            listAdjust=[10,20,10,20])  # [hl]

JPT.Debugger(copy_paste)
