

try:
    if os.path.isfile('./credentials.py'):
        from credentials import auth_url, username, project_id, user_domain_id, ssl_bundle
    else:
        print "credentials.py file missing, please create one. ie:\n{cred}".format(cred=example_credentials)
        raise SystemExit
except ImportError:
    print "Unable to read all variables, ensure file is correct, i.e.:"
    print example_credentials
    raise SystemExit
