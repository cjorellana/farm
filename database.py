from motor.motor_asyncio import AsyncIOMotorClient

client =  AsyncIOMotorClient(' mongodb://root:example@localhost:27017')
database = client.taskdatabase
collection = database.tasks

async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task

async def get_all_task(id):
    task =[]
    cursor = await collection({})
    async for document in cursor:
        task.append(document)
    return task

async def create_task(task):
    new_task = await collection.insert_one(task)
    create_task = await collection.find_one({'_id': new_task.inserted_id})
    return create_task
