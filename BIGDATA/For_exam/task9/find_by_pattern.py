import re
def find_by_pattern(data: str) -> int:
    return len(re.findall(r'x.y.z', data))
