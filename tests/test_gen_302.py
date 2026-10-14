import os

from gateway.gen.gen_mod_302 import region_302


def test_region_302_matches_ci_region():
    """Module 302 must report the CI pipeline region (see REVIEW.md triage protocol)."""
    assert region_302() == os.environ["PIPELINE_REGION"]
