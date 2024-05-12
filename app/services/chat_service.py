from app.models import Chat, Message
from app import db 
from typing import Union 
import logging

def create_chat(chat_name:int) -> Union[Chat,None]:
    """ create a chat instance """
    try:
        chat = Chat(name=chat_name)
        db.session.add(chat)
        db.session.commit()
        return chat 
    except Exception as e:
        logging.error(f"Failed to create new chat instance: >> {e}")
        return 

def get_chat_by_id(chat_id:int) -> Union[Chat,None]:
    """ get chat by id """
    try:
        return Chat.query.get(chat_id)
    except Exception as e:
        logging.error(f"Querying chat error: {e}")
        return 

def get_all_chats() -> list[dict]:
    """ return all chat instances for admin """
    try:
        all_chats = Chat.query.all() # db.session.execute(db.select(Chat).order_by(Chat.id))
        chats = [chat.as_dict() for chat in all_chats]
        return chats
    except Exception as e:
        logging.error(f"{e}")
        return []

def delete_all_chats() -> bool:
    """ return true if deleting run successfully """
    try:
        db.session.query(Chat).delete()
        db.session.commit()
        return True  
    except Exception as e:
        logging.error(f"Failed to delete all chats >> \n {e}")
        db.session.rollback()  
        return False

def delete_chat_by_id(chat_id:int) -> bool:
    try:
        # Query for the chat by its ID
        chat_to_delete = db.session.query(Chat).filter_by(id=chat_id).first()
        
        if chat_to_delete:
            db.session.delete(chat_to_delete)
            db.session.commit()
            return True  
        else:
            logging.info(f"No Chat found with id: {chat_id}")
            return False  
    except Exception as e:
        logging.error(f"Failed to delete this chat >> \n {e}")
        db.session.rollback()  
        return False  

def create_message(senderName:str,content:str, chat_id:int) -> Union[Message,None]:
    """ send new message for a chat """
    try:
        # check if chat exists 
        chat = get_chat_by_id(chat_id)
        if not chat:
            logging.error("No Chat Found for this id")
            return 
        message = Message(content=content,senderName=senderName, chat_id=chat_id)
        print(f"message:{message}")
        db.session.add(message)
        db.session.commit()
        return message
    except Exception as e:
        logging.error(f"Failed to create new Message: {e}")
        return 

def get_messages_by_chat_id(chat_id:int) ->list[dict]:
    """ get  chat messages """
    try:
        all_messages = Message.query.filter_by(chat_id=chat_id).all()
        messages = [chat.as_dict() for chat in all_messages]
        return messages
    
    except Exception as e:
        logging.error("{e}")
        return []