# Title:   Geometry.Transform.BestFit()
# Desc:    Align the selected parts based on their geometric features.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.BestFit
# ---
# Prepare the model
Geometry.Part.Cube(
    dlLength=[0.003, 0.004, 0.005], 
    iPartColor=7463537)

Geometry.Part.Cube(
    dlLength=[0.004, 0.003, 0.005], 
    strName="Cube_2", iPartColor=15658599)

Geometry.Transform.BestFit(  # [hl:start]
    crlStaticTarget=[Part(1)], 
    crlDynamicTarget=[Part(2)], 
    dError=1e-08, 
    iMaxCycle=400, 
    iAlgorithmsType=0)  # [hl:end]
