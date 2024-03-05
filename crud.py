from model import db, Item, connect_to_db

def create_table():
    db.create_all()

def create_item(name):
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()

def update_item(name):
    item = Item.query.filter_by(name=name).first()
    if item:
        item.votes += 1
        db.session.commit()
    else:
        # Handle case where item with given name does not exist
        pass

def select_all_items():
    items = Item.query.all()
    return items
 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


# TODO error handling