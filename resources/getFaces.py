import requests
from PIL import Image
from io import BytesIO

def download_images(num_images, save_path):
    base_url = 'https://thispersondoesnotexist.com/'
    
    for i in range(1, num_images + 1):
        url = f'{base_url}'
        response = requests.get(url)
        
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            image = Image.open(image_bytes)
            image.save(f'{save_path}/{i}.jpeg')
            print(f'Immagine {i} scaricata e salvata correttamente.')
        else:
            print(f'Errore nel scaricare l\'immagine {i}. Status Code: {response.status_code}')

if __name__ == "__main__":
    num = int(input("Inserisci il numero di facce da scaricare: "))
    download_images(num_images=num, save_path='./faces')
