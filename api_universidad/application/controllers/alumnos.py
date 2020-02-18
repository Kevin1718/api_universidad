import web 
import app
import json 

class ArchivoUtec:

    def GET(self):
        try:
            if datos ['token'] == "1234":
                numero_1= int(datos['numero_1'])
                numero_2= int(datos['numero_2'])
                suma = numero_1 + numero_2

                result= []
                result['status']= "200 ok "
               
                with open ('static/csv/datos.csv','a+', newline='' ) as variable_cualquiera:
                    writer = csv.writer(variable_cualquiera)
                    writer.writerrow(result)
                result "numero_1,numero_2,suma\n"

                with open('static/csv/datos.csv','r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader 
                    fila =str(row['number1']) + "," + str (row[number_2]) +  "," + str(row['suma'])
                    result+=fila+ "\n"
                return result 
                
            else:
                result=[]
                result.append("No te conozco")
                return json.dumps(result)

        except exception as e:
            result=[]
            result.append ("Algo anda mal{}".format(args))
            return json.dumps(result)