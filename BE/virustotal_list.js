const axios = require('axios');

const apiKey = '24e23e5e024c7298872ffa4e9c3835cd051a229584a5f280dbb41e57503b5aed';
const fileHash = '8f3184f1e508eb1394ffd94ba4062d8ee93dd095349b59ec4a5eb4563bf503fc';

axios.get(`https://www.virustotal.com/api/v3/files/${fileHash}`, {
  headers: {
    'x-apikey': apiKey
  }
})
.then(response => {
  console.log(response.data.data.attributes.reputation);

  const analysisResults = response.data.data.attributes.last_analysis_results;
  const maliciousVendors = Object.keys(analysisResults).filter(vendor => analysisResults[vendor].category === 'malicious');
  //   console.log(analysisResults);
  //   console.log(maliciousVendors);
  
  console.log(maliciousVendors.length/Object.keys(analysisResults).length);
  console.log(`${maliciousVendors.length} out of ${Object.keys(analysisResults).length}`);
})
.catch(error => {
  console.error(error);
});
