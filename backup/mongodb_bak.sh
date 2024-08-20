#! /bin/bash

# MongoDB Atlas
MONGO_URL="mongodb+srv://thomasleong:8zvnWrT3sf8N2u7x@cluster0.ef0wowh.mongodb.net"
DATABASE_NAME="Thomas"
COLLECTION_NAME="Night_Database"

# Get the current date
DATE=$(date +"%Y_%m_%d") 

# Define the output file path
OUTPUT_FILE="/Users/n02-19/Desktop/Night_Water/backup/${DATE}.csv"

# Define the fields to export (no spaces in the list)
FIELDS="_id,Ven_Machine,Credit,Unit,Secure_Credit,Report" # Do not put space, else not working lol"

# Run mongoexport
mongoexport --uri="${MONGO_URL}/${DATABASE_NAME}" --collection=${COLLECTION_NAME} --type=csv --fields=${FIELDS} --out="${OUTPUT_FILE}"

echo "Data exported to ${OUTPUT_FILE}"
