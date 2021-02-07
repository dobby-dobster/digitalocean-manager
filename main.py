#!/usr/bin/env python

import os
import logging
import digitalocean

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
DO_TOKEN = os.getenv('DO_TOKEN') 

manager = digitalocean.Manager(token=DO_TOKEN)

def Droplets():
    """
    Find all droplets and destroy any with no tags
    """
    my_droplets = manager.get_all_droplets()
    num = len(my_droplets)
    if num > 0:
        logging.info('Found a total of %s droplets: %s', num, my_droplets)
        for droplet in my_droplets:
            if not droplet.tags :
                logging.info('Droplet has no tags %s %s, deleting...', droplet.id, droplet.name)
                try:
                    droplet.destroy()
                    logging.info('Droplet deleted')
                except:
                    logging.warn('Failed to destroy %s %s!', droplet.id, droplet.name)
    else:
        logging.info('Found 0 droplets')

def Loadbalancers():
    """
    Find all loadbalancers and destroy any with no associated droplets
    """
    my_lbs = manager.get_all_load_balancers()
    num = len(my_lbs)
    if num > 0:
        logging.info('Found a total of %s lbs: %s', num, my_lbs)
        for lb in my_lbs:
            if not lb.droplet_ids:
                logging.info('Loadbalancer %s has no droplets associated, deleting', lb)
                try:
                    lb.destroy()
                except:
                    logging.warn('Failed to destroy')
    else:
        logging.info('Found 0 loadbalancers')

if __name__ == "__main__":
    Droplets()
    Loadbalancers()
