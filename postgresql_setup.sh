#!/bin/bash

## PostgrSQL Installation 

sudo apt update

sudo apt install postgresql postgresql-contrib

#sudo -i -u postgres

#psql

set -e
DB_NAME=${1:-accis_test_new_1234}
DB_USER=${2:-my_db_1234}
DB_USER_PASS=${3:-accis_test@123}
sudo su postgres <<EOF
createdb  $DB_NAME;
psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_USER_PASS';"
psql -c "grant all privileges on database $DB_NAME to $DB_USER;"
echo "Postgres User '$DB_USER' and database '$DB_NAME' created."
EOF
