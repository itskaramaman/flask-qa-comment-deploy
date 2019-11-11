from main import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	title = db.Column(db.String(255), nullable=False)
	content = db.Column(db.Text, nullable=False)
	# posted_on = db.Column(db.DateTime, nullable=False)
	
	def __init__(self, title, content):
		self.title = title
		self.content = content

		
	def __repr__(self):
		return "<Post(id=%s, title=%s, content=%s)>" % (
			self.id, self.title, self.content)		
