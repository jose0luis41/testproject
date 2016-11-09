from flask import Flask, request, abort
import os, json

from files_commands import get_files, remove_all_files, get_files_recent

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url + '/files', methods=['POST'])
def create_file():
  content = request.get_json(silent=True)
  filename = content['filename']
  content = content['content']
  os.chdir('files_created')
  result = open(filename+'.txt','a')
  result.write(content+'\n')
  result.close()
  os.chdir('..')
  return "CREATED",201

@app.route(api_url + '/files', methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_files()
  return json.dumps(list), 200

@app.route(api_url + '/files', methods=['PUT'])
def update_file():
  return "NOT FOUND", 404
  
@app.route(api_url + '/files', methods=['DELETE'])
def delete_file():
  error = False
  error = remove_all_files()
  if error:
    return 'REMOVE ALL FILES', 200
  else:
    return 'ERROR', 400

@app.route(api_url + '/files/recently_created', methods=['POST'])
def create_file_recent():
  return "NOT FOUND", 404
  
@app.route(api_url + '/files/recently_created', methods=['GET'])
def read_file_recent():
  list = {}
  list["files"] = get_files_recent()
  return json.dumps(list), 200
  
@app.route(api_url + '/files/recently_created', methods=['PUT'])
def update_file_recent():
  return "NOT FOUND", 404
  
@app.route(api_url + '/files/recently_created', methods=['DELETE'])
def delete_file_recent():
  return "NOT FOUND", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9090, debug='True')
