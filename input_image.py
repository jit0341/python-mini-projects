import requests
import os

api_key = 'kNCAvwwY2jYHFvq1db97Q7w6'
input_folder = '/storage/emuliated/0/input_images'
output_folder = '/storage/emulated/0/output_images_white_bg'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '_white.png')

        with open(input_path, 'rb') as file:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': file},
                data={'size': 'auto', 'bg_color': 'white'},
                headers={'X-Api-Key': api_key},
            )

        if response.status_code == requests.codes.ok:
            with open(output_path, 'wb') as out:
                out.write(response.content)
            print(f"✅ Processed: {filename}")
        else:
            print(f"❌ Failed: {filename} – {response.status_code}, {response.text}")
