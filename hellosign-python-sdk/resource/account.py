from http.request import HSRequest
from resource import Resource
import json

class Account(Resource):

	# ACCOUNT_KEY = "account";
	# ACCOUNT_ID = "account_id";
	# ACCOUNT_EMAIL_ADDRESS = "email_address";
	# ACCOUNT_IS_PAID_HS = "is_paid_hs";
	# ACCOUNT_IS_PAID_HF = "is_paid_hf";
	# ACCOUNT_TEMPLATES_LEFT = "templates_left";
	# ACCOUNT_API_SIG_REQS_LEFT = "api_signature_requests_left";
	# ACCOUNT_CALLBACK_URL = "callback_url";
	# ACCOUNT_ROLE_CODE = "role_code";
	# OAUTH_DATA = "oauth_data";
	# ACCOUNT_PASSWORD = "password";
	ACCOUNT_INFO_URL = 'https://api.hellosign.com/v3/account'
	ACCOUNT_UPDATE_URL = 'https://api.hellosign.com/v3/account'

	"""docstring for Account"""
	# def __init__(self, arg):
	# 	super(Account, self).__init__()
	# 	self.arg = arg

	def get_info(self):
		request = HSRequest()
		response = request.get(self.ACCOUNT_INFO_URL)
		# TODO: update info using get & set
		return response

	def update_info(self):
		request = HSRequest()
		response = request.post(self.ACCOUNT_UPDATE_URL)
		return response