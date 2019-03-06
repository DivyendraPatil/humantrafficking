import cherrypy
import io
import os

import numpy as np
import tensorflow as tf
import label_image as li

class MelCheck():
    
    def __init__(self):
        self.users = [user.strip('\n') for user in open('users.txt', 'r')]
        self.usr_div1 = '<li class="mdl-menu__item"><a href="get_user?user='
        self.usr_div2 = '</a></li>'
        self.usrsdiv = [self.usr_div1 + usr + '">' + usr + self.usr_div2 for usr in self.users]
        self.topp1 = ''.join([line for line in open('toppart.html', 'r')])
        self.topp2 = ''.join([line for line in open('toppart2.html', 'r')])
        self.botp = ''.join([line for line in open('belowpart.html', 'r')])
        self.cm = {'msk 1': 'Mole 1','msk 2': 'Mole 2','malignant': 'High risk','clearskin':'Clear Skin'}
        
    def save_user(self, user):
        fw = open('users.txt', 'a')
        fw.write('\n'+user)
        fw.close()
        self.users.append(user)
        self.usrsdiv.append(self.usr_div1 + user  + '">'+ self.usr_div2)
        
    def get_user_files(self, user):
        mypath = "./images/usr/"+user+"/"
        onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and '.DS' not in f]
        if onlyfiles:
            return onlyfiles
        return []
        
    def get_top(self):
        return self.topp1 + ''.join(self.usrsdiv) + self.topp2

    @cherrypy.expose
    def get_user(self, user):
        try:
            data = self.get_top()
            data += '<font size="4"><text>History of '+user+'</text></font>            <br>            <br><div class="row">'
            user = user.lower()
            uf = self.get_user_files(user)
            if len(uf) > 0:
                for i in range(int((len(uf)/6)+1)):
                    data += '<div class="column">'
                    for j in uf[i*6:(i+1)*6]:
                        data += '<img width="350px" src="images/usr/'+user+'/' + j + '">'
                    data += '</div>'
            data += self.botp
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"

    @cherrypy.expose
    def index(self):
        try:
            data = self.get_top() + ''.join([line for line in open('index.html', 'r')])
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"

    @cherrypy.expose
    def MSK1(self):
        try:
            data = self.get_top() + ''.join([line for line in open('MSK1.html', 'r')])
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"
            
    @cherrypy.expose
    def MSK2(self):
        try:
            data = self.get_top() + ''.join([line for line in open('MSK2.html', 'r')])
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"
            
    @cherrypy.expose
    def Malignant(self):
        try:
            data = self.get_top() + ''.join([line for line in open('Malignant.html', 'r')])
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"
            
    @cherrypy.expose
    def ClearSkin(self):
        try:
            data = self.get_top() + ''.join([line for line in open('ClearSkin.html', 'r')])
            return data
        except:
            return "<html><body><h1>Load form for Mel Check</h1></body></html>"

    @cherrypy.expose
    def about(self):
        try:
            data = self.get_top() + ''.join([line for line in open('about.html', 'r')])
            return data
        except:
            return "<html><body><h1>about page</h1></body></html>"

    @cherrypy.expose
    def services(self):
        try:
            data = self.get_top() + ''.join([line for line in open('services.html', 'r')])
            return data
        except:
            return "<html><body><h1>Services page</h1></body></html>"
            
    @cherrypy.expose
    @cherrypy.tools.accept(media='multipart/form-data')
    def send_to_doc(self, fileToUpload, fileName, user, submit):
        try:
            if user not in self.users:
                self.save_user(user)
            
            img = open(user+'/'+fileName, 'wb')
            img.write(io.BytesIO(fileToUpload.file.read()).read())
            img.close()
        except:
            pass
        return "200"

    @cherrypy.expose
    @cherrypy.tools.accept(media='multipart/form-data')
    def check(self, fileToUpload, submit):
        try:
            res = "<html><body><h1>Test Result</h1>"
            res_var = None
            if fileToUpload:
                file_name = "uploads/1.jpg"

                img = open(file_name, 'wb')
                img.write(io.BytesIO(fileToUpload.file.read()).read())
                img.close()

                model_file = "output_graph.pb"
                label_file = "output_labels.txt"
                input_height = 299
                input_width = 299
                input_mean = 0
                input_std = 255
                input_layer = "Mul"
                output_layer = "final_result"

                graph = li.load_graph(model_file)
                t = li.read_tensor_from_image_file(
                       file_name,
                       input_height=input_height,
                       input_width=input_width,
                       input_mean=input_mean,
                       input_std=input_std)

                input_name = "import/" + input_layer
                output_name = "import/" + output_layer
                input_operation = graph.get_operation_by_name(input_name)
                output_operation = graph.get_operation_by_name(output_name)

                with tf.Session(graph=graph) as sess:
                    results = sess.run(output_operation.outputs[0], {
                              input_operation.outputs[0]: t
                    })
                results = np.squeeze(results)

                top_k = results.argsort()[-5:][::-1]
                labels = li.load_labels(label_file)
                if results[top_k[0]] > 0.7:
                    res += "<h3>You uploaded image of " + self.cm[str(labels[top_k[0]])] + ' ' + str(results[top_k[0]] * 100) +  "%</h3>"
                    res_var = '\n Probability of ' + self.cm[str(labels[top_k[0]])] + ' = ' + str(results[top_k[0]] * 100) +  "%"
                else:
                    res += "<h3>Sorry couldn't detect<br>Try with different image</h3>"

            try:
                data = self.get_top()
                res1 = ''.join([line for line in open('result1.html', 'r')])
                res2 = ''.join([line for line in open('result2.html', 'r')])

                resm = "<img src=\"uploads/1.jpg\" width=\"400\"  >" + "<h1 class=\"mb-10\"> \n Our Result:</h1>" + "<p>" + res_var + "</p>"

                return data + res1 + resm + res2
            except Exception as e1:
                print(e1)
                return res + "<a href='/'>Try another</a></body></html>"
        except Exception as e:
            print(e)
            return "<html><body><h1>Please try again (Corrupt or invalid Image)</h1></body></html>"


if __name__=="__main__":
    conf = {
        '/' : {
            'tools.sessions.on' : True,
            'tools.staticdir.root' : os.path.abspath(os.getcwd())
        },
#        '/js' : {
#            'tools.staticdir.on' : True,
#            'tools.staticdir.dir' : './js'
#        },
#        '/css' : {
#            'tools.staticdir.on' : True,
#            'tools.staticdir.dir' : './css'
#        },
#        '/fonts' : {
#            'tools.staticdir.on' : True,
#            'tools.staticdir.dir' : './fonts'
#        },
        '/Melanoma' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : './Melanoma'
        },
        '/images' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : './images'
        },
        '/uploads' : {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : './uploads'
        }
    }

    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port' : 11111})
    cherrypy.quickstart(MelCheck(), "/", conf)

