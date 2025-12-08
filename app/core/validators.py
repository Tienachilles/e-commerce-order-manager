from datetime import datetime

def is_positive_int(val):
    """Check if value is int >= 0."""
    try:
        return int(val) >= 0
    except:
        return False


def is_positive_number(val):
    """Check if value is float >= 0."""
    try:
        return float(val) >= 0
    except:
        return False


def parse_date(s):
    """
    Parse date using:
    - YYYY-MM-DD
    - DD-MM-YYYY
    Returns date or None.
    """
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except:
            continue
    return None
