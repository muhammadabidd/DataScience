# Import the scrapy library
import scrapy

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = 'https://www.datacamp.com', callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css( 'p.course-block__author-name::text' ).extract()
    # Here we will just return the list of Authors
    return author_names
  
