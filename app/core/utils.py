def safe_lower(s):
    """Return lowercase safe string."""
    return (s or "").strip().lower()


def merge_search(*args):
    """Combine multiple fields into a single searchable string."""
    return " ".join([safe_lower(x) for x in args])
