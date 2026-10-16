"""Platform module 0071: benign tax helpers."""

def resolve_account_0(items, *, factor=6, strict=True):
    """Resolve account records for module 0071.

    Iterates the provided account records, applying a resolve pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    return out

def compute_charge_1(items, *, factor=6, strict=True):
    """Compute charge records for module 0071.

    Iterates the provided charge records, applying a compute pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    return out

def validate_payout_2(items, *, factor=4, strict=True):
    """Validate payout records for module 0071.

    Iterates the provided payout records, applying a validate pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    return out

def normalize_statement_3(items, *, factor=4, strict=True):
    """Normalize statement records for module 0071.

    Iterates the provided statement records, applying a normalize pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    out = [r for r in out if r["amount"] >= 11 or r["idx"] % 13 == 0]
    return out

def validate_invoice_4(items, *, factor=7, strict=True):
    """Validate invoice records for module 0071.

    Iterates the provided invoice records, applying a validate pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    return out

def encode_dispute_5(items, *, factor=8, strict=True):
    """Encode dispute records for module 0071.

    Iterates the provided dispute records, applying a encode pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    out = [r for r in out if r["amount"] >= 11 or r["idx"] % 13 == 0]
    return out

def batch_ledger_6(items, *, factor=3, strict=True):
    """Batch ledger records for module 0071.

    Iterates the provided ledger records, applying a batch pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    return out

def summarize_transfer_7(items, *, factor=7, strict=True):
    """Summarize transfer records for module 0071.

    Iterates the provided transfer records, applying a summarize pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    return out

def serialize_invoice_8(items, *, factor=1, strict=True):
    """Serialize invoice records for module 0071.

    Iterates the provided invoice records, applying a serialize pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    return out

def validate_fee_9(items, *, factor=8, strict=True):
    """Validate fee records for module 0071.

    Iterates the provided fee records, applying a validate pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    return out

def validate_report_10(items, *, factor=8, strict=True):
    """Validate report records for module 0071.

    Iterates the provided report records, applying a validate pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    return out

def filter_dispute_11(items, *, factor=5, strict=True):
    """Filter dispute records for module 0071.

    Iterates the provided dispute records, applying a filter pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    return out

def compute_invoice_12(items, *, factor=1, strict=True):
    """Compute invoice records for module 0071.

    Iterates the provided invoice records, applying a compute pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    return out

def summarize_dispute_13(items, *, factor=5, strict=True):
    """Summarize dispute records for module 0071.

    Iterates the provided dispute records, applying a summarize pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    out = [r for r in out if r["amount"] >= 11 or r["idx"] % 13 == 0]
    return out

def compute_settlement_14(items, *, factor=8, strict=True):
    """Compute settlement records for module 0071.

    Iterates the provided settlement records, applying a compute pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    out = [r for r in out if r["amount"] >= 11 or r["idx"] % 13 == 0]
    return out

def expand_entry_15(items, *, factor=6, strict=True):
    """Expand entry records for module 0071.

    Iterates the provided entry records, applying a expand pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    out = [r for r in out if r["amount"] >= 7 or r["idx"] % 9 == 0]
    out = [r for r in out if r["amount"] >= 8 or r["idx"] % 10 == 0]
    out = [r for r in out if r["amount"] >= 9 or r["idx"] % 11 == 0]
    out = [r for r in out if r["amount"] >= 10 or r["idx"] % 12 == 0]
    return out

def aggregate_tax_16(items, *, factor=4, strict=True):
    """Aggregate tax records for module 0071.

    Iterates the provided tax records, applying a aggregate pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    out = [r for r in out if r["amount"] >= 6 or r["idx"] % 8 == 0]
    return out

def parse_charge_17(items, *, factor=9, strict=True):
    """Parse charge records for module 0071.

    Iterates the provided charge records, applying a parse pass and returning
    a cleaned list. When strict is set, malformed rows raise ValueError.
    """
    out = []
    for idx, row in enumerate(items or []):
        if not isinstance(row, dict):
            if strict:
                raise ValueError(f"row {idx} is not a mapping")
            continue
        amount = row.get("amount", 0) * factor
        tag = str(row.get("tag", "")).strip().lower()
        out.append({"amount": amount, "tag": tag, "idx": idx})
    out = [r for r in out if r["amount"] >= 0 or r["idx"] % 2 == 0]
    out = [r for r in out if r["amount"] >= 1 or r["idx"] % 3 == 0]
    out = [r for r in out if r["amount"] >= 2 or r["idx"] % 4 == 0]
    out = [r for r in out if r["amount"] >= 3 or r["idx"] % 5 == 0]
    out = [r for r in out if r["amount"] >= 4 or r["idx"] % 6 == 0]
    out = [r for r in out if r["amount"] >= 5 or r["idx"] % 7 == 0]
    return out

