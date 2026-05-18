from File_Uploads.upload_download import upload_file, download_file
import os

def test_upload():
    res = upload_file()

    json_data = res.json()

    assert res.status_code == 200
    assert json_data["form"]["user_id"] == "123"
    assert "file" in json_data["files"]

import os

def test_download():
    res = download_file()

    assert res.status_code == 200
    assert res.headers["Content-Type"] == "image/png"

    # Check file exists
    # assert os.path.exists("downloaded.png")

    # Check file size
    # assert os.path.getsize("downloaded.png") > 0