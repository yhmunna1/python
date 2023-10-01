# We need to sue 'self' parameter for all the time

def call():
    print('Calling someone')
    return 'Call Done'

class Phone:
    price = 28000
    color = 'blue'
    brand = 'xiaomi'
    features = ['camera', '64mp', '120hz']

    def call(self):
        print('Calling a person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text


my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(12345, 'I missed to miss you')
print(result)
