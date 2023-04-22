const axios = require('axios');

const scanHash = async (fileHash) => {
  try {
    axios.get(`https://www.virustotal.com/api/v3/files/${fileHash}`, {
      headers: {
        'x-apikey': '24e23e5e024c7298872ffa4e9c3835cd051a229584a5f280dbb41e57503b5aed'
      }
    })
    .then(response => {
      const analysisResults = response.data.data.attributes.last_analysis_results;
      const maliciousVendors = Object.keys(analysisResults).filter(vendor => analysisResults[vendor].category === 'malicious');
      //   console.log(analysisResults);
      //   console.log(maliciousVendors);
       
      const res = {
        sha256: fileHash,
        reputation: response.data.data.attributes.reputation,
        malicious: maliciousVendors.length/Object.keys(analysisResults).length,
        log: `${maliciousVendors.length} out of ${Object.keys(analysisResults).length} security vendors detected this file as malicious`
      };
      console.log(res);
      return res;
    })
    .catch(error => {
      console.error(error);
      return null;
    });
  } catch (error) {
    console.error(error);
    return null;
  }
};

const checkHashes = async (hashes) => {
  const maliciousHashes = [];
  const promises = hashes.map(async (hash) => {
    const result = await scanHash(hash);
    if (result !== null) {
      maliciousHashes.push(result);
    }
  });
  await Promise.all(promises);
  console.log(maliciousHashes);
};

module.exports = checkHashes;
