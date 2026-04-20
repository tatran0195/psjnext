# Title:   Home.AddResults.Actran()
# Desc:    Add Actran Op2 results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Actran
# ---
# Please put mesh and actran file below path
meshfile='C:/Sample/mesh.bdf'
actrandatafile= 'C:/Sample/actran.op2'

Home.ImportResults.ImportMesh.Nastran(meshfile, bReadLoadAndConstraint=True, bReadConnection=True)
Home.AddResults.Actran(strlPaths=[actrandatafile], bMergeTree=False)  # [hl]
