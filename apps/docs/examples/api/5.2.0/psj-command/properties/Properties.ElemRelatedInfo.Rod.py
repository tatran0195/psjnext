# Title:   Properties.ElemRelatedInfo.Rod()
# Desc:    Modify information such as direction vectors and end releases for the selected rod elements, individually
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.ElemRelatedInfo.Rod
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
Properties.Rod(
    strName="ROD_1", 
    iPropertyColor=3742001, 
    crMat=Material(5), 
    dArea=2e-07, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Rod(  # [hl:start]
        listERIRodData=[
            ERIROD_DATA(
                iElemId=87, 
                iPropId=1, 
                iEndA=79, 
                iEndB=78)])  # [hl:end]
print(ret)
