def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate


defaultValue = convert_usd_to_aud(100)
customAudValue = convert_usd_to_aud(100, rate=0.78)

print(customAudValue)
