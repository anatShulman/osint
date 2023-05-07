const axios = require('axios');

const scanHash = async ({ sha256, name, path, instance }) => {
  try {
    const response = await axios.get(`https://www.virustotal.com/api/v3/files/${sha256}`, {
      headers: {
        'x-apikey': '24e23e5e024c7298872ffa4e9c3835cd051a229584a5f280dbb41e57503b5aed'
      }
    });
    const analysisResults = response.data.data.attributes.last_analysis_results;
    const maliciousVendors = Object.keys(analysisResults).filter(vendor => analysisResults[vendor].category === 'malicious');

    const res = {
      sha256,
      reputation: response.data.data.attributes.reputation,
      malicious: maliciousVendors.length/Object.keys(analysisResults).length,
      path: path,
      name: name,
      instance: instance,
      // log: `${maliciousVendors.length} out of ${Object.keys(analysisResults).length} security vendors detected this file as malicious`
    };
    return res;
  } catch (error) {
    console.error(error);
    return null;
  }
};

const checkHashes = async (hashes) => {
  const maliciousHashes = [];
  const promises = hashes.map(async ({ sha256, name, path, instance }) => {
    const result = await scanHash({ sha256, name, path, instance });
    if (result !== null) {
      if (result.malicious > 0 || result.malicious < 0){  
        maliciousHashes.push(result);
      }
    }
  });
  await Promise.all(promises);

  // Remove duplicate dictionaries
  const uniqueMaliciousHashes = [...new Set(maliciousHashes.map(JSON.stringify))].map(JSON.parse);

  return uniqueMaliciousHashes;
};

module.exports = checkHashes;