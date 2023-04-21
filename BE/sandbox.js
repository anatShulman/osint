const checkUrls = require('./urlscan_list.js');
const getUrls = require('./get_urls.js');

// here we want to get the current email and date from Agent.exe,
// after being notified that a scan had occured of the URLs and connections

// getUrls('moaosint@gmail.com', '19/04/2023, 23:21:18')
//   .then(concatenatedList => {
//     console.log(concatenatedList.slice(0, 50));
//     // sending only first 50 elements unlisted
//     checkUrls(concatenatedList.slice(0, 50))
//   })
//   .catch(error => {
//     console.error(error);
//   });


// // example of real malicious urls for testing
// const URLS = [
//   'http://lists-prizes.fun/?u%5C=40dwkwf&o%5C=8vkp4zm&t%5C=arc4',
//   'https://datehub.life/?u=y2ykaew&o=2xzp89r&m=1&t=1504&utm_campaign=d4',
//   'https://romanceroundup.life/?u=54lkaeg&o=grmpkza&m=1&t=sexxys&cid=sexxys',
//   'http://landing.globify.in/wp-content/sidelightex.php?utm_campaign=rv'
// ];

// checkUrls(URLS);