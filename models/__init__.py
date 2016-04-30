import json
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ccaf.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Utility function to return dictionary of kv pairs from SqlAlchemy query results.
def to_dict(result):
	if result:
		resdict = result.__dict__.copy()
		for key,val in resdict.items():
			if key.startswith("_") or key == "metadata":
				resdict.pop(key,None)
				continue
			try:
				json.dumps(result.__getattribute__(key))
			except:
				resdict.pop(key,None)
                                continue
		return resdict
