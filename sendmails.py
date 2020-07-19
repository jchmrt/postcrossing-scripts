# sendmails.py --- Summer postcrossing scripts

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

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import csv
import time
import random

# Fill in these variables for the email address you will be using:
MY_ADDRESS = "your-email-here"
PASSWORD = "your-password-here"
SMTP_SERVER = "smtp.gmail.com" # Or some other server if using a
                               # different mail provider.
SMTP_PORT = 587


BUDDIES = []
ALREADY_SENT_FILE = 'already-sent.txt'
ALREADY_SENT = []
TO_SEND = []



def read_buddies(filename):
    """Read in the buddies from the file and add them to the list
    BUDDIES"""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            personA = {"name":    row["0"],
                       "email":   row["1"],
                       "address": row["2"],
                       "memory":  row["3"],
                       "bio":     row["4"],
                       "holiday": row["5"],
                       "song":    row["6"]}
            personB = {"name":    row["7"],
                       "email":   row["8"],
                       "address": row["9"],
                       "memory":  row["10"],
                       "bio":     row["11"],
                       "holiday": row["12"],
                       "song":    row["13"]}
            BUDDIES.append((personA, personB))

def read_already_sent(filename):
    with open(filename) as f:
        for line in f.read().splitlines():
            ALREADY_SENT.append(line)

def generate_emails():
    for (personA, personB) in BUDDIES:
        msg1 = generate_email(personA, personB)
        msg2 = generate_email(personB, personA)
        TO_SEND.append(msg1)
        TO_SEND.append(msg2)


def generate_email(p_entry, b_entry):
    msg = MIMEMultipart('alternative')
    msg['From'] = MY_ADDRESS
    msg['To'] = p_entry["email"]
    msg['Subject'] = "Summer Postcrossing Mate Details"


    body_plain = f"""
Dear {p_entry['name']},

Thank you for joining AEGEE-Nijmegen's second Summer Postcrossing.

Down below you can find your mate's details and now it is up to you to pick the funniest or most beautiful card you can find and send it to him/her before the 1st of September 2020. We would be delighted if you share a picture of the card you received on our Facebook event (<insert facebook event here>) and share this summer happiness with us.

We have also collected all your favorite summer songs in one spotify
playlist. Check out this amazing playlist here: <insert spotify here>

Here are your Summer Postcrossing Mate details:

Name: {b_entry['name']}
Address: {b_entry['address']}
Favorite summer song: {b_entry['song']}
Tell a little bit about yourself:  {b_entry['bio']}
Best summer memory: {b_entry['memory']}
Favourite holiday destination:  {b_entry['holiday']}

Enjoy your summer!

Postcrossing team
AEGEE-Nijmegen
"""
    body_html = f"""\
<html>
  <head></head>
  <body>
<p>Dear {p_entry['name']},</p>

<p>Thank you for joining AEGEE-Nijmegen's second Summer Postcrossing. </p>

<p>Down below you can find your mate's details and now it is up to you
  to pick the funniest or most beautiful card you can find and send it
  to him/her <b>before the 1st of September 2020</b>. We would be delighted
  if you share a picture of the card you received on our <a href="<insert facebook event here>">Facebook event</a> and share this summer happiness with us.</p>

<p>We have also collected all your favorite summer songs in one
  spotify playlist. Check out this amazing playlist <a href="<insert spotify here>">here</a>!</p>

<p><b>Here are your Summer Postcrossing Mate details:</b>
<br>
<u>Name:</u> {b_entry['name']}<br>
<u>Address:</u> {b_entry['address']}<br>
<u>Favorite summer song:</u> {b_entry['song']}<br>
<u>Tell a little bit about yourself:</u>  {b_entry['bio']}<br>
<u>Best summer memory:</u> {b_entry['memory']}<br>
<u>Favourite holiday destination:</u> {b_entry['holiday']}</p>

<p>Enjoy your summer!</p>

<p>
Postcrossing team<br>
AEGEE-Nijmegen
</p>
  </body>
</html>
"""

    msg.attach(MIMEText(body_plain, 'plain'))
    msg.attach(MIMEText(body_html, 'html'))

    return msg

def add_to_sent(email):
    """Add an email address to the ALREADY_SENT list, so that we don't
    sent to it again."""
    ALREADY_SENT.append(email)

    with open(ALREADY_SENT_FILE, 'a') as f:
        f.write(email)
        f.write('\n')


def send_mails():
    """Send all emails in the TO_SEND list, except for the ones to
    addresses to which we have already send an email"""
    j = 0
    for mail in TO_SEND:
        j = j + 1
        if mail and mail['To'] not in ALREADY_SENT:
            print("Sending the following email:")
            print(mail)

            print("This is email " + str(j) + " out of " + str(len(TO_SEND)))
            print("Sending to: " + mail['To'])
            print("Press ctrl-C to cancel...")

            for i in range(1, 10):
                print(10 - i)
                time.sleep(1)


            ##########################################################
            ## Uncomment these lines when you ACTUALLY WANT TO SEND ##
            ## THE EMAILS:                                          ##
            ##########################################################
            # s = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
            # s.starttls()
            # s.login(MY_ADDRESS, PASSWORD)
            # s.send_message(mail)
            # s.close()
            # add_to_sent(mail['To'])


            print("The message has been sent!")

            seconds = random.randint(90, 300)
            print("Sleeping for " + str(seconds) + " seconds")
            time.sleep(seconds)




if __name__ == "__main__":
    # Read the buddies, read the already sent, generate the emails and
    # send them:
    read_buddies('buddies-information.csv')
    read_already_sent(ALREADY_SENT_FILE)
    generate_emails()
    send_mails()
