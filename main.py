from fastapi import FastAPI,HTTPException
from models import Topic, Comment, session

app = FastAPI()

#/api/topic/post
@app.post("/api/create_topic/{topic}")
async def create_topic(topic: str):
    topic = Topic(topic=topic)
    session.add(topic)
    session.commit()
    return {"Message":"Topic Added"}

#/api/topic/get
@app.get("/api/retrieve_all_topics")
async def retrieve_all_topics():
    all_topics = session.query(Topic.topic).all()
    return [topic[0] for topic in all_topics]

#/api/topic/:id/get
@app.get("/api/specific_topic_retrieve/{id}")
async def specific_topic(id:int):
    specific_topic=session.query(Topic).filter(Topic.topic_id==id).first()
    if not specific_topic:
            raise HTTPException(status_code=404, detail="Topic not found")
    return {f"Topic in ID-{id}":specific_topic.topic}

#/api/topic/:id/put
@app.put("/api/specific_topic_update/{id}")
async def specific_topic_update(id:int,topic:str):
    topics_query=session.query(Topic).filter(Topic.topic_id==id).first()
    if not topics_query:
            raise HTTPException(status_code=404, detail="Topic not found")
    if topic :
        topics_query.topic=topic
    session.add(topics_query)
    session.commit()
    return {"Message":"Topic updated"}

#/api/topic/:id/delete
@app.delete("/api/specific_topic_delete/{id}")
async def specific_topic_delete(id:int):
    topic_to_delete=session.query(Topic).filter(Topic.topic_id==id).first()
    if not topic_to_delete:
            raise HTTPException(status_code=404, detail="Topic not found")
    session.delete(topic_to_delete)
    session.commit()
    return {"Message":"Topic Deleted"}

#/api/topic/:id/comment/post
@app.post("/api/comment_specific_topic/{topic}/{comment}")
async def comment_specific_topic(topic:str,comment:str):
    topics_obj=session.query(Topic).filter(Topic.topic==topic).first()
    if not topic_obj:
            raise HTTPException(status_code=404, detail="Topic not found")
    comment=Comment(comment=comment,topic=topics_obj)
    session.add(comment)
    session.commit()
    return {"Message":"Comment added"}

#/api/topic/:id/retrieve_comments_topic_id/get
@app.get("/api/retrieve_comments_topic_id/{id}")
async def retrieve_comments_topic_id(id:int):
    all_comments=session.query(Comment).filter(Comment.topic_id==id).all()
    if not all_comments:
            raise HTTPException(status_code=404, detail="Topic not found")
    return all_comments

#/api/topic/:id/comment/:id/get
@app.get("/api/retrieve_specific_topic_specific_comment/{topic_id}/{comment_id}")
async def retrieve_specific_topic_specific_comment(topic_id:int,comment_id:int):
    topic_obj=session.query(Topic).filter(Topic.topic_id==topic_id).first()
    if not topic_obj:
            raise HTTPException(status_code=404, detail="Topic_ID not found")
    comment_obj=session.query(Comment).filter(Comment.comment_id==comment_id).first()
    if not comment_obj:
            raise HTTPException(status_code=404, detail="Comment_ID not found")
    if not topic_id==comment_obj.topic_id:
            raise HTTPException(status_code=404, detail="Topic_ID is not specific to the comment_ID")
    return {topic_obj.topic:comment_obj.comment}

#/api/topic/:id/comment/put
@app.put("/api/update_specific_comment_specific_topic/{topic_id}/{comment_id}/{comment}")
async def update_specific_comment_specific_topic(topic_id:int,comment_id:int,comment:str):
    topic_obj=session.query(Topic).filter(Topic.topic_id==topic_id).first()
    if not topic_obj:
            raise HTTPException(status_code=404, detail="Topic_ID not found")
    comment_obj=session.query(Comment).filter(Comment.comment_id==comment_id).first()
    if not comment_obj:
            raise HTTPException(status_code=404, detail="Comment_ID not found")
    if not topic_id==comment_obj.topic_id:
            raise HTTPException(status_code=404, detail="Topic_ID is not specific to the comment_ID")
    comment_obj.comment=comment
    session.add(comment_obj)
    session.commit()
    return {"Message":"Comment updated"}

#/api/topic/:id/comment/delete
@app.put("/api/delete_specific_comment_specific_topic/{topic_id}/{comment_id}")
async def update_specific_comment_specific_topic(topic_id:int,comment_id:int):
    topic_obj=session.query(Topic).filter(Topic.topic_id==topic_id).first()
    if not topic_obj:
            raise HTTPException(status_code=404, detail="Topic_ID not found")
    comment_obj=session.query(Comment).filter(Comment.comment_id==comment_id).first()
    if not comment_obj:
            raise HTTPException(status_code=404, detail="Comment_ID not found")
    if not topic_id==comment_obj.topic_id:
            raise HTTPException(status_code=404, detail="Topic_ID is not specific to the comment_ID")
    session.delete(comment_obj)
    session.commit()
    return {"Message":"Comment deleted"}



