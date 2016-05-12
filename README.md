# codeAllTheThings

TO INSTALL THE WEB FOLLOW THE STEPS LISTED HERE:
http://elinux.org/RPi_webserver

For this test I used a root mysql database with password root99.

Once everything is setup/install properly mv the piweb folder to /var/www/html/
Make sure all your permissions are www-data:www-data and 755

You should be able to then go to localhost/piweb/ and see a chart render

*IMPORTANT*
The step in the readme where you install php, sql, and cgi it says you can install all 3 in one command. That does not work and you will need to install each one one at at time.

When you install the sqlLite data base it will ask you for a password I used root99 and user root.
For the same code I have I created a blank data base called Test, this will need to be updated to the real database we create for the pi project.
