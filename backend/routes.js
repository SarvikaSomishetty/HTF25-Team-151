// const { callFakeNewsAPI } = require('./apiClient');

// const detectFakeNews = async (req, res) => {
//   const { text } = req.body;
//   if (!text) return res.status(400).json({ error: 'No text provided' });

//   try {
//     const result = await callFakeNewsAPI(text);
//     res.json(result);
//   } catch (err) {
//     console.error(err);
//     res.status(500).json({ error: 'API call failed' });
//   }
// };

// module.exports = { detectFakeNews };
// routes.js
//-------------
// const { callFakeNewsAPI } = require('./apiClient');

// const detectFakeNews = async (req, res) => {
//   const { text } = req.body;

//   if (!text) return res.status(400).json({ error: 'No text provided' });

//   try {
//     const result = await callFakeNewsAPI(text);
//     res.json(result);
//   } catch (err) {
//     console.error('Error calling Fake News API:', err.message);
//     res.status(500).json({ error: 'Failed to detect fake news' });
//   }
// };

// module.exports = { detectFakeNews };
const { callFakeNewsAPI } = require('./apiClient');

const detectFakeNews = async (req, res) => {
  const { text } = req.body;

  if (!text) return res.status(400).json({ error: 'No text provided' });

  try {
    console.log('Sending text to Google Fact Check API:', text);
    const result = await callFakeNewsAPI(text);
    console.log('Google Fact Check API response:', result);
    res.json(result);
  } catch (err) {
    console.error('Backend API error:', err.response ? err.response.data : err.message);
    res.status(500).json({ error: 'Failed to detect fake news', details: err.message });
  }
};

module.exports = { detectFakeNews };
