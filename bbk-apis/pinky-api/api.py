# Copyright 2021 Bugbound

from flask import Flask, request
import subprocess
import os


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
    project_manifest_filepath = build_manifest(pinky_script, bbs_project_id, bbs_project_code, input_list_to_use)
    #try kill the job if its already running...
    subprocess.call(['kubectl', 'delete', '-f', project_manifest_filepath])
    #run the job
    subprocess.call(['kubectl', 'apply', '-f', project_manifest_filepath])
    return "<h1>PINKY</h1><p>pinky starting: %s </p>"%project_manifest_filepath
  
def build_manifest(pinky_script, bbs_project_id, bbs_project_code, input_list_to_use):
    manifest_template = "/bbk-app/process-manifests/"+pinky_script
    head, tail = os.path.split(manifest_template)
    new_filename = tail.replace(".template","")
    project_manifest_filepath = "/bbk-app/generated-manifests/"+new_filename
    template_content = ""
    with open(manifest_template) as f:
        template_content = f.read()
        print(template_content)
    
    project_manifest_content = template_content.replace("TASK_NAME", bbs_project_code).replace("BBS_PROJECT_ID", bbs_project_id).replace("BBS_PROJECT_CODE", bbs_project_code).replace("BBS_PROJECT_LIST", input_list_to_use)
        
    with open(project_manifest_filepath, "w") as text_file:
        text_file.write(project_manifest_content)
        
    return project_manifest_filepath


