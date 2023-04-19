const headers = {
  'API-Key': 'b4cf584d-9c3d-4020-aad1-46e1d6f56894',
  'Content-Type': 'application/json'
};

const urls = ['http://lists-prizes.fun/?u%5C=40dwkwf&o%5C=8vkp4zm&t%5C=arc4'];
const maliciousUrls = [];

urls.forEach((url) => {
    const data = {
        url: url,
        visibility: 'public'
    };
    fetch('https://urlscan.io/api/v1/scan', {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        setTimeout(() => {
            fetch(data.api, {
                method: 'GET',
                headers: headers
            })
            .then(response => response.json())
            .then(data => {
                if (data.verdicts.overall.malicious){
                    const message = `${url} is malicious: ${data.verdicts.overall.tags}`;
                    console.log(message);
                    maliciousUrls.push(message);
                }
                else{
                    console.log(`${url} is not malicious`);
                }
                });
            }, 10000); // wait for 10 seconds before sending GET request
        })
        .catch(error => {
            console.error(error);
        });
});

console.log(maliciousUrls);