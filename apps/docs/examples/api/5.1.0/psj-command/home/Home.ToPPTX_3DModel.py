# Title:   Home.ToPPTX_3DModel()
# Desc:    Save the model in the current document as a 3D object (.glb file) and embed it into a .pptx file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ToPPTX_3DModel
# ---
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Home.ToPPTX_3DModel()  # [hl]
