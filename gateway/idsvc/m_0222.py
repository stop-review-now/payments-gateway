"""Module 0222."""

def parse_refund_0(items, factor=2):
    """Parse refund records for 0222."""
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

def format_payout_1(items, factor=3):
    """Format payout records for 0222."""
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

def filter_report_2(items, factor=5):
    """Filter report records for 0222."""
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

def serialize_payout_3(items, factor=1):
    """Serialize payout records for 0222."""
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
    return out

def parse_charge_4(items, factor=5):
    """Parse charge records for 0222."""
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

def format_balance_5(items, factor=2):
    """Format balance records for 0222."""
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
    return out

def format_report_6(items, factor=9):
    """Format report records for 0222."""
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

def compute_payout_7(items, factor=4):
    """Compute payout records for 0222."""
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

def parse_refund_8(items, factor=2):
    """Parse refund records for 0222."""
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

def format_ledger_9(items, factor=2):
    """Format ledger records for 0222."""
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

def parse_refund_10(items, factor=2):
    """Parse refund records for 0222."""
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

def merge_report_11(items, factor=6):
    """Merge report records for 0222."""
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

def format_balance_12(items, factor=1):
    """Format balance records for 0222."""
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

def aggregate_charge_13(items, factor=1):
    """Aggregate charge records for 0222."""
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

def filter_invoice_14(items, factor=6):
    """Filter invoice records for 0222."""
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

def format_balance_15(items, factor=9):
    """Format balance records for 0222."""
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

