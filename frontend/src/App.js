// import React, { useState } from 'react';
// import { detectNews } from './api';

// function App() {
//   const [text, setText] = useState('');
//   const [result, setResult] = useState('');

//   const handleDetect = async () => {
//     if (!text) return alert('Please enter some text!');
//     setResult('Detecting...');
//     try {
//       const res = await detectNews(text);
//       setResult(JSON.stringify(res, null, 2));
//     } catch (err) {
//       setResult('Error connecting to backend');
//       console.error(err);
//     }
//   };

//   return (
//     <div style={{ padding: '30px', fontFamily: 'Arial, sans-serif' }}>
//       <h1>📰 Fake News Detection</h1>
//       <textarea
//         value={text}
//         onChange={(e) => setText(e.target.value)}
//         placeholder="Enter news text here..."
//         style={{ width: '100%', height: '120px', fontSize: '16px', padding: '8px' }}
//       />
//       <button
//         onClick={handleDetect}
//         style={{
//           marginTop: '12px',
//           padding: '10px 20px',
//           backgroundColor: '#007bff',
//           color: '#fff',
//           border: 'none',
//           borderRadius: '4px',
//           cursor: 'pointer'
//         }}
//       >
//         Detect
//       </button>

//       <pre style={{ marginTop: '20px', whiteSpace: 'pre-wrap' }}>{result}</pre>
//     </div>
//   );
// }

// export default App;
import React, { useState } from 'react';
import { detectNews } from './api';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleDetect = async () => {
    if (!text.trim()) return alert('Please enter some text!');
    setResult('Detecting...');
    try {
      const res = await detectNews(text);
      setResult(JSON.stringify(res, null, 2));
    } catch (err) {
      setResult('Error connecting to backend. Check server or API key.');
      console.error(err);
    }
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial, sans-serif' }}>
      <h1>📰 Fake News Detection</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter news text here..."
        style={{ width: '100%', height: '120px', fontSize: '16px', padding: '8px' }}
      />
      <button
        onClick={handleDetect}
        style={{
          marginTop: '12px',
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer'
        }}
      >
        Detect
      </button>

      <pre style={{ marginTop: '20px', whiteSpace: 'pre-wrap' }}>{result}</pre>
    </div>
  );
}

export default App;
