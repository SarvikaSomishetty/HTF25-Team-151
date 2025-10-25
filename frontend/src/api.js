// export const detectNews = async (text) => {
//   const response = await fetch('http://localhost:5000/api/detect', {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({ text })
//   });

//   if (!response.ok) {
//     throw new Error('Failed to reach backend');
//   }

//   return response.json();
// };
// api.js
export const detectNews = async (text) => {
  const response = await fetch('/api/detect', {  // relative URL works with proxy
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });

  if (!response.ok) {
    throw new Error('Failed to reach backend');
  }

  return response.json();
};

