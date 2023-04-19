const urls = [
  'http://lists-prizes.fun/?u%5C=40dwkwf&o%5C=8vkp4zm&t%5C=arc4',
  'https://datehub.life/?u=y2ykaew&o=2xzp89r&m=1&t=1504&utm_campaign=d4',
  'https://romanceroundup.life/?u=54lkaeg&o=grmpkza&m=1&t=sexxys&cid=sexxys',
  'http://landing.globify.in/wp-content/sidelightex.php?utm_campaign=rv'
];

const checkUrls = async () => {
  const maliciousUrls = [];
  const workers = [];
  for (const url of urls) {
    const worker = new Worker('worker.js');
    workers.push(worker);
    worker.postMessage(url);
    worker.onmessage = (event) => {
      const result = event.data;
      if (result !== null) {
        maliciousUrls.push(result);
      }
      worker.terminate();
    };
  }
  await Promise.all(workers.map(worker => new Promise(resolve => {
    worker.onmessage = () => resolve();
  })));
  console.log(maliciousUrls);
};

checkUrls();