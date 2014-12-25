import json;

def load_strings(pagename):
       with open('static/strings/' + pagename + '.json') as stringfile:
           
           return json.load(stringfile)