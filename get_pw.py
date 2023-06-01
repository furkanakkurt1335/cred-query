import argparse, os, json

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
creds_path = os.path.join(THIS_DIR, 'creds.json')
with open(creds_path, 'r') as f:
    creds = json.load(f)

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--site', required=False)
args = parser.parse_args()

if args.site:
    site = args.site
    if site in creds:
        data = creds[site]
        username, password = data['username'], data['password']
        print(username, password, 'for', site)
    else:
        possible_sites = [k for k in creds.keys() if k.startswith(site)]
        poss_len = len(possible_sites)
        if poss_len == 1:
            data = creds[possible_sites[0]]
            username, password = data['username'], data['password']
            print(username, password, 'for', possible_sites[0])
        elif poss_len == 0:
            print('No site found')
        else:
            print('Multiple sites found:')
            for site in possible_sites:
                print('\t' + site)
else:
    print('Please specify a site with -s or --site')
    print('Available sites: ' + ', '.join(creds.keys()))