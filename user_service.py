from fastapi import FastAPI
from datetime import datetime
import hashlib
from logger_config import setup_logger

logger = setup_logger('UserService')

app = FastAPI()

@app.get("/get_user_id")
def get_user_id():
    time_str = str(datetime.now())
    user_id = hashlib.md5(time_str.encode()).hexdigest()
    logger.info(f"Generated user_id: {user_id}")
    return {"user_id": user_id}

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting UserService")
    uvicorn.run(app, host="127.0.0.1", port=8000)
