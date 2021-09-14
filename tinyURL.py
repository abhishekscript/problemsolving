
# BASIC LOGIC

class TinyURL:
	def __init__(self):
		self.hashMap = {}

	def encode( self, longURL ):
		
		encoded  = hash(longURL) 
		shortURL = f'http://tinyurl.com/{encoded}'
		self.hashMap[ shortURL ] = longURL
		return shortURL

	def decode( self, shortURL ):
		return self.hashMap.get( shortURL, 404 )


obj  = TinyURL()

#ENCODE
tiny = obj.encode( 'http://codelinkster.com' )
#DECODE
print("encoded", tiny)
print("decoded", obj.decode( tiny ) )


# FULL WORKING IN-MEMORY

class TinyURL:


	def __init__(self):
		self.hashMap  =  {}
		self.dataBase =  []
		self.base62   =  [str(x) for x in range(11)]
		self.ptr 	  =  -1
		k = 0
		for x in range(26):
			self.base62.append( chr(65+x) )
			self.base62.append( chr(97+x) )

	def insert( self, longURL):
		self.dataBase.append( longURL )
		self.ptr+=1
		self.encode( self.ptr )
		return self.ptr

	def remove( self, ptr ):
		self.dataBase[ ptr ] = 404

	def encode( self, ptr ):
		
		hashCode = ''
		n = ptr
		while n!=0:
			d = n % 62
			n = n // 62
			hashCode+= self.base62[ d ] 
		print(hashCode)
		shortURL = f'http://tny.co/{hashCode}'
		self.hashMap[ shortURL  ] = self.dataBase[ ptr ]


obj = TinyURL()
for x in range(1, 200):
	result_id = obj.insert( "http://codelinkster.com/"+str(x) )





