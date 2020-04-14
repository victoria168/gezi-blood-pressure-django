#!/bin/bash
# Install PostgreSQL for MMS on Ubuntu 18.04 LTS and configure MMS database, create user for Django, and update connection parameters
# Instructions:
#   1. Configure the database's name and setup a username and password below
#   2. Run this shell script with './install_db.sh'
#   3. If everything ran successfully, reboot (don't shutdown, otherwise the public IP will change) the EC2 instance on the AWS console

#################################### Config ####################################

# Set database name, username, and password here
DATABASENAME=gezi_db
DBUSERNAME=geziadmin
DBPASSWORD=secret


################################## Configuration ###############################

# Create database and user for Django
sudo -u postgres psql -c "CREATE DATABASE $DATABASENAME;"
sudo -u postgres psql -c "CREATE USER $DBUSERNAME WITH PASSWORD '$DBPASSWORD';"

# Update connection parameters (required for Django)
sudo -u postgres psql -c "ALTER ROLE $DBUSERNAME SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE $DBUSERNAME SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $DBUSERNAME SET timezone to 'UTC';"

# Grant user permission to access the database table
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DATABASENAME TO $DBUSERNAME;"
