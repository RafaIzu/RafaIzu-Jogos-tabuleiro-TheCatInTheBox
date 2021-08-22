from entities.entity import Session, engine, Base
from entities.consumer import Consumer

Base.metadata.create_all(engine)

session = Session()

consumer = session.query(Consumer).all()

if len(consumer) == 0:
    new_consumer = Consumer("Reimu", "reimu@hakurei.com", "123", "111")
    session.add(new_consumer)
    session.commit()
    session.close()

    consumers = session.query(Consumer).all()

print('### Consumer:')
for consumer in consumers:
    print(f"{consumer.id}: {consumer.name} | {consumer.email} | {consumer.cpf}")
