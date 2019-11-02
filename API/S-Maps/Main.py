import webapp2
from random import shuffle
import jinja2
import os
import json 


# For more searchable types please go to this link:
#     https://developers.google.com/places/supported_types

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    

class project(webapp2.RequestHandler):
     def get(self):
         project_template= the_jinja_env.get_template('project.html')

         self.response.write(project_template.render())
         
     def post(self):
        origin = self.request.get('school')
        #self.response.write(origin)
        print "**************"
        
        print origin
        myDict = {
            'key': origin
        }
        end_template = the_jinja_env.get_template('results.html')
        self.response.write(end_template.render(myDict))


class results(webapp2.RequestHandler):
    # def post(self):
    #     origin = self.request.get('school')
    #     #self.response.write(origin)
    #     print "**************"
    #     print origin
    #     myDict = {
    #         'key': origin
    #     }
    #     end_template = the_jinja_env.get_template('results.html')
    #     self.response.write(end_template.render(myDict))
    def get(self):
        latLong = "{lat: 36.598339, lng : -121.896431}"
        myDict = {
             'key': unicode(latLong,"utf-8")
         }
         
        maps = the_jinja_env.get_template('map.html')
        self.response.write(maps.render(myDict))
		
app = webapp2.WSGIApplication([
     ('/', results),
    #  ('/results', results),
 ], debug=True)
