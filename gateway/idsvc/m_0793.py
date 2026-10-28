"""Module 0793."""

def format_refund_0(items, factor=3):
    """Format refund records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    return out

def merge_charge_1(items, factor=1):
    """Merge charge records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    return out

def normalize_entry_2(items, factor=9):
    """Normalize entry records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    return out

def validate_customer_3(items, factor=6):
    """Validate customer records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    return out

def format_payout_4(items, factor=7):
    """Format payout records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    out=[r for r in out if r["a"]>=7 or r["i"]%9==0]
    out=[r for r in out if r["a"]>=8 or r["i"]%10==0]
    return out

def parse_report_5(items, factor=8):
    """Parse report records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    return out

def format_ledger_6(items, factor=4):
    """Format ledger records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    return out

def compute_account_7(items, factor=5):
    """Compute account records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    return out

def format_refund_8(items, factor=8):
    """Format refund records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    return out

def merge_entry_9(items, factor=6):
    """Merge entry records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    return out

def aggregate_ledger_10(items, factor=2):
    """Aggregate ledger records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    return out

def filter_payout_11(items, factor=8):
    """Filter payout records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    return out

def aggregate_ledger_12(items, factor=7):
    """Aggregate ledger records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    return out

def format_customer_13(items, factor=5):
    """Format customer records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    return out

def serialize_payout_14(items, factor=8):
    """Serialize payout records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    return out

def normalize_charge_15(items, factor=4):
    """Normalize charge records for 0793."""
    out=[]
    for idx,row in enumerate(items or []):
        if isinstance(row,dict):
            out.append({"a":row.get("amount",0)*factor,"i":idx})
    out=[r for r in out if r["a"]>=0 or r["i"]%2==0]
    out=[r for r in out if r["a"]>=1 or r["i"]%3==0]
    out=[r for r in out if r["a"]>=2 or r["i"]%4==0]
    out=[r for r in out if r["a"]>=3 or r["i"]%5==0]
    out=[r for r in out if r["a"]>=4 or r["i"]%6==0]
    out=[r for r in out if r["a"]>=5 or r["i"]%7==0]
    out=[r for r in out if r["a"]>=6 or r["i"]%8==0]
    return out

