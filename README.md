# Aplicação de Leitura e Organização de Arquivos da Receita Federal - DIRF

Esta é uma aplicação desenvolvida em Python para realizar a leitura e organização de arquivos fornecidos pela Receita Federal, especificamente o arquivo DIRF (Declaração do Imposto de Renda Retido na Fonte). O objetivo principal é automatizar o processo de extração de informações relevantes contidas no arquivo, bem como organizar e salvar os arquivos de forma mais conveniente.

### Funcionalidades

 - Leitura de arquivo PDF: A aplicação é capaz de ler arquivos em formato PDF, mesmo que contenham um grande número de páginas. Utilizamos a biblioteca pdfplumber para extrair as informações necessárias.

 - Conversão para imagens: Os arquivos PDF são convertidos em imagens (formato JPG) utilizando a biblioteca pdf2image. Essa etapa permite processar as páginas individualmente e realizar a análise de cada uma.
 - Reconhecimento óptico de caracteres (OCR): Utilizamos a biblioteca pytesseract para extrair o texto das imagens. Isso nos permite identificar e capturar informações específicas, como CNPJ e CPF.
 - Organização e salvamento dos arquivos: Com base nas informações extraídas, os arquivos são organizados em diretórios separados para CNPJ e CPF. Além disso, eles são nomeados de acordo com o CNPJ ou CPF presente em cada um. Utilizamos as bibliotecas os e PyPDF2 para realizar essa organização e salvamento em formato PDF.

### Como utilizar
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Instale as dependências do projeto executando o comando pip install -r requirements.txt.
4. Execute o arquivo main.py para iniciar a aplicação.
5. Siga as instruções fornecidas pela interface para realizar a leitura e organização dos arquivos DIRF.

### Contribuição
Contribuições e sugestões são bem-vindas! Se você tiver alguma ideia para melhorar a aplicação ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.


Contato
Se você tiver alguma dúvida ou quiser entrar em contato, pode me encontrar no LinkedIn ou por e-mail.

LinkedIn: https://www.linkedin.com/in/guilherme-morais-a58548123/
E-mail: morais3295@gmail.com

Espero que esta aplicação seja útil e facilite o seu trabalho com os arquivos DIRF da Receita Federal. Aproveite!
