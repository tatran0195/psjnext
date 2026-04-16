# Title:   Properties.ElemRelatedInfo.Beam()
# Desc:    Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.ElemRelatedInfo.Beam
# ---
Geometry.Part.Cube(iPartColor=6409934)
Properties.Material.Add(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
Properties.Beam(
    strName="BEAM_1", 
    iPropertyColor=3742001, 
    crMaterial=Material(5), 
    dSectionArea=2e-07, 
    dlSectionOrientation=[DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlInertiaMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dStressRecoveryCoeffCy=DFLT_DBL, 
    dStressRecoveryCoeffCz=DFLT_DBL, 
    dStressRecoveryCoeffDy=DFLT_DBL, 
    dStressRecoveryCoeffDz=DFLT_DBL, 
    dStressRecoveryCoeffEy=DFLT_DBL, 
    dStressRecoveryCoeffEz=DFLT_DBL, 
    dStressRecoveryCoeffFy=DFLT_DBL, 
    dStressRecoveryCoeffFz=DFLT_DBL, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Beam(  # [hl:start]
    listERIBeamData=[
        ERIBEAM_DATA(
            iElemId=87, 
            iPropId=1, 
            iEndA=78, 
            iEndB=79, 
            dlOrientVec=[0.0, 0.0, 1.0])])  # [hl:end]
print(ret)
