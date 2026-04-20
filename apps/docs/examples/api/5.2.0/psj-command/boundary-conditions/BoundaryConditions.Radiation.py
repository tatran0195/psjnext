# Title:   BoundaryConditions.Radiation()
# Desc:    Create a radiation applied to the selected Face or Element or Group. User inputs the radiation value and it will apply the radiation to the selected items
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Radiation
# ---
Geometry.Part.Cube()
BoundaryConditions.Radiation(  # [hl:start]
    strName="Radiation_1", 
    radiation=LBC_RADIATION_DATA(
        dAmbientTemp=373.15, 
        crTimeDependAm=None, 
        dEmissivity=0.5, 
        crTimeDependEm=None, 
        crTempDependEm=None), 
    crlTargets=[Face(26), Elem(301, 341)])  # [hl:end]
