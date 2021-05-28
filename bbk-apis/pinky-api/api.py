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
    input_list_to_use = request.args.get('input')
    #build manifest
    #kube del
    #kube apply
    build_manifest(pinky_script, bbs_project_id, bbs_project_code, input_list_to_use)
    #subprocess.call(['/bin/bash', '/bbk-app/bbk-apis/pinky-api/run_pinky_script.sh', pinky_script, bbs_project_id, bbs_project_code, input_list_to_use])
    return "<h1>PINKY</h1><p>pinky starting: %s </p>"%pinky_script
  
def build_manifest(pinky_script, bbs_project_id, bbs_project_code, input_list_to_use):
    manifest_template = "/bbk-app/process-manifests/"+pinky_script
    project_manifest_filepath = "/bbk-app/project-data/"+bbs_project_code+"/manifests/bah.yaml"
    template_content = ""
    with open(manifest_template) as f:
        template_content = f.read()
        print(template_content)
    
    project_manifest_content = template_content.replace("TASK_NAME", bbs_project_code).replace("BBS_PROJECT_ID", bbs_project_id).replace("BBS_PROJECT_CODE", bbs_project_code).replace("BBS_PROJECT_LIST", input_list_to_use)
        
    with open(project_manifest_filepath, "w") as text_file:
        text_file.write(project_manifest_content)


