import json
import pymongo
import sys, getopt

def read_cases_data(file):
    return json.loads(open(file,'r').read())

def create_import(file,type):
    data = read_cases_data(file)
    for label in data['cases'][0]:
      value = data['cases'][0][label]
      print ("curl -s -X POST https://corona.9it.eu/api/v1/corona/" + type + "/" + label + "/" + value )
      # print ("curl -s -X POST http://localhost:4006/api/v1/corona/" + type + "/" + label + "/" + value )

def main(argv):
  inputfile = ''
  type = ''
  try:
    opts, args = getopt.getopt(argv,"hi:t:",["ifile=","type="])
  except getopt.GetoptError:
    print 'test.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -i <inputfile> '
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-t", "--type"):
      type = arg
  if inputfile != str(""):
    print 'Input file is "',inputfile,'""'
    create_import(inputfile,type)
  else:
    print 'kein Input file angegeben!'

if __name__ == "__main__":
   main(sys.argv[1:])
