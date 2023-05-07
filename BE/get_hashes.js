const { MongoClient } = require('mongodb');

const getHashes = async (email, date) => {
  const client = new MongoClient('mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority');
  await client.connect();

  const db = client.db('test');
  const collection = db.collection('CSV');

  const query = {
    email,
    "scanned time": { $gte: new Date(date) },
  };

  const options = {
    projection: {
      _id: 0,
      sha256: 1,
    },
  };

  const result = await collection.find(query, options).toArray();

  const sha256Set = new Set(result.map(({ sha256 }) => sha256));
  const sha256List = Array.from(sha256Set);

  await client.close();

  return sha256List;
}

module.exports = getHashes;
