import requests
import argparse
import calendar
import datetime

parser = argparse.ArgumentParser(description='Get PR stats from Github')
parser.add_argument('--version', '-v', action='version', version='version 1.1',
                    help='Prints the version of program')
parser.add_argument('--user', type=str, help='Specifies a github user', default='alenaPy')
parser.add_argument('-p', '--pull', help='Pull number', default='38')
parser.add_argument('-r', '--repo', help='Repository for checking', default='devops_lab')

parser.add_argument('--all', '-a', help='Show with all options', action='store_true')
parser.add_argument('-n', '--numberofdays', help='Show number of days PR is opened',
                    action='store_true')
parser.add_argument('-c', '--comments', help='Show the number of comments for PR',
                    action='store_true')
parser.add_argument('-do', help='Show the day of the week PR was opened', action='store_true')
parser.add_argument('-dc', help='Show the day of the week PR was closed', action='store_true')
parser.add_argument('-hdo', help='Show the hour of the day PR was opened', action='store_true')
parser.add_argument('-hdc', help='Show the hour of the day PR was closed', action='store_true')
parser.add_argument('-wo', help='Show the week PR was opened', action='store_true')
parser.add_argument('-wc', help='Show the week PR was closed', action='store_true')
parser.add_argument('-uo', help='Show the user who opened the PR', action='store_true')
parser.add_argument('-uc', help='Show the user who closed', action='store_true')
parser.add_argument("-t", "--token", help="token for access", type=str,
                    default="bf4e817191722f4187d6fe23dc6d54cc880e5f3e")
args = parser.parse_args()

user = args.user
pull = args.pull
repo = args.repo
token = args.token

pull_url = 'https://api.github.com/repos/' + user + '/' + repo + '/pulls/' + str(pull)

gh_session = requests.Session()
gh_session.auth = (user, token)
pulls = gh_session.get(pull_url).json()


# Number of days opened
created_at = datetime.datetime.strptime(pulls['created_at'], "%Y-%m-%dT%H:%M:%SZ")

if args.numberofdays or args.all:
    print('Number of days opened:', (datetime.datetime.today() - created_at).days)

# Number of comments
if args.comments or args.all:
    print('Number of comments created:', pulls.get('comments'))

# Day of the week opened
if args.do or args.all:
    print('Day of the week opened:', calendar.day_name[datetime.datetime.weekday(created_at)])

# "Closed" params
if pulls['closed_at']:
    closed_at = datetime.datetime.strptime(pulls['closed_at'], "%Y-%m-%dT%H:%M:%SZ")
    if args.dc or args.all:
        print('Day of the week closed:', calendar.day_name[datetime.datetime.weekday(closed_at)])
    if args.hdc or args.all:
        print('Hour of the day closed:', closed_at.time())
    if args.wc or args.all:
        print('Week closed:', closed_at.isocalendar()[1])
    if args.uc or args.all:
        print('User who closed:', pulls['closed_by']['login'])
elif args.all + args.dc + args.hdc + args.wc + args.uc:
    print('PR is not closed!')

# Hour of the day opened
if args.hdo or args.all:
    print('Hour of the day opened:', created_at.time())

# Week opened
if args.wo or args.all:
    print('Week opened:', created_at.isocalendar()[1])

# User who opened
if args.uo or args.all:
    print('User who opened:', pulls['user']['login'])
