#-------------------------------------------------------------------------------
# Name:        makeTempsSQL
# Purpose:     Convert my values from the CSV to valid SQL INSERT statements
#              This script and the data will be used as examples in-class.
#
#              Perhaps later we should consider scripting with a direct MySQL
#              connection, but this is an iterative process to build up to that.
#
# Author:      Ben Rehberg, github@rtech.co
#
# Created:     06/29/2013
# Copyright:   (c) bmrehberg 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
import csv
def main():
    of = open('inserts.sql', 'w')
    of.write('-- INSERT statements created by makeTempsSQL\n\n')
    with open('temps.csv', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        for row in f:
            of.write('INSERT INTO temps (temptime, temp_c) VALUES (\'{}\', {});\n'.format(row[0], row[1].strip()))
    of.close()

if __name__ == '__main__':
    main()
