import os
from datetime import datetime
from src.utils.db_operation import DB
from src.utils.utils import load_recognise, text_to_speech, detect_face
from dotenv import load_dotenv
load_dotenv()

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}
date = datetime.utcnow()
current_time = datetime.now().strftime("%H:%M:%S")
#recognizer, labels = load_recognise()
#engine, rate = text_to_speech()
#face_cascade, cap = detect_face()

if __name__ == "__main__":
    db = DB(db_config)

    # example
    query = 'select * from Customer'
    response = db.read(query)
    print (response)



    ### CLEAR MEMORY WITH CAP.RELEASE() IF YOU USE IT HERE

    #cap.release()