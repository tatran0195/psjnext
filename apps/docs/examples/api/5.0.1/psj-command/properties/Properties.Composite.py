# Title:   Properties.Composite()
# Desc:    Create 2D Composite Material Shell Property
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Composite
# ---
Geometry.Part.Cube()
Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Composite(strName="ComMatShell1", iPropertyColor=16131973, crMaterial=Material(1),  # [hl:start]
    iPID=1, crlTargets=[Face(26)])  # [hl:end]
