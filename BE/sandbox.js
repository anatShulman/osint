const headers = {
  'API-Key': 'b4cf584d-9c3d-4020-aad1-46e1d6f56894',
  'Content-Type': 'application/json'
};

const urls = [
  'http://lists-prizes.fun/?u%5C=40dwkwf&o%5C=8vkp4zm&t%5C=arc4',
  'https://datehub.life/?u=y2ykaew&o=2xzp89r&m=1&t=1504&utm_campaign=d4',
  'https://romanceroundup.life/?u=54lkaeg&o=grmpkza&m=1&t=sexxys&cid=sexxys',
  'http://landing.globify.in/wp-content/sidelightex.php?utm_campaign=rv'
];

const scanUrl = async (url) => {
  try {
    const data = {
      url: url,
      visibility: 'unlisted'
    };
    const response = await fetch('https://urlscan.io/api/v1/scan', {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(data)
    });
    const scanData = await response.json();
    await new Promise(resolve => setTimeout(resolve, 10000));
    const apiResponse = await fetch(scanData.api, {
      method: 'GET',
      headers: headers
    });
    const apiData = await apiResponse.json();
    if (apiData.verdicts.overall.malicious) {
      return `${url} is malicious: ${apiData.verdicts.overall.tags}`;
    } else {
      return null;
    }
  } catch (error) {
    console.error(error);
    return null;
  }
};

const checkUrls = async () => {
  const maliciousUrls = [];
  for (const url of urls) {
    const result = await scanUrl(url);
    if (result !== null) {
      maliciousUrls.push(result);
    }
  }
  console.log(maliciousUrls);
};

checkUrls();