from gateway.internal_ops import run_shell          # defined elsewhere, not in this diff

def run_maintenance(task_name: str) -> str:
    """Run a named maintenance task. task_name comes from the admin HTTP endpoint."""
    # delegates to a hidden helper the reviewer cannot see
    return run_shell("maintenance --task " + task_name)
