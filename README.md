# 🐍 Python VG Portal Scraper

Este projeto tem como finalidade extrair informações de tickets de um dado portal de suporte utilizando técnicas de Web Scraping.

O projeto é formado por 4 scrips .py:

* "get_html_v2" alcança a página do portal de suporte, realiza o login na página, acessa, salva e retorna o código html de duas páginas distintas. Foram utilizadas as bibliotecas Selenium e BeautifulSoup. O script pode ser encontrado no link abaixo:

   -    (https://github.com/ArthurPatricio/Python_VG_portal_scraper/blob/main/get_html_v2.py)

* "scraper_incidents" realiza o "scraping" propriamente dito de um dos códigos html retornados por "get_html_v2". Além disso, salva o conteúdo "minerado" em um dataframe pandas, realiza operações de ordenação e filtragem e, retorna o dataframe. O script pode ser encontrado no link abaixo:

   -    (https://github.com/ArthurPatricio/Python_VG_portal_scraper/blob/main/scraper_incidents.py)


* "scraper_help_requests" realiza as mesmas operações feitas por "scraper_incidents" porém, para o segundo código html retornado por "get_html_v2". O script pode ser encontrado no link abaixo:

   -    (https://github.com/ArthurPatricio/Python_VG_portal_scraper/blob/main/scraper_help_requests.py)

* "run_scraper", responsável por executar toda a opereção. Recebe os dataframes retornados pelos scripts acima e os salva em uma uma planilha excel (.xlsx) em abas distintas:

   -    (https://github.com/ArthurPatricio/Python_VG_portal_scraper/blob/main/run_scraper.py)

Abaixo, pode ser encontrado um exemplo da planilha gerada ao final do processo:

   -    (https://github.com/ArthurPatricio/Python_VG_portal_scraper/blob/main/VertiGIS_Tickets.xlsx)
