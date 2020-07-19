# matching.py --- Summer postcrossing scripts

# Copyright (C) 2020 Jochem Raat <jochem@invulns.nl>

# Author: Jochem Raat <jochem@invulns.nl>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import csv
import random

FIELDS = ['country', 'email']
ENTRIES = {}
EMAILS = []



def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDS, skipinitialspace=True)
        for row in reader:
            ENTRIES[row['email']] = row
            EMAILS.append(row['email'])

read_data('emails.csv')

assert(len(ENTRIES) == 54)
assert(len(EMAILS) == 54)


BUDDIES = []
MISMATCHES = 0

def find_match(person, people):

    for i in range(1, 100):
        potential_buddy = random.choice(people)
        country1 = ENTRIES[potential_buddy]['country']
        country2 = ENTRIES[person]['country']

        if (potential_buddy != person
            and
            country1 != country2
            and
            (country1 == 'Netherlands' or country2 == 'Netherlands')):
            return potential_buddy

    print("WARNING: could not find a buddy from a different country for " + person)
    global MISMATCHES
    MISMATCHES += 1

    return random.choice(people)


def match_buddies():
    people = EMAILS.copy()

    while people:
        person = people.pop()
        buddy = find_match(person, people)

        people.remove(buddy)

        BUDDIES.append((person, buddy))

match_buddies()
print(BUDDIES)
print(MISMATCHES)

with open('buddies.csv', 'w', newline='') as csvfile:
    buddywriter = csv.writer(csvfile)
    for buddy in BUDDIES:
        buddywriter.writerow([buddy[0], buddy[1]])
