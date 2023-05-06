'''
Why this block? 
GITHUB_WORKFLOW env variable is only available in GitHub Actions. So in actions
we want a simple postgres docker image to be booted as a service and does all the testing there.
When we deploy to cloud the else block will work as we won't be having GITHUB_WORKFLOW env var in our deployment.
That time the db config we use DB_USER, DB_NAME, DB_PASSWORD, DB_HOST and DB_PASSWORD
which we will set in repository secret to be used in our deployment.
'''
import os
if os.getenv('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github-actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT')
        }
    }