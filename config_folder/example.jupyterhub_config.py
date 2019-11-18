
# Configuration file for jupyterhub.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
c.Application.log_format = '[%(name)s] %(message)s'

## Set the log level by value or name.
c.Application.log_level = 'DEBUG'


#------------------------------------------------------------------------------
# JupyterHub(Application) configuration
#------------------------------------------------------------------------------

## An Application for starting a Multi-User Jupyter Notebook server.

## Maximum number of concurrent servers that can be active at a time.
#
#  Setting this can limit the total resources your users can consume.
#
#  An active server is any server that's not fully stopped. It is considered
#  active from the time it has been requested until the time that it has
#  completely stopped.
#
#  If this many user servers are active, users will not be able to launch new
#  servers until a server is shutdown. Spawn requests will be rejected with a 429
#  error asking them to try again.
#
#  If set to 0, no limit is enforced.
#c.JupyterHub.active_server_limit = 0

## Duration (in seconds) to determine the number of active users.
#c.JupyterHub.active_user_window = 1800

## Grant admin users permission to access single-user servers.
#
#  Users should be properly informed if this is enabled.
c.JupyterHub.admin_access = True

## DEPRECATED since version 0.7.2, use Authenticator.admin_users instead.
#c.JupyterHub.admin_users = set()

## Allow named single-user servers per user
#c.JupyterHub.allow_named_servers = False

## Answer yes to any questions (e.g. confirm overwrite)
#c.JupyterHub.answer_yes = False

#------------------------------------------------------------------------------
# Authenticator configuration
#------------------------------------------------------------------------------

# A class for authentication.
# 
# The primary API is one method, `authenticate`, a tornado coroutine for
# authenticating users.

# set of usernames of admin users
# 
# If unspecified, only the user that launches the server will be admin.
# c.Authenticator.admin_users = set()

# Dictionary mapping authenticator usernames to JupyterHub users.
# 
# Can be used to map OAuth service names to local users, for instance.
# 
# Used in normalize_username.
# c.Authenticator.username_map = {}

# Regular expression pattern for validating usernames.
# 
# If not defined: allow any username.
# c.Authenticator.username_pattern = ''

# Username whitelist.
# 
# Use this to restrict which users can login. If empty, allow any user to
# attempt login.
c.Authenticator.whitelist = {'account1@clh.com', 'account1@clh.com'}
c.Authenticator.admin_users = {'account2@clh.com', 'account2@clh.com'}

#------------------------------------------------------------------------------
# LocalAuthenticator configuration
#------------------------------------------------------------------------------

# Base class for Authenticators that work with local Linux/UNIX users
# 
# Checks for local users, and can attempt to create them if they exist.

# The command to use for creating users as a list of strings.
# 
# For each element in the list, the string USERNAME will be replaced with the
# user's username. The username will also be appended as the final argument.
# 
# For Linux, the default value is:
# 
#     ['adduser', '-q', '--gecos', '""', '--disabled-password']
# 
# To specify a custom home directory, set this to:
# 
#     ['adduser', '-q', '--gecos', '""', '--home', '/customhome/USERNAME', '--
# disabled-password']
# 
# This will run the command:
# 
# adduser -q --gecos "" --home /customhome/river --disabled-password river
# 
# when the user 'river' is created.
# c.LocalAuthenticator.add_user_cmd = []
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']

# If a user is added that doesn't exist on the system, should I try to create
# the system user?
# c.LocalAuthenticator.create_system_users = False
c.LocalAuthenticator.create_system_users = True

# Automatically whitelist anyone in this group.
# c.LocalAuthenticator.group_whitelist = set()

#------------------------------------------------------------------------------
# Spawner configuration
#------------------------------------------------------------------------------

# Base class for spawning single-user notebook servers.
# 
# Subclass this, and override the following methods:
# 
# - load_state - get_state - start - stop - poll

# Extra arguments to be passed to the single-user server
# c.Spawner.args = []

# The command used for starting notebooks.
# c.Spawner.cmd = ['jupyterhub-singleuser']

# Enable debug-logging of the single-user server
# c.Spawner.debug = False

# Whitelist of environment variables for the subprocess to inherit
# c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']

# Timeout (in seconds) before giving up on a spawned HTTP server
# 
# Once a server has successfully been spawned, this is the amount of time we
# wait before assuming that the server is unable to accept connections.
# c.Spawner.http_timeout = 30

# The IP address (or hostname) the single-user server should listen on
# c.Spawner.ip = 'localhost'

# The notebook directory for the single-user server
# 
# `~` will be expanded to the user's home directory `%U` will be expanded to the
# user's username
c.Spawner.notebook_dir = '~'

# An HTML form for options a user can specify on launching their server. The
# surrounding `<form>` element and the submit button are already provided.
# 
# For example:
# 
#     Set your key:
#     <input name="key" val="default_key"></input>
#     <br>
#     Choose a letter:
#     <select name="letter" multiple="true">
#       <option value="A">The letter A</option>
#       <option value="B">The letter B</option>
#     </select>
# c.Spawner.options_form = ''

# Interval (in seconds) on which to poll the spawner.
# c.Spawner.poll_interval = 30

# Timeout (in seconds) before giving up on the spawner.
# 
# This is the timeout for start to return, not the timeout for the server to
# respond. Callers of spawner.start will assume that startup has failed if it
# takes longer than this. start should return when the server process is started
# and its location is known.
# c.Spawner.start_timeout = 60


#------------------------------------------------------------------------------
# PAMAuthenticator configuration
#------------------------------------------------------------------------------

# Authenticate local Linux/UNIX users with PAM

# The encoding to use for PAM
# c.PAMAuthenticator.encoding = 'utf8'

# The PAM service to use for authentication.
# c.PAMAuthenticator.service = 'login'

c.PAMAuthenticator.open_sessions = False
c.JupyterHub.statsd_prefix = 'jupyterhub'

#------------------------------------------------------------------------------
# LocalGoogleOAuthenticator configuration
#------------------------------------------------------------------------------

from oauthenticator.google import LocalGoogleOAuthenticator
c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator

# use Google OAuthenticator for local users
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGoogleOAuthenticator'
# Need to create certificate in gcp interface and get client_id, client_secret
c.GoogleOAuthenticator.oauth_callback_url = 'http://your_domain_url:8000/hub/oauth_callback'
c.GoogleOAuthenticator.client_id = 'your_client_id'
c.GoogleOAuthenticator.client_secret = 'your_client_secret'
c.GoogleOAuthenticator.hosted_domain = ['host_name']
c.GoogleOAuthenticator.login_service = 'Login with email'





