import argparse
from pathlib import Path
from flask import Flask, jsonify, request
from flask_swagger import swagger


def create_app(project_dir: Path):
    # create the app
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/mappings", methods=["GET"])
    def get_mappings():
        """
        Get the available mappings
        Returns a list with all mappings, including the name and the url to access it.
        ---
        produces:
          - application/json
        responses:
          200:
            description: Available mappings
        """
        return {"123": {"name": "example-mapping", "url": "/mapping/123"}}, 501

    @app.route("/mapping/<id>", methods=["GET"])
    def get_mapping(id: str):
        """
        Get a specific mapping
        Returns the mapping with the given id. This includes all details like classifications, presences in profiles, etc.
        ---
        produces:
          - application/json
        parameters:
          - in: path
            name: id
            type: string
            required: true
            description: The id of the mapping
        responses:
          200:
            description: The mapping with the given id
          404:
            description: Mapping not found
        """
        return {
            "id": id,
            "name": "example-mapping",
            "fields": {"name": {"classification": "use"}},
        }, 501

    @app.route("/mapping/<id>/fields", methods=["GET"])
    def get_mapping_fields(id: str):
        """
        Get the fields of a mapping
        Returns a brief list of the fields
        ---
        produces:
          - application/json
        parameters:
          - in: path
            name: id
            type: string
            required: true
            description: The id of the mapping
        responses:
          200:
            description: The fields of the mapping
          404:
            description: Mapping not found
        """
        return {"id": id, "fields": {"name": {}}}, 501

    @app.route("/mapping/<mapping_id>/field/<field_id>", methods=["POST"])
    def post_mapping_field(mapping_id: str, field_id: str):
        """
        Post a manual entry for a field
        Overrides the default classification of a field. A field can target a field with the same name or a different one to map the field, can point to 'null' to ignore it or can be set to a fixed value
        ---
        consumes:
          - application/json
        parameters:
          - in: path
            name: mapping_id
            type: string
            required: true
            description: The id of the mapping
          - in: path
            name: field_id
            type: string
            required: true
            description: The id of the field
          - in: body
            name: body
            schema:
              properties:
                target:
                  type: string
                  description: The target field
                fixed:
                  type: string
                  description: Fixed value to assign to the field
        responses:
          200:
            description: The field was updated
          404:
            description: Mapping or field not found
        """
        print(request.get_json())
        return "", 501

    @app.route("/spec", methods=["GET"])
    def spec():
        swag = swagger(app)
        swag["info"]["version"] = "1.0"
        swag["info"]["title"] = "Structure Comparer"
        return jsonify(swag)

    return app


def get_args():
    parser = argparse.ArgumentParser(
        description="Compare profiles and generate mapping"
    )

    parser.add_argument(
        "--project-dir",
        type=Path,
        help="The project directory containing the profiles and config",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    app = create_app(project_dir=args.project_dir)
    app.run()
