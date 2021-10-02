# buzzmaker

This is a service to generate links for the buzzcorner in yaml file. Currently this is generated daily. This is the same format as what we use in devkami.com

# Structure

* code is at `make_buzz/app.py`
* dependency is at `make_buzz/requirements.txt`
* `template.yml` have the definition for AWS Sam

# Deployment

This is installed with sam. I will not cover the installation.

* `sam build --profile someprofile`
* `sam deploy -g --profile someprofile`

