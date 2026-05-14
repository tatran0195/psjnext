---
title: "JPT.ShowMappingData()"
description: "Show specified mapping contour on current model."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Show specified mapping contour on current model.
The maximum and minimum values for this contour are automatically set. They can be modified by [Post.ResultSettings.Contour](../psj-command/post/Post.ResultSettings.Contour)\_ .

## Syntax

```psj
JPT.ShowMappingData(...)
```

## Inputs

<!-- @since:5.1.0 @type:DItem @required -->
### `DItemObject`

- The object which will be display contour.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `BoolType`

- The controls the data display type when Convection Mapping is selected.
  - _True_: Display Temperature data.
  - _False_: Display Heat Transfer Coefficient data.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {42}
import os
import csv
import itertools

def write _node _data(filename, node _data):
    headers = [
        'nodenumber', 
        'x-coordinate', 
        'y-coordinate', 
        'z-coordinate', 
        'temperature', 
        'heat-transfer-coef'
    ]
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)    
        writer.writerow(headers)
        for node in node _data:
            writer.writerow(node)

def generate _conv _data(
    size=5, 
    start _pos=-10, 
    step=5, 
    start _temp=-100, 
    temp _step=10, 
    start _coef=0.01, 
    coef _step=0.01
):
    positions = [start _pos + i * step for i in range(size)]
    nodes = [
        [i + 1, x, y, z, start _temp + i * temp _step, start _coef + i * coef _step]
        for i, (x, y, z) in enumerate(itertools.product(positions, repeat=3))
    ]
    
    return nodes

def setup _mapping _view():
    JPT.DisableScreenAnimation()
    JPT.ViewFitToModel()
    conv _map = JPT.GetEntitiesByID(JPT.EntityType.LBC _MAPPING _THERMAL _CONVECTION, 1)[0]
    JPT.ShowMappingData(conv _map)

def save _mapping _image(image _path):
    MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=False)
    Home.ToImage(strImgPath=image _path)
    MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=True)

def apply _convection _mapping(csv _path):
    BoundaryConditions.Convection.SurfaceMapping(
        strName="MappingConvection _1", 
        crlTargets=[Face(24, 26, 22)], 
        iPos=2, 
        iCp=2, 
        iMappedCpIndex0=1, 
        dSearchRange=0.0, 
        iTempUnit=1, 
        strPath=csv _path
    )

def main():
    temp _path = JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)
    csv _path = os.path.join(temp _path, 'node _data.csv')
    image _path = os.path.join(temp _path, "conv _img.png")

    #Prepare mapping data (convection)
    nodes = generate _conv _data()
    write _node _data(csv _path, nodes)

    #Preapre Model
    Geometry.Part.Cube(iPartColor=6409934)
    apply _convection _mapping(csv _path)
    
    #Show mapping result and save image
    setup _mapping _view()
    save _mapping _image(image _path)

if __name__ == "__main__":
    main()
```
