from phonenumbers import geocoder, parse

# Make for Russian numbers
def normalize(phone):
    if phone[0] == "+":
        phone = phone[1:]
    return phone

# Make for other services
def transformPhone(phone, i):
	# Pizzahut
	if i == 5:
		return '+' + phone[0] + ' (' + phone[1:4] + ') ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11] # '+7 (915) 350 99 08'

# Get country name by phone
def getCountry(phone):
	query = parse("+" + phone, None)
	return repr(geocoder.description_for_number(query, 'en'))
