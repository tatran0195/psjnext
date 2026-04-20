# Title:   Tools.ToPost()
# Desc:    Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.ToPost
# ---
# Prepare Pre model
Geometry.Part.Cube()

# Convert to Post
Tools.ToPost(strName="Jupiter1", ilOptions=[0, 1, 2, 3, 4])  # [hl]
