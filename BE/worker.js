const headers = {
    'API-Key': 'b4cf584d-9c3d-4020-aad1-46e1d6f56894',
    'Content-Type': 'application/json'
  };
  
const scanUrl = async (url) => {
  try {
    const data = {
      url: url,
      visibility: 'public'
    };
    const response = await fetch('https://urlscan.io/api/v1/scan', {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(data)
    });
    const scanData = await response.json();
    await new Promise(resolve => setTimeout(resolve, 5000));
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

onmessage = async (event) => {
  const url = event.data;
  const result = await scanUrl(url);
  postMessage(result);
};