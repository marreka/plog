import os

from datetime import date
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self):
    # Non changing keys
    api_key = "AIzaSyD93XmVS5O-lZnc4Gi5RA2QAW5nuV_W5XE"
    table_id = "2710811"

    # Define map parameters
    map_center = "42.0, -30.0"
    zoom = 3
    
    today = date.today()
    # TODO(mattak): Make sure to remove the hardcoded line before going on the plane!
    today = today.replace(2012, 01, 22)
    
    formatted_day = "%s/%s/%s" % (today.month, today.day, today.year)
    
    where_condition = ''

    if today > date(2012, 01, 23):
      where_condition = "date > '01/23/2012'"
      map_center = "45.58, 8.43"
      zoom = 7

    # Render template
    template_values = {
      'api_key': api_key,
      'map_center': map_center,
      'table_id': table_id,
      'today': formatted_day,
      'where_condition': where_condition,
      'zoom': zoom,
    }
    
    path = os.path.join(os.path.dirname(__file__), 'map.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()