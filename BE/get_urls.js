const { MongoClient } = require('mongodb');

const getUrls = async (email, date) => {
  const client = new MongoClient('mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority');
  await client.connect();

  const db = client.db('test');
  const collection = db.collection('CSV');

  let query = {
    "instance of": 'network connection'
  };
  if (email){
    query = {
      email,
      "scanned time": { $gte: new Date(date) },
      "instance of": 'network connection'
    };
  }

  const options = {
    projection: {
      _id: 0,
      'ip list': 1,
      'url list': 1,
    },
  };

  const result = await collection.find(query, options).toArray();

  // // for testing only, several malicious URLs
  // const URLS = [
  //   'http://lists-prizes.fun/?u%5C=40dwkwf&o%5C=8vkp4zm&t%5C=arc4',
  //   'https://datehub.life/?u=y2ykaew&o=2xzp89r&m=1&t=1504&utm_campaign=d4',
  //   'https://romanceroundup.life/?u=54lkaeg&o=grmpkza&m=1&t=sexxys&cid=sexxys',
  //   'http://landing.globify.in/wp-content/sidelightex.php?utm_campaign=rv'
  // ];
  // return URLS

  const concatenatedList = result.reduce((acc, { 'ip list': ipList, 'url list': urlList }) => {
    return [...acc, ...ipList, ...urlList];
  }, []);

  await client.close();

  // console.log(concatenatedList);
  return concatenatedList;
}

module.exports = getUrls;