import ReactDOM from 'react-dom';

import './index.css';
import App from './App';
import './App.module.css'
import { AuthProvider } from './context/AuthProvider';

ReactDOM.render( <AuthProvider>
    <App />
  </AuthProvider>, document.getElementById('root'));

