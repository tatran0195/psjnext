# Title:   JPT.SaveToMLIB()
# Desc:    Save materials iin document to .mlib file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_SaveToMLIB
# ---
# Create materials in User Data Base.
Properties.Material.Add(
    strMaterialName="MyMaterial1",
    dictMaterialProperty={
        'Density': {
            'density': {
                'DENSITY': [8300.0]}}, 
        'Elastic': {
            'elastic': {
                'YOUNGS_MODULUS': [110000000000.0], 
                'POISSONS_RATIO': [0.34]}}}, 
    iMaterialID=1, 
    iMaterialColor=7901428)

Properties.Material.Add(
    strMaterialName="MyMaterial2", 
    dictMaterialProperty={
        'Density': {
            'density': {
                'DENSITY': [2770.0]}}, 
        'Elastic': {
            'elastic': {
                'YOUNGS_MODULUS': [71000000000.0], 
                'POISSONS_RATIO': [0.33]}}}, 
     iMaterialID=2, 
    iMaterialColor=11052963)

# Get all materials from current user data base. 
strCrlMaterials=[mat.id for mat in JPT.GetAllMaterials()]
strMlibFileName = "C:/Temp/new.mlib" 

crlMaterials=Material(*[mat.id for mat in JPT.GetAllMaterials()])

JPT.SaveToMLIB(  # [hl]
    strFileName=strMlibFileName, 
    crlMaterials=[crlMaterials], 
    bAppendToCurrentMlib=True # Include all the materials in Library Data Base
)
