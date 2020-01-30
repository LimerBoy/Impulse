from phonenumbers import geocoder, parse

# Make for Russian numbers
def normalize(phone):
    if phone[0] == "+":
        phone = phone[1:]
    if phone[0] == "8":
        phone = "7" + phone[1:]
    if phone[0] == "9":
        phone = "7" + phone
    return phone

# Get country name by phone
def getCountry(phone):
	query = parse("+" + phone, None)
	return repr(geocoder.description_for_number(query, 'en'))