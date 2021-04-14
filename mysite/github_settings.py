# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App 

# Using ngrok is hard because the url changes every time you start ngrok

# If you are running on localhost, here are some settings:

Application name: Django4Everybody
Homepage Url: http://127.0.0.1:8000/
Application Description: Whatever
Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/


# Using PythonAnywhere here are some settings:


# Application name: Django4Everybody
# Homepage Url: https://django4everybody.pythonanywhere.com/
# Application Description: Whatever
# Authorization callback URL: https://django4everybody.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '4425dbf5df7f90f15759'
SOCIAL_AUTH_GITHUB_SECRET = '088080b3f2f62f27af0a4f0e92f594042eff08d1'

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/