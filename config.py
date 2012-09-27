app_name = "Tiny Probe"

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': '14758f1afd44c09b7992073ccf00b43d',
}
webapp2_config['webapp2_extras.auth'] = {
    'user_model': 'models.models.User',
    'cookie_name': 'session_name'
}
webapp2_config['webapp2_extras.jinja2'] = {
    'template_path': 'templates',
    'environment_args': {'extensions': ['jinja2.ext.i18n']},
}

app_lang = 'en'
# Locale code = <language>_<territory> (ie 'en_US')
# to pick locale codes see http://cldr.unicode.org/index/cldr-spec/picking-the-right-language-code
# also see http://www.sil.org/iso639-3/codes.asp
# Language codes defined under iso 639-1 http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# Territory codes defined under iso 3166-1 alpha-2 http://en.wikipedia.org/wiki/ISO_3166-1
#locales = ['en_US', 'es_ES', 'it_IT', 'zh_CN', 'id_ID', 'fr_FR', 'de_DE']
locales = ['en_US']

contact_sender = "kordless@gmail.com"
contact_recipient = "kordless@gmail.com"

salt = "5758c08d38fe9ff725033600429cde55"

# get your own consumer key and consumer secret by registering at https://dev.twitter.com/apps
# callback url must be: http://[YOUR DOMAIN]/login/twitter/complete
twitter_consumer_key = 'sBhPXfyvmZzKzeGEPKVg'
twitter_consumer_secret = 'KxFRgg0SaCyKk9p6iJOLue4M0uVoAfJc3v4MGicK7fs'

# github login
github_client_id = 'd43f79b4e7c21fa43454'
github_client_secret = 'a64ddfdc29dcf0c7590147476014950bf160883f'

# get your own recaptcha keys by registering at www.google.com/recaptcha
captcha_public_key = "6LeZidUSAAAAAH4URz_h0kKl-NDciRnE3Nw8ajJd"
captcha_private_key = "6LeZidUSAAAAAI1L48D6X2YKToFCmCpXf8VyCHvK"

google_analytics_code = "UA-34233674-1"

error_templates = {
    403: 'errors/default_error.html',
    404: 'errors/default_error.html',
    500: 'errors/default_error.html',
}

# Enable Federated login (OpenID and OAuth)
# Google App Engine Settings must be set to Authentication Options: Federated Login
enable_federated_login = True

# jinja2 base layout templates
base_layout = 'base.html'

# terminal commands URI path 
command_path = "/js/commands/"