// const axios = require('axios');

// const callFakeNewsAPI = async (text) => {
//   const apiKey = process.env.FAKE_NEWS_API_KEY; // your key
//   const response = await axios.post(
//     'https://fake-news-api-url.com/detect', // replace with real API URL
//     { text },
//     { headers: { 'Authorization': `Bearer ${apiKey}` } }
//   );
//   return response.data;
// };

// module.exports = { callFakeNewsAPI };
// apiClient.js
//--------------
// const axios = require('axios');

// const callFakeNewsAPI = async (text) => {
//   const apiKey = process.env.FAKE_NEWS_API_KEY; // make sure .env has this key
//   const apiUrl = process.env.FAKE_NEWS_API_URL; // add real API URL in .env

//   if (!apiKey || !apiUrl) {
//     throw new Error('API key or URL not set in environment variables');
//   }

//   try {
//     const response = await axios.post(
//       apiUrl,
//       { text },
//       { headers: { 
//           'Authorization': `Bearer ${apiKey}`,
//           'Content-Type': 'application/json'
//         } 
//       }
//     );
//     return response.data;
//   } catch (err) {
//     console.error('Axios request error:', err.response ? err.response.data : err.message);
//     throw err;
//   }
// };

// module.exports = { callFakeNewsAPI };
const axios = require('axios');

const callFakeNewsAPI = async (text) => {
  const apiKey = process.env.FAKE_NEWS_API_KEY;
  const url = process.env.FAKE_NEWS_API_URL;

  if (!apiKey || !url) {
    throw new Error('API key or URL not set in .env');
  }

  try {
    const response = await axios.get(url, {
      params: {
        query: text,
        key: apiKey,
        languageCode: 'en-US',
        pageSize: 5, // number of results you want
      },
    });

    return response.data;
  } catch (err) {
    console.error('Error calling Google Fact Check API:', err.response ? err.response.data : err.message);
    throw err;
  }
};

module.exports = { callFakeNewsAPI };

