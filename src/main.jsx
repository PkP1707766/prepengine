import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

// Clear the pre-JS boot placeholder painted by index.html.
const root = document.getElementById('root')
root.innerHTML = ''

createRoot(root).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
