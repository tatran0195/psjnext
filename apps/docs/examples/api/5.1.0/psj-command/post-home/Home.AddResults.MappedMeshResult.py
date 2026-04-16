# Title:   Home.AddResults.MappedMeshResult()
# Desc:    Add mapped mesh result to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.MappedMeshResult
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.dat"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.MappedMeshResult(strlPaths=[Result], bMergeTree=False)  # [hl]
