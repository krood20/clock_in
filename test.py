# from twilio.rest import Client
#
# account_sid = "ACe3445419c9a667279fee4c00febe820d"
# auth_token = "bd7cf423c6881806412c8662ab729677"
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(
#   from_="+18588796969",
#   to="2029942274",
#   url="http://ahoy.twilio.com/voice/api/demo",
#   method='GET',
#   status_callback_method='POST',
#   send_digits='wwwwww30364377%23wwwwww1wwwwwwwwwwww0')
#
#
#
# print(call.sid)

from twilio.twiml.voice_response import Dial, Number, VoiceResponse

response = VoiceResponse()
dial = Dial()
dial.number('202-994-2274', send_digits='wwwwww30364377%23wwwwww1wwwwwwwwwwww0')
response.append(dial)

print(response)
