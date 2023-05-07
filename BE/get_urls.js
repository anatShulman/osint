const { MongoClient } = require('mongodb');

const getUrls = async (email, date) => {
  const client = new MongoClient('mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority');
  await client.connect();

  const db = client.db('test');
  const collection = db.collection('CSV');

  const query = {
    email,
    "scanned time": { $gte: new Date(date) },
    "instance of": 'network connection'
  };

  const options = {
    projection: {
      _id: 0,
      'ip list': 1,
      'url list': 1,
    },
  };

  const result = await collection.find(query, options).toArray();

  const concatenatedList = result.reduce((acc, { 'ip list': ipList, 'url list': urlList }) => {
    return [...acc, ...ipList, ...urlList];
  }, []);

  await client.close();

  // console.log(concatenatedList);
  return concatenatedList;
}

module.exports = getUrls;