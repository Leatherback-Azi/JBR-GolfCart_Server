class Setup:
    version_no = "v1"
    version_no_route = "/" + version_no

    # SUPPORTING FORMATS - PNG, JPG, GIF, PNG, PDF, JPEG
    map_image_route = "./static/img_birchhill.png"
    map_image_fomat = "png"

class Response:
    BASE_RESPONSE = {
        "status": int(),
        "detail": str(),
        "data": {}
    }
