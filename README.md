# Summer postcrossing scripts

These are a few helper scripts that were written in 2020 to automate
the process of matching postcrossing buddies and sending them each
others information for the summer postcrossing event of
AEGEE-Nijmegen.

## ```sendmails.py```
If you have a spreadsheet containing the matches you chose and their
full information, you can use the ```sendmails.py``` script to send
customised emails to each of the participant, informing them of the
details of their postcrossing mate.

However, to use this you should have some knowledge of programming
in python and how email works. **It is especially important to remember
that mail servers can very easily think similar messages sent in a
short time are spam, so make sure that you have adequate time outs
enabled in the script.** Also make sure to test the script without
sending the emails to see if it will be sending the correct things.

To use the ```sendmails.py``` script you should do these steps at
least:

1. Fill in the details of the email account at the top of the
  ```sendmails.py``` script.
2. If you are using a gmail account, make sure that less secure apps
   are allowed by going to https://accounts.google.com and under
   security enabling less secure apps. This is necessary for the
   script to be allowed to send emails. If you want you can disable
   this setting again after the script is done sending the emails.
3. Make sure that there is a file called ```already-sent.txt``` in the
   working directory and that it is initially empty (or only contains
   the email addresses you _don't_ want to send to, if that is
   something you want).
4. Make sure that you have your selected matches in a csv file called
   ```buddies-information.csv``` in the working directory. This file
   should as a first line contain numbers for each column, e.g. the
   first line should be something like:

   ```
   0,1,2,3,4,5,6,7,8,9,10,11,12,13
   ```
5. Make sure that the field in the ```read_buddies``` function are in
   the right order and have the right names.
6. Customise the email message in the ```generate_email``` function so
   that it contains the right information. Make sure to change both
   the plain text and the HTML versions!
7. Check the time outs in the ```send_mails``` function. For 2020 we
   had about 50 mails to send out and for this I used a time out of a
   few minutes between each email. To be on the safe side you might
   want to increase this if you are going to be sending out more
   emails.
8. Test the script and look at the emails it will be sending and how
   many there are. Do these match with what you expect? If not,
   investigate the problem.
9. If everything looks correct, uncomment the lines that actually send
   the email in the ```send_mails```.
10. Run the script again, it will now start actually sending the
    emails! If anything looks incorrect stop it by pressing
    control+c. You can also stop it after it has sent the first (few)
    mail(s) and check in the sent items of the mail account to check
    if everything looks correct.
11. After all emails have been sent, check whether everything went
    correctly. It might also be a good idea to put a message on the
    event page informing everyone that the emails have been sent out
    and telling them to contact you if they didn't receive anything,
    or they have any questions.

## ```matching.py```
This script was used to create the random matching in 2020. It is far
from optimal, so I had to tweak the matching afterwards a bit by hand
afterwards anyways.

The script expects a csv file ```emails.csv``` which contains an email
address and an email for each participant. It then tries to randomly
match these email addresses with each other so that everyone is
matched with someone from another country.

In 2020 we had the problem that more than 50% of the participants were
Dutch, so this was impossible. To get as close as possible I put in a
special case for Dutch people. After the matching was created using
this program, I manually adjusted it so that the people who were
matched with someone from the same country were at least matched with
someone from another local.

If you want to reuse this script it might be necessary to modify it
somewhat, but it probably can't hurt to try to use it.



## License
All code in this repository is free software licensed under the GNU
General Public License version 3, or (at your option) any later
version. For more details, see the COPYING file.
