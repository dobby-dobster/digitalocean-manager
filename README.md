# digitalocean-manager

Small python script which carries out the following:

- Destroys any droplets (aka instances) which have no tags
- Destroys any loadbalancer which has no associated droplets

Requires the 'python-digitalocean' python module.

`pip install -U python-digitalocean`

## Usage

Pass in DigitalOcean access token as environment variable.

`DO_TOKEN="XXXXXXXXXXXXXX" python main.py`