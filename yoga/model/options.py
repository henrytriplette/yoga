DEFAULT_OPTIONS = {
        "output_format": "glb",             # glb|gltf
        "no_graph_optimization": False,
        "no_meshes_optimization": False,
        "no_textures_optimization": False,
        }


def normalize_options(options=None):
    if not options:
        return dict(DEFAULT_OPTIONS)

    result = dict(DEFAULT_OPTIONS)

    # "GLB" -> "glb" (lower case)
    if "output_format" in options:
        value = options["output_format"].lower()

        if value not in ("gltf", "glb"):
            raise ValueError("Invalid value for 'output_format': '%s'" % value) # noqa

        result["output_format"] = value

    # Optimization flags
    for key in ("no_graph_optimization", "no_graph_optimization",
                "no_graph_optimization"):
        if key in options:
            result[key] = bool(options[key])

    return result


def extract_image_options(options=None):
    if not options:
        return None

    result = dict()

    for key in options:
        if key.startswith("image_"):
            result[key[6:]] = options[key]

    return result
