from fastapi import FastAPI
from models import Review, session

app = FastAPI()


@app.post("/create")
async def create_review(topic: str, feedBack: str):
    review = Review(topic=topic, feedBack=feedBack)
    session.add(review)
    session.commit()
    return {"Topic":review.topic,"Feedback":review.feedBack}

@app.get("/")
async def get_all_topics():
    topics_query = session.query(Review.topic)  # Selecting only the 'topic' column
    return [topic[0] for topic in topics_query.all()]

@app.get("/feedBack/{topic}")
async def get_feedBack(topic: str):
    review_query = session.query(Review).filter(Review.topic == topic).all()
    return {"reviews": review_query}


@app.put("/update/{id}")
async def update_feedBack(
    id: int,
    feedBack: str = ""
):
    review_query = session.query(Review).filter(Review.id==id).first()
    if feedBack:
        review_query.feedBack = feedBack
    session.add(review_query)
    session.commit()

@app.delete("/delete/{topic}")
async def delete_topic(topic:str):
    review_query = session.query(Review).filter(Review.topic==topic).all() # Review object
    for review in review_query:
        session.delete(review)
    session.commit()
    return {"topic deleted": topic}