# Title:   Properties.Material.Add()
# Desc:    Create a new material to the current User database library
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Material.Add
# ---
#Prepare material with unit
dict_mat_prop = {
    'Density': {
        'density': {
            'DENSITY': [8.3e-9],
        },
    },
    'Elastic': {
        'elastic': {
            'POISSONS_RATIO': [0.3],
            'YOUNGS_MODULUS': [1.1e+5],
            'SHEAR_MODULUS': [5.2e+3],
        }
    },
    'Unit': {
        'Density': {
            'density': {  
                'DENSITY': JPT.DensityUnit.Density_t_mm3
            }
        },
        'Elastic': {
            'elastic': {  
                'YOUNGS_MODULUS': JPT.ModulusUnit.Modulus_N_mm2
            }
        }
    }
}

#Add new material to document
new_material=Properties.Material.Add(  # [hl:start]
    strMaterialName="NewMaterial", 
    dictMaterialProperty=dict_mat_prop,
    iMaterialID=1, 
    iMaterialColor=9614382)  # [hl:end]

JPT.Debugger(new_material) #for checking return value
