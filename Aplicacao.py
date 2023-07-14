##Para ler o arquivo pdf, split e salvar em jpg
# import module
# #from PIL import Image
# from pdf2image import convert_from_path
#
# # # Store Pdf with convert_from_path function
# images = convert_from_path('C:\\Users\\55379\Desktop\\unimed\\AutomacaoPy\\INFORMES2022_4.pdf')
# #500,poppler_path=r'C:\\Users\\55379\\Desktop\\unimed\\AutomacaoPy\\Release-22.12.0-0\\poppler-22.12.0\\Library\\bin')
# #
#
# #print(images)
# for i in range(len(images)):
#      # Save pages as images in the pdf
#      images[i].save('page' + str(i) + '.jpg', 'JPEG')
#---------------------------------------------------------

##Aplicação para ler os arquivos .JPG e salvar .pdf com o cnpj contido no arquivo. 
import cv2
import pytesseract
import os
import pdfplumber
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
#Biblioteca para utilização da funcao regex
import re
#Biblioteca para converter de pdf para imagem
import aspose.words as aw
import os.path
##C:\testeApiRota\DIRF_1
files = os.listdir("C:\\testeApiRota\\DIRF_4")

#Funcao para salvar arquivo com CPF
def salvar_aqr_cpf(img, name):        
      img = aw.Document()
      builder = aw.DocumentBuilder(img)
      builder.insert_image("C:\\testeApiRota\\DIRF_4\\"+files[i],
      aw.drawing.RelativeHorizontalPosition.MARGIN, -80, aw.drawing.RelativeVerticalPosition.MARGIN, -90, -90, -80, aw.drawing.WrapType.SQUARE)        
      if (os.path.exists('C:\\testeApiRota\\CPF\\'+name)):
         name = name + '_X'
         img.save(name + '.pdf')         
      else:
         img.save("C:\\testeApiRota\\CPF\\"+name+".pdf")         
         
#Funcao para salvar arquivo com CNPJ
def salvar_aqr_cnpj(img, name):        
      img = aw.Document()
      builder = aw.DocumentBuilder(img)
      builder.insert_image("C:\\testeApiRota\\DIRF\\"+files[i],
      aw.drawing.RelativeHorizontalPosition.MARGIN, -80,
            aw.drawing.RelativeVerticalPosition.MARGIN, -90, -90, -80, aw.drawing.WrapType.SQUARE)        
      if (os.path.exists('C:\\testeApiRota\\CNPJ\\'+name)):
         name = name + '_2'
         img.save(name + '.pdf')
         print(name+'cnpj2')
      else:
         print(name+'cnpj1')        
         img.save("C:\\testeApiRota\\CNPJ\\"+name+".pdf")

#Estutura de repetição para leitura de dos os arquivos de imagem
for i in range(len(files)):
   img = cv2.imread("C:\\testeApiRota\\DIRF_4\\"+files[i])
   pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   resultador = pytesseract.image_to_string(img)
   linhas = resultador.split('\n')
   name = linhas[15]    
   tt = linhas[9]  
   #g = linhas[42] 
   #print(linhas)         
                
   #regex para remover os numeros
   if ( linhas[0] ==  '. COMPROVANTE ANUAL DE RENDIMENTOS PAGOS OU'):
      name = linhas[15]      
      name = re.sub('[^0-9]', '', name)  
      #namepag2 = name               
      ##salvar_aqr_cpf(img, name)    
      if (name == ''):
         name = linhas[16]      
         name = re.sub('[^0-9]', '', name) 
         if (name == ''):
            name = linhas[17]      
            name = re.sub('[^0-9]', '', name)     
            #salvar_aqr_cpf(img, name)                
            print(name+'_Pt')
         elif (linhas[13] == '2. PESSOA JURIDICA BENEFICIARIA DOS RENDIMENTOS'):  
            name = linhas[16]    #Brasao              
            name = re.sub('[^0-9]', '', name)  
            #salvar_aqr_cpf(img, name)                
            print(name)                         
         else :
            #salvar_aqr_cpf(img, name)    
            print(name+'_/_')
      else :
         name = re.sub('[^0-9]', '', name)      
         #salvar_aqr_cnpj(img, name)         
         print(name+'_1') 
   
   elif (linhas[13] == '3. RELACAO DE PAGAMENTOS E RETENCOES'):  
      name = linhas[12]    #Brasao              
      name = re.sub('[^0-9]', '', name)  
      #salvar_aqr_cnpj(img, name)         
      print(name) 
   
                   
   elif (linhas[14] == '3. RELACAO DE PAGAMENTOS E RETENCOES'):  
      name = linhas[13]    #Brasao              
      name = re.sub('[^0-9]', '', name)  
      if(name == ''):
         name = linhas[12]
         name = re.sub('[^0-9]', '', name)    
         #salvar_aqr_cnpj(img, name)        
         print(name) 
      else :   
         #salvar_aqr_cnpj(img, name)       
         print(name)        
             
      #print(linhas)  
      ##salvar_aqr_cnpj(img, name)             
    
    
   elif ( linhas[14] =='CNPJ Nome completo' ):  
      name = linhas[15]   #Receita_Federal
      #name = re.sub('[^0-9]', '', name)         
     
      if(name == ''):
         name = linhas[15]
         name = re.sub('[^0-9]', '', name)   
         print(name+'_892')            
         #salvar_aqr_cnpj(img, name) 
         #print(linhas)    
      elif ( name  =='3. RELACAO DE PAGAMENTOS E RETENCOES' ):  
         name = linhas[14]   #Receita_Federal
         name = re.sub('[^0-9]', '', name)   
         #salvar_aqr_cnpj(img, name) 
         print(name+'_27')    
            
      else :
         name = re.sub('[^0-9]', '', name)   
         #salvar_aqr_cnpj(img, name) 
         print(name+'_(')       
    
      
   elif ( linhas[13] =='CNPJ Nome completo' ):  
      name = linhas[15]   #Receita_Federal
      #name = re.sub('[^0-9]', '', name)         
     
      if(name == ''):
         name = linhas[14]
         name = re.sub('[^0-9]', '', name)   
         print(name+'_62')            
         #salvar_aqr_cnpj(img, name) 
         #print(linhas)    
      elif ( name  =='3. RELACAO DE PAGAMENTOS E RETENCOES' ):  
         name = linhas[14]   #Receita_Federal
         name = re.sub('[^0-9]', '', name)   
         #salvar_aqr_cnpj(img, name) 
         print(name+'_27')    
            
      else :
         name = re.sub('[^0-9]', '', name)   
         #salvar_aqr_cnpj(img, name) 
         print(name+'_(')       
         #print(linhas)    
      #print(linhas)    
      ##salvar_aqr_cnpj(img, name)              
                                    
   elif ( tt =='Nome Empresarial CNPJ' ):  
      name = linhas[15]   #Receita_Federal
      name = re.sub('[^0-9]', '', name)   
      print(name+'_25')    
      #print(linhas)    
      #salvar_aqr_cnpj(img, name)             
         
   elif ( linhas[12] =='CNPJ Nome completo' ):  
      name = linhas[13]   #Receita_Federal
      name = re.sub('[^0-9]', '', name)   
      #salvar_aqr_cnpj(img, name) 
      print(name+'_9')    
      #print(linhas)         
      
      
   elif (name == ''):  
       
      #y2 = linhas[42]           
      #print(y)
      #print(y2)
      if(linhas[30] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cnpj(img, name) 
         print(name) 
                 
      elif(linhas[32] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cnpj(img, name) 
         print(name)  
         
         
      elif(linhas[33] == 'Pag. 2'):
         name = namepag2 +'_2' 
         print(name)        
         #salvar_aqr_cnpj(img, name)          
       
      elif(linhas[35] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)          
         print(name)   
      
 
      elif(linhas[36] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)  
         print(name)   
            
      elif(linhas[37] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)           
         print(name)      
          
 
      elif(linhas[38] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)  
         print(name)    
      
      
      elif(linhas[39] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)  
         print(name)   
      
      
      elif(linhas[40] == 'Pag. 2'):
         name = namepag2 +'_2' 
         #salvar_aqr_cpf(img, name)  
         print(name)   
      
      elif(linhas[41] == 'Pag. 2'):
         name = namepag2 +'_2' 
         print(name)                  
         #salvar_aqr_cpf(img, name)              
         
      elif(linhas[42] == 'Pag. 2'):
            name = namepag2 +'_2' 
            #print(linhas)                              
            print(name)                  
            #salvar_aqr_cpf(img, name)    
             
      #elif(len(linhas) > 47) :     
      elif( linhas[43] == 'Pag. 2'):  
            name = linhas[40]    
            name = re.sub('[^0-9]', '', name) 
            name = namepag2
            #salvar_aqr_cpf(img, name+'_2')         
            print(name)       
      
      elif( linhas[44] == 'Pag. 2'):  
            #name = linhas[40]    
            #name = re.sub('[^0-9]', '', name) 
            name = namepag2
            #salvar_aqr_cpf(img, name+'_2')                     
            print(name) 
               
               
      elif( linhas[45] == 'Pag. 2'):  
         #name = linhas[40]    
         #name = re.sub('[^0-9]', '', name) 
         name = namepag2
         #salvar_aqr_cpf(img, name+'_2')                   
         print(name) 
         
         
      elif( linhas[46] == 'Pag. 2'):  
            #name = linhas[40]    
            name = re.sub('[^0-9]', '', name) 
            name = namepag2
            #salvar_aqr_cpf(img, name+'_2')          
            print(name)                       
      
                     
      elif( linhas[47] == 'Pag. 2'):  
            name = linhas[40]    
            name = re.sub('[^0-9]', '', name) 
            name = namepag2
            #salvar_aqr_cpf(img, name+'_2')                      
            print(name)                  
                     
                 
      elif( linhas[48] == 'Pag. 2'):  
            name = linhas[40]    
            name = re.sub('[^0-9]', '', name) 
            name = namepag2
            #salvar_aqr_cpf(img, name+'_2')                      
            print(name)                              
            #salvar_aqr_cpf(img, name+'_2')       
      
      elif( linhas[16] == 'CPF Nome Completo'):  
            name = linhas[17]    
            name = re.sub('[^0-9]', '', name) 
            if(name == ''):
               name = linhas[18] 
               name = re.sub('[^0-9]', '', name) 
               #salvar_aqr_cpf(img, name+'_2')       
               print(name)            
            else :    
               #salvar_aqr_cpf(img, name+'_2')                      
               print(name)         
            #name = namepag2
            #salvar_aqr_cpf(img, name+'_2')     
                                                                               
            #salvar_aqr_cpf(img, name+'_2')        
                           
      else :   
         name = linhas[14]  
         name = re.sub('[^0-9]', '', name)     
         ##salvar_aqr_cpf(img, name)                   
         print(name+'_3', files[i]) 
         #print(linhas)       
         #salvar_aqr_cnpj(img, name+'_2')    
   
   elif ( linhas[26]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)   
   
   elif ( linhas[27]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cnpj(img, name+'_2')                            
      print(name)
      
      
   elif ( linhas[28]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cnpj(img, name+'_2')                            
      print(name)
      
   
   elif ( linhas[30]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cnpj(img, name+'_2')                            
      print(name)
         
   elif ( linhas[31]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cnpj(img, name+'_2')                            
      print(name)
   
   elif ( linhas[32]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cnpj(img, name+'_2')                            
      print(name)          
   
   elif ( linhas[33]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)  
                                               
   elif ( linhas[34]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)    
        
         
   elif ( linhas[35]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)       
                           
         
   elif ( linhas[36]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
          
   elif ( linhas[37]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)     
  
   elif ( linhas[38]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)    
  
   elif ( linhas[39]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)    
                  
   elif ( linhas[40]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
      
   elif ( linhas[41]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
    
                      
   elif ( linhas[42]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 

   elif ( linhas[43]  == 'Pag. 2'):  
      #name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
      

   elif ( linhas[44]  == 'Pag. 2'):  
      name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
      
  
   elif ( linhas[45]  == 'Pag. 2'):  
      name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)
  
  
   elif( linhas[46] == 'Pag. 2'):  
      name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name)     

   elif ( linhas[47]  == 'Pag. 2'):  
      name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 


   elif ( linhas[48]  == 'Pag. 2'):  
      name = linhas[40]    
      name = re.sub('[^0-9]', '', name) 
      name = namepag2
      #salvar_aqr_cpf(img, name+'_2')                            
      print(name) 
   
   elif(name == ""):
      #salvar_aqr_cpf(img, name+'_2')                            
      print(linhas)            
                              
   else:        
      name = re.sub('[^0-9]', '', name)     
      namepag2 = name 
      #salvar_aqr_cnpj(img, name)  
      print(name)  
         
      if(name == ""):
         name = linhas[17] 
         name = re.sub('[^0-9]', '', name)  
         #salvar_aqr_cpf(img, name)           
         print(name, files[i])              
      else : 
         #salvar_aqr_cpf(img, name)           
         #print(name,files[i]) 
      ##salvar_aqr_cpf(img, name)                                    
         print(name+'_7', files[i])