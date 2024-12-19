from flask import Blueprint, request, jsonify, json
from app.controllers.converter_controller import json_to_xml, prettify_xml
import os

main = Blueprint('main', __name__)

@main.route('/convert', methods=['POST'])
def convert_json_to_xml():
    if 'files' not in request.files:
        return jsonify({"error": "No files part"}), 400

    files = request.files.getlist('files')
    converted_files = []

    for file in files:
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file and file.filename.endswith('.json'):
            json_data = file.read()
            try:
                json_obj = json.loads(json_data)
                xml_elem = json_to_xml(json_obj)
                pretty_xml_as_string = prettify_xml(xml_elem)

                # Armazena o XML convertido em uma lista com o nome do arquivo
                converted_files.append({
                    "filename": f"{os.path.splitext(file.filename)[0]}.xml",
                    "content": pretty_xml_as_string
                })
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": f"Invalid file type for {file.filename}"}), 400

    return jsonify({"converted_files": converted_files}), 200