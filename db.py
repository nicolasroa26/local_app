from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from flask_sqlalchemy import SQLAlchemy

engine = create_engine('postgres://fhpebriezsuyly:576364a25eed0956440777de9005f84bd021b89d5f65817338be42fc19df35de@ec2-23-23-180-121.compute-1.amazonaws.com:5432/d6b8r5d8bu18ri')
metadata = MetaData()
formulario = Table('formulario', metadata,
    Column('post', String),
    Column('tokens', String),
    Column('groups', String),
    Column('notification', String)
)

def insert(groups, usuarios, message):
	conn = engine.connect()
	conn
	metadata.create_all(engine)
	ins = formulario.insert().values(post=str(message), tokens=str(usuarios), groups=str(groups))
	ins.compile().params
	result = conn.execute(ins)
	ins.bind = engine
	str(ins)
	result.inserted_primary_key