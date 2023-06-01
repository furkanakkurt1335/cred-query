import argparse, os, json, pyotp

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
totp_path = os.path.join(THIS_DIR, 'totp_d.json')
with open(totp_path, 'r') as f:
    totp_d = json.load(f)

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--site', required=False)
args = parser.parse_args()

if args.site:
    site = args.site
    if site in totp_d:
        secret = totp_d[site].replace(' ', '')
        totp = pyotp.TOTP(secret).now()
        print(totp, 'for', site)
    else:
        possible_sites = [k for k in totp_d.keys() if k.startswith(site)]
        poss_len = len(possible_sites)
        if poss_len == 1:
            secret = totp_d[possible_sites[0]].replace(' ', '')
            totp = pyotp.TOTP(secret).now()
            print(totp, 'for', possible_sites[0])
        elif poss_len == 0:
            print('No site found')
        else:
            print('Multiple sites found:')
            for site in possible_sites:
                print('\t' + site)
else:
    print('Please specify a site with -s or --site')
    print('Available sites: ' + ', '.join(totp_d.keys()))
