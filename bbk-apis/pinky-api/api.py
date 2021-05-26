# Copyright 2021 Bugbound

from flask import Flask, request
import subprocess

app = Flask(__name__)

app.config.from_object('settings')
app.url_map.strict_slashes = False

@app.route('/')
def hello():
  return "<h1>BBS PINKY API</h1><a href='/start_pinky?pinkyscript=discovery/assetfinder.yaml.template&project_id=1&project_code=tesla'>Pinky Tesla Runner</a>"


@app.route('/start_pinky')
def start_pinky():
  pinky_script = request.args.get('pinkyscript')
  bbs_project_id = request.args.get('project_id')
  bbs_project_code = request.args.get('project_code')
  subprocess.call(['/bin/bash', '/bbk-app/bbk-apis/pinky-api/run_pinky_script.sh', pinky_script, bbs_project_id, bbs_project_code])
  return "<h1>PINKY</h1><p>pinky starting: %s </p>"%pinky_script
  
  


