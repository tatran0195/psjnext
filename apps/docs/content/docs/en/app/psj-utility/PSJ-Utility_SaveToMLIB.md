---
title: "JPT.SaveToMLIB()"
description: "Save materials iin document to .mlib file."
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Save materials in document to .mlib file.

## Syntax

```psj
JPT.SaveToMLIB(...)
```

## Inputs

### `strFileName` @type(String) @required

- Sspecifying the path of .mlib file to save.

### `bAppendToCurrentMlib` @type(Boolean) @required

- Whether the materials in current library also copied in the .mlib file.

### `crlMaterials` @type(List\[Cursor]) @default(\[])

- The materials needed to save.

## Return Code

- _True_ : The function can be executed
- _False_ : The function cannot be executed

## Sample Code

```psj {34}
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

JPT.SaveToMLIB(
    strFileName=strMlibFileName, 
    crlMaterials=[crlMaterials], 
    bAppendToCurrentMlib=True # Include all the materials in Library Data Base
)
```
