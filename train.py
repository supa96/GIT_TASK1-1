class Train( Transportation ):



   def __init__( self, start, end, distance , num_station):

      Transportation.__init__( self, start, end, distance)

      self.num_station = num_station



   def find_cost( self ):

      return self.num_station * 5
