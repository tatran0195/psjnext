# Title:   Home.CopyToClipboard()
# Desc:    Save the current display window of Jupiter to the clipboard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.CopyToClipboard
# ---
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy = Home.CopyToClipboard(bWhiteBG=False,  # [hl:start]
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900)  # [hl:end]

JPT.Debugger(copy)

copy = Home.CopyToClipboard(bWhiteBG=False,  # [hl:start]
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900,
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])  # [hl:end]

JPT.Debugger(copy)
