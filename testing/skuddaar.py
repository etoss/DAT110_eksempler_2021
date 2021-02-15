def skuddaar(aar):
    if aar%400 == 0:
        return True
    if aar%100 == 0:
        return False
    if aar%4 == 0:
        return True
    return False
