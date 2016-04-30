from datetime import datetime
import json
import logging
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import relationship, backref
from sqlalchemy.exc import OperationalError

from . import Base, session, to_dict

logger = logging.getLogger(__name__)

# Define the framework table
class Framework(Base):
	__tablename__ = 'framework'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)

# Query for frameworks
def get_framework(framework_id):
	query = None
	results = []

	if framework_id == None:
		query = session.query(Framework)
	else:
		query = session.query(Framework).filter(Framework.id==framework_id)

        for result in query.all():
		results.append(to_dict(result))

	return results
