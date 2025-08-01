def get_workspace_id(workspace_name: str, workspaces_response_result: dict) -> str | None:
    """Return the workspace_id assigned to the workspace in fabric."""
    for workspace in workspaces_response_result["body"]["value"]:
        if workspace["displayName"] == workspace_name:
            return workspace["id"]
    print("Workspace not found")
    return None


def get_artifact_id(artifact_name: str, workspace_id: str, items_response_result: dict) -> str:
    """Return the artifact_id in a workspace from the artifact name and workspace id."""
    # url = f"{FABRIC_API_BASE_URL}/workspaces/{workspace_id}/items"

    artifact_dict = {x["displayName"]: x for x in items_response_result["body"]["value"]}

    artifact = artifact_dict.get(artifact_name)
    if artifact is None:
        raise ValueError(f"Artifact with name {artifact_name} not Found in workspace with ID: {workspace_id}")
    artifact_id = artifact.get("id")

    return artifact_id
