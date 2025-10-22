import requests
from bs4 import BeautifulSoup
from slugify import slugify
import veeries.io as vio


class Download_File():
    def __init__(self):
        self.url = "https://cepa.epagri.sc.gov.br/index.php/mercado-agricola/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
        }
        self.save_path = r"C:\Users\Public\cepa_epagri_preco_insumos_fatores_producao\{}.xlsx"
        self.texto_alvo = "Preços dos insumos e fatores de produção"
            
    def get_download_link(self):
        '''
            Scrapping cepa.epagri website to get download link and filename
        '''
        response = requests.get(self.url, headers=self.header)
        
        response.raise_for_status()
        
        html_content = response.text
        filename = "teste"
        
        soup = BeautifulSoup(html_content, 'html.parser')

        link_tag = soup.find('a', text=self.texto_alvo)

        if link_tag and link_tag.get('href'):
            download_link = link_tag.get('href')
            print(f"Link (href): {download_link}")
        else:
            print(f"Erro: Não foi possível encontrar o link com o texto:{self.texto_alvo}")

        return download_link, filename
    
    def download_file(self):
        '''
            Downloading last available file and saving it
        '''
        download_link, filename = self.get_download_link()

        req_download = requests.get(download_link, headers=self.header)

        output = vio.python.open(self.save_path.format(filename), 'wb')
        output.write(req_download.content)
        output.close()

    def run_process(self):
        print("--- Downloading last avaliable file ---")

        self.download_file()

        print("--- File downloaded ---")

if __name__ == "__main__":
    Download_File().run_process()
